// 登入頁
const forms1 = document.getElementById('formsent1')
const e_input_login = document.getElementById('email-input-login')
const p_input_login = document.getElementById('password-input-login')
const v_input_login = document.getElementById('verify-input-login')

// 註冊頁
const forms2 = document.getElementById('formsent2')
const f_name = document.getElementById('nickname')
const e_input = document.getElementById('email-input')
const p_input = document.getElementById('password-input')
const r_p_input = document.getElementById('repeat-password-input')
const v_input = document.getElementById('verify-input')

const error_message = document.getElementById('error-message')

// 註冊錯誤
forms2.addEventListener('submit', (e) => {
    let error = []

    error = getSignUpFormErrors(f_name.value, e_input.value, p_input.value, r_p_input.value, v_input.value) 

    if (error.length > 0) {
        e.preventDefault()
        error_message.innerText = error.join('. ')
    }
})


const allinput1 = [f_name,e_input,p_input,r_p_input,v_input].filter(input => input != null)
// 清除錯誤訊息
allinput1.forEach(input => {
    input.addEventListener('input', () => {
        if (input.parentElement.classList.contains('incorrect')){
            input.parentElement.classList.remove('incorrect')
            error_message.innerText = ''
        }
    })
})



function getSignUpFormErrors(f_name_s, e_input_s, p_input_s, r_p_input_s, verify) {
    let error = []
    if (f_name_s === '' || f_name_s == null) {
        // 增加錯誤解釋到列表末端
        error.push('請輸入用戶名')
        // 增加class屬性
        f_name.parentElement.classList.add('incorrect')
    }

    if (e_input_s === '' || e_input_s == null) {
        error.push('請輸入信箱')
        e_input.parentElement.classList.add('incorrect')
    }

    if (p_input_s === '' || p_input_s == null) {
        error.push('請輸入密碼')
        p_input.parentElement.classList.add('incorrect')
    }

    if (verify === '' || verify == null) {
        error.push('請輸入驗證碼')
        v_input.parentElement.classList.add('incorrect')
    }

    if (p_input_s !== r_p_input_s){
        error.push('密碼不一致')
        r_p_input.parentElement.classList.add('incorrect')
    }

    return error
}

// 登入錯誤
forms1.addEventListener('submit', (e) => {
    let error = []
    error = getLogInFormErrors(e_input_login.value, p_input_login.value, v_input_login.value)

    if (error.length > 0) {
        e.preventDefault()
        error_message.innerText = error.join('. ')        
    }    
})

function getLogInFormErrors(e_input_s, p_input_s, verify) {
    let error = []

    if (e_input_s === '' || e_input_s == null) {
        error.push('請輸入信箱')
        e_input_login.parentElement.classList.add('incorrect')
    }

    if (p_input_s === '' || p_input_s == null) {
        error.push('請輸入密碼')
        p_input_login.parentElement.classList.add('incorrect')
    }

    if (verify === '' || verify == null) {
        error.push('請輸入驗證碼')
        v_input_login.parentElement.classList.add('incorrect')
    }

    return error
}


const allinput2 = [e_input_login,p_input_login,v_input_login].filter(input => input != null)
// 清除錯誤訊息
allinput2.forEach(input => {
    input.addEventListener('input', () => {
        if (input.parentElement.classList.contains('incorrect')){
            input.parentElement.classList.remove('incorrect')
            error_message.innerText = ''
        }
    })
})
