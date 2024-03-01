const registerForm = document.getElementById('registerForm');

function checkAllFields(formData) {
    

    const username = formData.get('username');
    const password = formData.get('password');
    const confirm = formData.get('confirm');

    if (confirm!=password)
        return "两个密码不一致"


    // 逐个判断字段的值长度和是否只包含键盘字符
    if (username.trim().length < 3 ||username.trim().length > 20)
        return "用户名长度为3-16个字符"
    
    
    if(password.trim().length < 3 ||password.trim().length > 20 ||!/^[a-zA-Z0-9!@#$%^&*()_+-=]+$/.test(password)) {
        return "密码为长度为3-16个数字字母特殊字符"
    }

    return true
}


registerForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(registerForm);
    const username = formData.get('username');
    const password = formData.get('password');
    const confirm = formData.get('confirm');
    allFieldsHaveContent = checkAllFields(formData)

    if (allFieldsHaveContent!=true) {
        alert(allFieldsHaveContent)
        return false
    }

    try {
        const response = await fetch('/api/adduser', {
            method: 'POST',
            credentials: 'include' ,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password ,confirm})
        });
        const data = await response.json();
        console.log(data); // 可以根据后端返回的数据做进一步处理// 在这里进行页面跳转
           
        if (data["code"] == "400")
            alert("用户名已存在")

        if (data["code"] == "ok")
            window.location.href = '/login';

         // 在这里进行页面跳转
       

    } catch (error) {
        console.error('Error registering:', error);
    }
});