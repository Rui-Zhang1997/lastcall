package com.example.sydneyq.lastcall2.api.models

import java.util.*

enum class Crowdedness {
    EMPTY, MODERATE, CROWDED
}

enum class Tolerance {
    LIGHTWEIGHT, MODERATE, STAGGERED
}

data class BarHopMeta(
        val hopCode: String? = null,
        var hopName: String,
        var sll: String,
        var ell: String,
        var stime: Date,
        var duration: Int)

data class HopMember(
        val memberId: Int,
        var memberName: String,
        var drunkLevel: Tolerance,
        var maxCost: Int,
        var crowdSize: Crowdedness
)

data class Hop(val hopId: String)
