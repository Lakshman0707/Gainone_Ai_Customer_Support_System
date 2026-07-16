// ==========================================
// GainOne AI Customer Support System
// script.js
// Block 1
// ==========================================

// ==========================================
// API URL
// ==========================================

const API_URL = "http://127.0.0.1:8000";


// ==========================================
// CUSTOMER LOGIN
// ==========================================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async function(e){

        e.preventDefault();

        const email = document.getElementById("email").value.trim();

        const password = document.getElementById("password").value.trim();

        try{

            const response = await fetch(API_URL + "/auth/login",{

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({

                    email:email,

                    password:password

                })

            });

            const data = await response.json();

            if(response.ok){

                localStorage.setItem("token",data.access_token);

                localStorage.setItem("user_id",data.user_id);

                localStorage.setItem("user_name",data.name);

                localStorage.setItem("user_email",data.email);

                localStorage.setItem("role",data.role);

                alert("Login Successful");

                window.location.href="dashboard.html";

            }

            else{

                alert(data.detail);

            }

        }

        catch(error){

            console.log(error);

            alert("Unable to connect to server.");

        }

    });

}


// ==========================================
// CUSTOMER REGISTER
// ==========================================

const registerForm = document.getElementById("registerForm");

if(registerForm){

    registerForm.addEventListener("submit",async function(e){

        e.preventDefault();

        const name=document.getElementById("name").value.trim();

        const email=document.getElementById("email").value.trim();

        const password=document.getElementById("password").value.trim();

        try{

            const response=await fetch(API_URL+"/auth/register",{

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify({

                    name:name,

                    email:email,

                    password:password

                })

            });

            const data=await response.json();

            if(response.ok){

                alert("Registration Successful");

                window.location.href="login.html";

            }

            else{

                alert(data.detail);

            }

        }

        catch(error){

            console.log(error);

            alert("Unable to connect to backend.");

        }

    });

}


// ==========================================
// CUSTOMER DASHBOARD
// ==========================================

const totalChats=document.getElementById("totalChats");

const totalTickets=document.getElementById("totalTickets");

if(totalChats && totalTickets){

    const userId=localStorage.getItem("user_id");

    if(!userId){

        window.location.href="login.html";

    }

    else{

        fetch(API_URL+"/customer/dashboard/"+userId)

        .then(res=>res.json())

        .then(data=>{

            totalChats.innerHTML=data.total_chats;

            totalTickets.innerHTML=data.total_tickets;

        })

        .catch(err=>console.log(err));

    }

}


// ==========================================
// CUSTOMER LOGOUT
// ==========================================

// ==========================================
// CUSTOMER LOGOUT
// ==========================================

async function logout(){

    const userId = localStorage.getItem("user_id");

    try{

        if(userId){

            await fetch(
                API_URL + "/conversation/logout-summary/" + userId,
                {
                    method: "POST"
                }
            );

        }

    }

    catch(error){

        console.log(error);

    }

    localStorage.removeItem("token");
    localStorage.removeItem("user_id");
    localStorage.removeItem("user_name");
    localStorage.removeItem("user_email");
    localStorage.removeItem("role");

    alert("Logged Out Successfully");

    window.location.href = "login.html";

}// ==========================================
// AI CHAT
// ==========================================

async function sendMessage() {

    const questionBox = document.getElementById("question");
    const chatBox = document.getElementById("chatBox");

    if (!questionBox || !chatBox) return;

    const question = questionBox.value.trim();

    if (question === "") return;

    const userId = localStorage.getItem("user_id");

    if (!userId) {

        alert("Please login first.");

        window.location.href = "login.html";

        return;

    }

    chatBox.innerHTML += `
        <div class="user">
            <b>You:</b><br>${question}
        </div>
    `;

    questionBox.value = "";

    try {

        const response = await fetch(API_URL + "/chatbot/ask", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                user_id: Number(userId),

                question: question

            })

        });

        const data = await response.json();

        if (response.ok) {

            chatBox.innerHTML += `
                <div class="bot">
                    <b>AI:</b><br>${data.answer}
                </div>
            `;

        }

        else {

            chatBox.innerHTML += `
                <div class="bot">
                    <b>AI:</b><br>${data.detail}
                </div>
            `;

        }

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    catch (error) {

        console.log(error);

        chatBox.innerHTML += `
            <div class="bot">
                <b>AI:</b><br>
                Unable to connect to backend.
            </div>
        `;

    }

}


// ==========================================
// CUSTOMER PROFILE
// ==========================================

const profileName = document.getElementById("name");

const profileEmail = document.getElementById("email");

const profileRole = document.getElementById("role");

if (profileName && profileEmail && profileRole) {

    const userId = localStorage.getItem("user_id");

    if (!userId) {

        window.location.href = "login.html";

    }

    else {

        fetch(API_URL + "/customer/profile/" + userId)

        .then(res => res.json())

        .then(user => {

            profileName.innerHTML = user.name;

            profileEmail.innerHTML = user.email;

            profileRole.innerHTML = user.role;

        })

        .catch(err => console.log(err));

    }

}


// ==========================================
// MY TICKETS
// ==========================================

const ticketTable = document.querySelector("#ticketTable tbody");

if (ticketTable) {

    const userId = localStorage.getItem("user_id");

    fetch(API_URL + "/customer/tickets/" + userId)

    .then(res => res.json())

    .then(data => {

        ticketTable.innerHTML = "";

        if (data.length === 0) {

            ticketTable.innerHTML = `

            <tr>

                <td colspan="4">

                    No Tickets Found

                </td>

            </tr>

            `;

            return;

        }

        data.forEach(ticket => {

            ticketTable.innerHTML += `

            <tr>

                <td>${ticket.id}</td>

                <td>${ticket.issue}</td>

                <td>${ticket.priority}</td>

                <td>${ticket.status}</td>

            </tr>

            `;

        });

    })

    .catch(err => console.log(err));

}


