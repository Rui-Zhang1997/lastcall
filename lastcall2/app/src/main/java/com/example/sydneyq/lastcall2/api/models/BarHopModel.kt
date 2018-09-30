package com.example.sydneyq.lastcall2.api.models

import java.io.Serializable
import java.util.*

enum class Crowdedness {
    EMPTY, MODERATE, CROWDED
}

enum class Tolerance {
    LIGHTWEIGHT, MODERATE, STAGGERED
}

data class BarHopMeta(
        val hopId: String? = null,
        var hopName: String,
        var sll: String,
        var ell: String,
        var stime: Date,
        var barCount: Int,
        var duration: Int) : Serializable

data class HopMember(
        val memberId: Int? = null,
        var memberName: String,
        var drunkLevel: Tolerance,
        var maxCost: Int,
        var crowdSize: Crowdedness,
        var currentHop: String) : Serializable

data class BarData(
        val barId: String,
        val barName: String,
        var barAddress: String,
        val barRating: String,
        val barCost: Int) : Serializable

data class DrinkData(
        val drinkName: String,
        val drinkCost: Float,
        val alcoholVol: Int,
        val incredients: Array<String>) : Serializable

data class Hop(val hopId: String,
               val bars: Array<BarData>) : Serializable
