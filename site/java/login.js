const urlLogin = 'http://127.0.0.1:5000/user_routes/login';

async function login() {
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    if (!email || !password) {
        alert("Preencha todos os campos.");
        return;
    }

    try {
        let response = await fetch(urlLogin, {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, senha: password }) 
        });

        let data = await response.json();

        if (response.ok) {
            console.log("Resposta da API:", data);
            alert("Login realizado com sucesso!");

            if (data.token) {
                localStorage.setItem("token", data.token);
            }

            window.location.href = '../html/home_perfil.html';
        } else {
            alert(data.erro || "Credenciais inválidas.");
        }

    } catch (error) {
        console.error("Erro na requisição:", error);
        alert("Erro no servidor. Tente novamente mais tarde.");
    }
}

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    login();
});
