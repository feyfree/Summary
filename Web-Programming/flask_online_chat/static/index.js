//如果新用户进来，输入用户角色
if (!localStorage.getItem('display_name') && !localStorage.getItem('current_channel') && !localStorage.getItem('comment_stack') ) {
    var username = prompt('Enter a display name ');
    localStorage.setItem('display_name', username);
    localStorage.setItem('current_channel', 'general');
    localStorage.setItem('comment_stack', JSON.stringify({'general': 110}));
}


const template = Handlebars.compile(document.querySelector('#load-messages').innerHTML);
const template_title = Handlebars.compile(document.querySelector('#load-channel-title').innerHTML);

// 加载当前角色的信息
document.addEventListener('DOMContentLoaded', () => {

    // 连接至Web Socket， 用于动态接收和发送消息
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // 从local storage获取当前的信息并显示
    var username = localStorage.getItem('display_name');
    document.querySelector('#user').innerHTML = username;

    var current_channel = localStorage.getItem('current_channel');
    const channel_to_display = template_title({'channel_to_display': current_channel});
    var channel_element = channel_to_display, parser = new DOMParser(), doc = parser.parseFromString(channel_element, 'text/xml');
    document.querySelector('#message-view').prepend(doc.querySelector('#channel-title'));

    function asynch_load_messages(request, refresh) {
        /*
        解析JSON数据
        */
        const data = JSON.parse(request.responseText);
        for(var i = 0; i < data.length; i++) {
            const comment = template({'comment': data[i]});
            document.querySelector('#comment-list').innerHTML += comment;
        }
        let comment_stack = JSON.parse(localStorage.getItem('comment_stack'));
        document.querySelector('#comment-list').style.paddingTop = `${comment_stack[current_channel]}%`;
        var comment_count = document.querySelector('#comment-list').childElementCount;
        if (comment_count > 0) {
            document.querySelector('#comment-list').lastElementChild.scrollIntoView();
        }

        if(refresh) {
            document.querySelectorAll('#submit-switch-channel').forEach(button => {
                if(button.value == current_channel) {
                    button.parentElement.style.backgroundColor = '#8C93B3';
                    button.firstElementChild.style.color = '#171C2F';
                }
            });
        }

        return false;
    }

    function channel_switch() {
        /* 
        定义频道按钮属性
        */

        console.log(this.value);

        // 切换频道时候，更新信息
        var room_to_leave = localStorage.getItem('current_channel');
        if(this.value != room_to_leave) {
            var current_channel = this.value;
            var current_user = localStorage.getItem('display_name');

            document.querySelectorAll('#submit-switch-channel').forEach(button => {
                if(button.value == current_channel) {
                    button.parentElement.style.backgroundColor = '#8C93B3';
                    button.firstElementChild.style.color = '#171C2F';
                }
                else if(button.value == room_to_leave) {
                    button.parentElement.style.backgroundColor = '#171C2F';
                    button.firstElementChild.style.color = '#8C93B3';
                }
            });

            socket.emit('join', current_channel);
            socket.emit('leave', room_to_leave);

            localStorage.setItem('current_channel', current_channel);
            document.querySelector('#comment-list').innerHTML = '';

            // 生成新的信息
            const request = new XMLHttpRequest();
            request.open('POST', '/');
            request.onload = asynch_load_messages.bind(null, request, refresh=false);
            const data = new FormData();
            data.append('channel_name', localStorage.getItem('current_channel'));
            document.querySelector('#channel-title').innerHTML = localStorage.getItem('current_channel');
            request.send(data);
            return false;

        }
        else {
            return false;
        }
    }

    function prevent_blank_text_entry(input_id, button_id) {
        /* 默认按钮Disabled，除非用户进入频道 */
        document.querySelector(button_id).disabled = true;

        document.querySelector(input_id).onkeyup = () => {
            if(document.querySelector(input_id).value.length > 0) {
                document.querySelector(button_id).disabled = false;
            }
            else {
                document.querySelector(button_id).disabled = true;
            }
        };
    }

    // 从服务器生成信息给用户
    const request = new XMLHttpRequest();
    request.open('POST', '/');
    request.onload = asynch_load_messages.bind(null, request, refresh=true);
    const data = new FormData();
    data.append('username', username);
    data.append('channel_name', current_channel);
    request.send(data);

    // 生成信息界面给用户，检查发送信息按钮，发送信息给用户
    socket.on('connect', () => {
       socket.emit('join', current_channel);

       document.querySelectorAll('#submit-switch-channel').forEach(button => {
            button.onclick = channel_switch;
        });

       prevent_blank_text_entry('#message-input', '#submit-send-message');
       document.querySelector('#submit-send-message').onclick = () => {
           /* 发送信息事件 */

           var message_content = document.querySelector('#message-input').value
           var timestamp = new Date();
           timestamp = timestamp.toLocaleString('en-US');
           var user = username;
           var current_channel = localStorage.getItem('current_channel');
           var delete_channel = `command delete ${current_channel}`;

           /* 超级用户可以删除频道 */
           if( (user == 'superuser') && (message_content == delete_channel) && (current_channel != 'general') )
           {
               user = "mod";
               message_content = `mod has deleted channel ${current_channel}`;
               let message_data = {"message_content": message_content, "timestamp": timestamp, "user":user, "current_channel": current_channel };

               console.log(message_data);
               document.querySelector('#message-input').value = '';
               socket.emit('delete channel', message_data);
               document.querySelector('#submit-send-message').disabled = true;

               return false;

           }
           else {
               if(user == 'superuser') {
                   user = 'mod';
               }
               let message_data = {"message_content": message_content, "timestamp": timestamp, "user":user, "current_channel": current_channel };
               console.log(message_data);
               document.querySelector('#message-input').value = '';
               socket.emit('send message', message_data);
               document.querySelector('#submit-send-message').disabled = true;

               return false;
           }
       };

    });

    // 当信息广播到频道，接受信息并且显示
    socket.on('recieve message', message_data => {
        // 创建消息元素，并添加显示

        const li = document.createElement('li');
        li.setAttribute('class', 'media comment-item');

        const div_media_body = document.createElement('div');
        div_media_body.setAttribute('class', 'media-body comment-media');

        const h5 = document.createElement('h5');
        h5.setAttribute('class', 'mt-0 mb-1 comment-user');
        let midpt = '&middot';
        let space = '\u0020';
        h5.innerHTML = `${message_data["user"]}${space}${midpt}${space}`;

        const div_time = document.createElement('div');
        div_time.setAttribute('class', 'comment-time');
        div_time.setAttribute('id', 'time');
        div_time.innerHTML = message_data["timestamp"];

        const div_comment = document.createElement('div');
        div_comment.setAttribute('class', 'comment-comment');
        div_comment.innerHTML = message_data["message_content"];

        div_media_body.appendChild(h5);
        div_media_body.appendChild(div_time);
        div_media_body.appendChild(div_comment);

        li.appendChild(div_media_body);

        document.querySelector('#comment-list').append(li);
        if(!message_data['deleted_message']) {
            let comment_stack = JSON.parse(localStorage.getItem('comment_stack'));
            let current_channel = localStorage.getItem('current_channel');
            comment_stack[current_channel] -= 10;
            localStorage.setItem('comment_stack', JSON.stringify(comment_stack));
            document.querySelector('#comment-list').style.paddingTop = `${comment_stack[current_channel]}%`;
        }
        li.scrollIntoView();
    });

    socket.on('announce channel deletion', message_data => {
        var deleted_channel = message_data["deleted_channel"];
        message_data = message_data["data"];
        socket.emit('join', 'general');
        socket.emit('leave', deleted_channel);

        document.querySelector('#comment-list').innerHTML = '';
        document.querySelector('#channel-title').remove();

        var comment_stack = JSON.parse(localStorage.getItem('comment_stack'));
        delete comment_stack[deleted_channel];
        localStorage.setItem('comment_stack', JSON.stringify(comment_stack));
        document.querySelectorAll('#submit-switch-channel').forEach(button => {
            if(button.value == deleted_channel) {
                button.parentElement.remove();
            }
            else if(button.value == localStorage.getItem('current_channel')) {
                button.parentElement.style.backgroundColor = '#171C2F';
                button.firstElementChild.style.color = '#8C93B3';
            }
        });
        localStorage.setItem('current_channel', 'general');
        document.querySelectorAll('#submit-switch-channel').forEach(button => {
            if(button.value == localStorage.getItem('current_channel')) {
                button.parentElement.style.backgroundColor = '#8C93B3';
                button.firstElementChild.style.color = '#171C2F';
            }
        });

        const channel_to_display = template_title({'channel_to_display': localStorage.getItem('current_channel')});
        var channel_element = channel_to_display, parser = new DOMParser(), doc = parser.parseFromString(channel_element, 'text/xml');
        document.querySelector('#message-view').prepend(doc.querySelector('#channel-title'));

        var data = message_data;
        for(var i = 0; i < data.length; i++) {
            const comment = template({'comment': data[i]});
            document.querySelector('#comment-list').innerHTML += comment;
        }
        document.querySelector('#comment-list').style.paddingTop = `${comment_stack[localStorage.getItem('current_channel')]}%`;
        var comment_count = document.querySelector('#comment-list').childElementCount;
        if (comment_count > 0) {
            document.querySelector('#comment-list').lastElementChild.scrollIntoView();
        }
    });

    // 设置添加频道属性
    prevent_blank_text_entry('#channel', '#submit-add-channel');
    document.querySelector('#add-channel-form').onsubmit = () => {
        const channel_name = document.querySelector('#channel').value;
        var comment_stack = JSON.parse(localStorage.getItem('comment_stack'));
        if( !(channel_name in comment_stack) ) {

            socket.emit('create channel', channel_name);

            // 保存消息信息comment_stack给所有用户
            socket.on('new channel', new_channel => {
                var comment_stack = JSON.parse(localStorage.getItem('comment_stack'));
                comment_stack[new_channel] = 110;
                localStorage.setItem('comment_stack', JSON.stringify(comment_stack));
            });

            // 建立频道
            // 假定请求正常，并添加至前端显示
            // 如果请求失败，从页面杀出
            const form = document.createElement('form');
            form.setAttribute('id', 'switch-channel-form');

            const button = document.createElement('button');
            button.id = 'submit-switch-channel';
            button.setAttribute('type', 'submit');
            button.setAttribute('value', channel_name);
            button.onclick = channel_switch;

            const li = document.createElement('li');
            li.innerHTML = `# ${channel_name}`;
            li.setAttribute('id','channel-option');

            button.appendChild(li);
            form.appendChild(button);
            console.log(form);
            document.querySelector('#channels').append(form);

            document.querySelector('#channel').value = '';
            document.querySelector('#submit-add-channel').disabled = true;

            // 建立Ajax连接至flask server
            const request = new XMLHttpRequest();
            request.open('POST', '/');

            // 确保响应成功，并且发送信息成功
            request.onload = () => {
                const data = JSON.parse(request.responseText);
                if(data.success) {
                    console.log("Keeping added channel UI clientside");
                }
                else {
                    console.log("Server did not process request to add new channel, deleting channel UI");
                    document.querySelector('#channels').lastElementChild.remove();
                }
            }

            const data = new FormData();
            data.append('channel_name', channel_name);
            request.send(data);

            return false;

        }
        else {
            document.querySelector('#channel').value = '';
            document.querySelector('#submit-add-channel').disabled = true;
            alert("Channel already exists");
            return false;
        }
    };

});

