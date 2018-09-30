package com.example.sydneyq.lastcall2.fragments


import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup

import com.example.sydneyq.lastcall2.R
import com.example.sydneyq.lastcall2.api.models.BarData
import com.example.sydneyq.lastcall2.api.models.DrinkData
import io.reactivex.subjects.PublishSubject
import kotlinx.android.synthetic.main.bar_list_item.view.*
import kotlinx.android.synthetic.main.drink_list_item.view.*
import kotlinx.android.synthetic.main.fragment_list.*
import org.apache.commons.lang3.StringUtils

/**
 * A simple [Fragment] subclass.
 *
 */
class BarViewHolder(val v: View) : RecyclerView.ViewHolder(v) {
    fun bind(data: BarData, listener: (BarData) -> Unit) = with(itemView) {
        bar_name.text = data.barName
        bar_address.text = data.barAddress
        bar_rating.text = data.barRating
        bar_cost.text = data.barCost.toString()
        setOnClickListener { listener(data) }
    }
}

class BarListAdapter(val data: Array<BarData>, val sub: PublishSubject<BarData>) : RecyclerView.Adapter<BarViewHolder>() {
    override fun getItemCount(): Int {
        return data.size
    }

    override fun getItemViewType(position: Int): Int {
        return position % 2;
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): BarViewHolder {
        if (viewType == 0) {
            return BarViewHolder(LayoutInflater.from(parent.context)
                    .inflate(R.layout.bar_list_item, parent, false) as View)
        } else {
            return BarViewHolder(LayoutInflater.from(parent.context)
                    .inflate(R.layout.bar_list_item_red, parent, false) as View)
        }
    }

    override fun onBindViewHolder(holder: BarViewHolder, position: Int) {
        holder.bind(data.get(position), { data ->
            sub.onNext(data)
        })
    }
}

class DrinkViewHolder(val v: View) : RecyclerView.ViewHolder(v) {
    fun bind(data: DrinkData, listener: (BarData) -> Unit) = with(itemView) {
        drink_price.text = data.drinkCost.toString()
        drink_title.text = data.drinkName
        drink_alcohol.text = data.drinkName
        drink_ingredients.text = StringUtils.join(data.incredients, ",")
    }
}

class DrinkListAdapter(val data: Array<DrinkData>) : RecyclerView.Adapter<DrinkViewHolder>() {
    override fun getItemCount(): Int {
        return data.size
    }

    override fun getItemViewType(position: Int): Int {
        return position % 2;
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DrinkViewHolder {
        if (viewType == 0) {
            return DrinkViewHolder(LayoutInflater.from(parent.context)
                    .inflate(R.layout.drink_list_item, parent, false) as View)
        } else {
            return DrinkViewHolder(LayoutInflater.from(parent.context)
                    .inflate(R.layout.drink_list_item_red, parent, false) as View)
        }
    }

    override fun onBindViewHolder(holder: DrinkViewHolder, position: Int) {
        holder.bind(data.get(position), { data -> null })
    }
}

class SlideUpListFragment : Fragment() {
    val barSelectedSubject = PublishSubject.create<BarData>()
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        val args = arguments
        bar_list_recyclerview.layoutManager = LinearLayoutManager(context)
        if (args!!.getInt("type") == 0) {
            bar_list_recyclerview.adapter = BarListAdapter(args!!.get("data") as Array<BarData>, barSelectedSubject)
        } else {
            bar_list_recyclerview.adapter = DrinkListAdapter(args!!.get("data") as Array<DrinkData>)
        }
        return inflater.inflate(R.layout.fragment_list, container, false)
    }

    fun displayDrinksList(bar: BarData) {
        val transaction = fragmentManager!!.beginTransaction()
        val drinksFragment = SlideUpListFragment()
        val args = Bundle()
        args.putInt("type", 1)
        args.putSerializable("data", bar.menu)
        drinksFragment.arguments = args
        transaction.replace(R.id.bar_list_recyclerview, SlideUpListFragment())
        transaction.addToBackStack(null)
    }
}
