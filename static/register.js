const registerForm = document.getElementById('registerForm');
registerForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(registerForm);
    const username = formData.get('username');
    const password = formData.get('password');
    const confirm = formData.get('confirm');

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

         // 在这里进行页面跳转
        window.location.href = '/login';

    } catch (error) {
        console.error('Error registering:', error);
    }
});