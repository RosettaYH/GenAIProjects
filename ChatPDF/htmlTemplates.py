css = '''
<style>
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
    align-items: center;
    justify-content: flex-end; /* Aligns content to the end */
}

.chat-message.user {
    background-color: #e8e8e8;
    color: #333;
    flex-direction: row-reverse; /* Flips the order for user messages */
}

.chat-message.bot {
    background-color: #007bff;
    color: #fff;
    justify-content: flex-start; /* Aligns bot messages to the start */
}

.chat-message .avatar {
    width: 20%;
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <!-- Using a generic bot avatar image -->
        <img src="https://www.boostability.com/content/wp-content/uploads/sites/2/2021/02/Feb.-17-Bots-e1614642771145.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <!-- User avatar can remain the same or change to a more neutral image -->
        <img src="https://static.vecteezy.com/system/resources/previews/022/123/337/original/user-icon-profile-icon-account-icon-login-sign-line-vector.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''