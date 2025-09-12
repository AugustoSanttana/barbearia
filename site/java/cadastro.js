const url = 'http://127.0.0.1:5000/user_routes/cadastrar';

async function cadastro() {
    let name = document.getElementById('name').value;
    let cpf = document.getElementById('cpf').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let endereco = document.getElementById('endereco').value;

    if (!name || !email || !password || !cpf || !endereco) {
        alert("Todos os campos são obrigatórios.");
        return;
    }

    try {
        let response = await fetch(url, {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, user_type_id: 1, password, cpf, endereco })
        });

        let data = await response.json();

        if (response.ok) {
            console.log(data);
            alert(data.mensagem);
            window.location.href = '../html/home.html';
        } else {
            let errorMessage = "Erro no cadastro. Por favor, tente novamente.";

            if (data.data && data.data.errors) {
                if (data.data.errors.cpf_cnpj) errorMessage = data.data.errors.cpf_cnpj[0];
                else if (data.data.errors.email) errorMessage = data.data.errors.email[0];
                else if (data.data.errors.password) errorMessage = data.data.errors.password[0];
            }

            alert(errorMessage);
        }

    } catch (error) {
        console.error("Erro na requisição:", error);
        alert("Erro no cadastro, CPF/CNPJ já utilizado. Por favor, tente novamente.");
    }
}

// Previne reload do form e chama a função cadastro()
document.getElementById('cadastroForm').addEventListener('submit', function(event) {
    event.preventDefault();
    cadastro();
});