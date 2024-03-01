const registerForm = document.getElementById('LoginForm');

function checkAllFields(formData) {
    for (let value of formData.values()) {
        if (!value.trim()) {
            return false; // 如果有任何一个字段的值为空，则返回 false
        }
    }
    return true; // 所有字段都有内容，返回 true
}


registerForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(registerForm);

    allFieldsHaveContent = checkAllFields(formData)

    if (!allFieldsHaveContent) {
        alert('输入用户名或密码')
        return false
    }
    
   
    
    const username = formData.get('username');
    const password = formData.get('password');
  

    try {
        const response = await fetch('api/login', {
            method: 'POST',
            credentials: 'include' ,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        console.log(data); // 可以根据后端返回的数据做进一步处理
        


        if (data["code"] == "ok")
            window.location.href = '/index';

        if (data["code"] == "error")
            alert('用户名或密码错误!')



        
    } catch (error) {
        console.error('Error registering:', error);
    }
});