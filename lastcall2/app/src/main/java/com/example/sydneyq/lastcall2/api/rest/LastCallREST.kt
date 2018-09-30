package com.example.sydneyq.lastcall2.api.rest

import retrofit2.Retrofit

val BASE_URL = "http://localhost"
var retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .build()

var lastCallREST: LastCallRESTService = retrofit.create(LastCallRESTService::class.java)