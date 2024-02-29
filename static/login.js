const registerForm = document.getElementById('LoginForm');
registerForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(registerForm);
    const username = formData.get('username');
    const password = formData.get('password');
  

    try {
        const response = await fetch('api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        console.log(data); // 可以根据后端返回的数据做进一步处理

        window.location.href = '/index';
    } catch (error) {
        console.error('Error registering:', error);
    }
});