// ==========================================
// CHAT HISTORY
// ==========================================

const historyContainer = document.getElementById("history");

if (historyContainer) {

    const userId = localStorage.getItem("user_id");

    fetch(API_URL + "/conversation/history/" + userId)

    .then(res => res.json())

    .then(history => {

        historyContainer.innerHTML = "";

        if (history.length === 0) {

            historyContainer.innerHTML = "<h3>No Chat History</h3>";

            return;

        }

        history.forEach(chat => {

            historyContainer.innerHTML += `

            <div class="card">

                <h4>Question</h4>

                <p>${chat.question}</p>

                <h4>Answer</h4>

                <p>${chat.answer}</p>

                <hr>

            </div>

            `;

        });

    })

    .catch(err => console.log(err));

}
// ==========================================
// ADMIN LOGIN
// ==========================================

const adminLoginForm = document.getElementById("adminLoginForm");

if (adminLoginForm) {

    adminLoginForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        const email = document.getElementById("adminEmail").value.trim();
        const password = document.getElementById("adminPassword").value.trim();

        try {

            const response = await fetch(API_URL + "/admin/login", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    email: email,
                    password: password

                })

            });

            const data = await response.json();

            if (response.ok) {

                localStorage.setItem("admin_token", data.access_token);
                localStorage.setItem("admin_id", data.admin_id);
                localStorage.setItem("admin_name", data.name);

                window.location.href = "admin_dashboard.html";

            }

            else {

                alert(data.detail);

            }

        }

        catch (error) {

            console.log(error);

            alert("Unable to connect to backend.");

        }

    });

}


// ==========================================
// ADMIN DASHBOARD
// ==========================================

const customerTable = document.getElementById("customerTable");

if (customerTable) {

    if (!localStorage.getItem("admin_token")) {

        window.location.href = "admin_login.html";

    }

    document.getElementById("adminName").innerHTML =
        localStorage.getItem("admin_name");

    fetch(API_URL + "/admin/dashboard")

        .then(res => res.json())

        .then(data => {

            document.getElementById("adminTotalUsers").innerHTML =
                data.total_users;

            document.getElementById("adminTotalChats").innerHTML =
                data.total_chats;

            document.getElementById("adminTotalTickets").innerHTML =
                data.total_tickets;

            document.getElementById("adminTotalDocuments").innerHTML =
                data.total_documents;

        });

    fetch(API_URL + "/admin/customers")

        .then(res => res.json())

        .then(customers => {

            customerTable.innerHTML = "";

            customers.forEach(customer => {

                customerTable.innerHTML += `

                <tr>

                    <td>${customer.id}</td>

                    <td>${customer.name}</td>

                    <td>${customer.email}</td>

                    <td>${customer.total_chats}</td>

                    <td>${customer.total_tickets}</td>

                    <td>

                        <button onclick="viewCustomer(${customer.id})">

                            View

                        </button>

                    </td>

                </tr>

                `;

            });

        });

}

function viewCustomer(id){

    window.location.href =
        "customer_history.html?id=" + id;

}


// ==========================================
// ADMIN CUSTOMER HISTORY
// ==========================================

const historyDiv = document.getElementById("history");

if(historyDiv){

    const params = new URLSearchParams(window.location.search);

    const id = params.get("id");

    fetch(API_URL+"/admin/customer/"+id)

    .then(res=>res.json())

    .then(user=>{

        document.getElementById("customerInfo").innerHTML=`

        <h2>${user.name}</h2>

        <p>Email : ${user.email}</p>

        <p>Total Chats : ${user.total_chats}</p>

        <p>Total Tickets : ${user.total_tickets}</p>

        <hr>

        `;

    });


    fetch(API_URL+"/admin/customer/"+id+"/history")

    .then(res=>res.json())

    .then(history=>{

        historyDiv.innerHTML="";

        history.forEach(chat=>{

            historyDiv.innerHTML += `

            <div class="card">

                <h3>Question</h3>

                <p>${chat.question}</p>

                <h3>Answer</h3>

                <p>${chat.answer}</p>

                <hr>

            </div>

            `;

        });

    });

}


// ==========================================
// ADMIN TICKETS
// ==========================================

const adminTicketTable = document.getElementById("adminTicketTable");

if(adminTicketTable){

    loadTickets();

}

function loadTickets(){

    fetch(API_URL+"/admin/tickets")

    .then(res=>res.json())

    .then(data=>{

        adminTicketTable.innerHTML="";

        data.forEach(ticket=>{

            adminTicketTable.innerHTML += `

            <tr>

                <td>${ticket.ticket_id}</td>

                <td>${ticket.customer}</td>

                <td>${ticket.email}</td>

                <td>${ticket.issue}</td>

                <td>${ticket.priority}</td>

                <td>${ticket.status}</td>

                <td>${ticket.assigned_agent}</td>

                <td>

                    <button onclick="closeTicket(${ticket.ticket_id})">

                        Close

                    </button>

                </td>

            </tr>

            `;

        });

    });

}

async function closeTicket(ticketId){

    if(!confirm("Close Ticket?")) return;

    const response = await fetch(API_URL+"/tickets/close",{

        method:"PUT",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            ticket_id:ticketId

        })

    });

    const data = await response.json();

    alert(data.message);

    loadTickets();

}


// ==========================================
// ADMIN LOGOUT
// ==========================================

function adminLogout(){

    localStorage.removeItem("admin_token");
    localStorage.removeItem("admin_id");
    localStorage.removeItem("admin_name");

    window.location.href="admin_login.html";

}