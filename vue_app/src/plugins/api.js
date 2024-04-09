import { request } from "./request";

export function getAllCountries(data) {
    return request({
        url:'/countries/all_country_data',
        method: 'get',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function getAllUser(data) {
    return request({
        url:'/security/list_users',
        method: 'get',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function getLandingstatus(data) {
    return request({
        url:'/funds/landing_stats',
        method: 'get',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function getAllStaff(data) {
    return request({
        url:'/security/list_staff',
        method: 'get',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function getAllHouseType(data) {
    return request({
        url:'/house/read_list',
        method: 'get',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function insertUser(data) {
    return request({
        url:'/security/create_user',
        method: 'post',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function insertStaff(data) {
    return request({
        url:'/security/create_staff',
        method: 'post',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function editUser(data) {
    return request({
        url:'/security/edit_user',
        method: 'post',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function deleteUser(data) {
    return request({
        url:'/security/remove_user',
        method: 'post',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function getAllHouseList(data) {
    return request({
        url:'/house/read_info',
        method: 'get',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function upgradeStaff(data) {
    return request({
        url:'/security/add_roles',
        method: 'post',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function addFundingToServer(data) {
    return request({
        url:'/funds/add',
        method: 'post',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function getChart1Data(data) {
    return request({
        url:'/funds/fund_date',
        method: 'get',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function getChart2Data(data) {
    return request({
        url:'/funds/fund_countries',
        method: 'get',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}

export function signIn(data) {
    return request({
        url:'/security/login',
        method: 'post',
        data,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Headers': 'x-requested-with,content-type'
        }
    })
}
