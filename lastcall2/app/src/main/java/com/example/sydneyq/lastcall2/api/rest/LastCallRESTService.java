package com.example.sydneyq.lastcall2.api.rest;

import com.example.sydneyq.lastcall2.api.models.BarHopMeta;
import com.example.sydneyq.lastcall2.api.models.Hop;
import com.example.sydneyq.lastcall2.api.models.HopMember;

import java.util.Date;

import io.reactivex.Observable;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Path;

public interface LastCallRESTService {
    @POST("hop/make")
    Observable<BarHopMeta> createNewHop(
            @Body String start,
            @Body String end,
            @Body String name,
            @Body Date stime,
            @Body int duration);

    @POST("hop/join/{hopcode}")
    Observable<HopMember> joinHop(@Path("hopcode") String hopcode, @Body HopMember member);

    @POST("hop/exists/{hopcode}")
    Observable<Boolean> checkIfHopExists(@Path("hopcode") String hopcode);

    @GET("hop/member/{id}")
    Observable<HopMember> getMember(@Path("id") String id);

    @GET("hop/{hopId}")
    Observable<Hop> getHop(@Path("hopId") String hopId);

    @POST("hop/update/{memberId}")
    Observable<BarHopMeta> updateHop(@Path("memberId") String memberId, @Body Hop hop);
}

