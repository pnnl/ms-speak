/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

public class SDNRule {
	Integer ruleid;
	String dpid;
	Integer in_port;
	String dl_src;
	String dl_dst;
	Integer dl_type;
	String nw_src_prefix;
	Integer nw_src_maskbits;
	String nw_dst_prefix;
	Integer nw_dst_maskbits;
	Integer nw_proto;
	Integer tp_src;
	Integer tp_dst;
	Boolean wildcard_dpid;
	Boolean wildcard_in_port;
	Boolean wildcard_dl_src;
	Boolean wildcard_dl_dst;
	Boolean wildcard_dl_type;
	Boolean wildcard_nw_src;
	Boolean wildcard_nw_dst;
	Boolean wildcard_nw_proto;
	Boolean wildcard_tp_src;
	Boolean wildcard_tp_dst;
	Integer priority;
	String action;

	public String getPrintString() {
		return "ruleid="+ruleid+","+ "nw_src_prefix="+nw_src_prefix+ "," + "nw_dst_prefix="+nw_dst_prefix+ "," +"action="+action;
	}
	
	public Integer getRuleid() {
		return ruleid;
	}
	public void setRuleid(Integer ruleid) {
		this.ruleid = ruleid;
	}
	public String getDpid() {
		return dpid;
	}
	public void setDpid(String dpid) {
		this.dpid = dpid;
	}
	public Integer getIn_port() {
		return in_port;
	}
	public void setIn_port(Integer in_port) {
		this.in_port = in_port;
	}
	public String getDl_src() {
		return dl_src;
	}
	public void setDl_src(String dl_src) {
		this.dl_src = dl_src;
	}
	public String getDl_dst() {
		return dl_dst;
	}
	public void setDl_dst(String dl_dst) {
		this.dl_dst = dl_dst;
	}
	public Integer getDl_type() {
		return dl_type;
	}
	public void setDl_type(Integer dl_type) {
		this.dl_type = dl_type;
	}
	public String getNw_src_prefix() {
		return nw_src_prefix;
	}
	public void setNw_src_prefix(String nw_src_prefix) {
		this.nw_src_prefix = nw_src_prefix;
	}
	public Integer getNw_src_maskbits() {
		return nw_src_maskbits;
	}
	public void setNw_src_maskbits(Integer nw_src_maskbits) {
		this.nw_src_maskbits = nw_src_maskbits;
	}
	public String getNw_dst_prefix() {
		return nw_dst_prefix;
	}
	public void setNw_dst_prefix(String nw_dst_prefix) {
		this.nw_dst_prefix = nw_dst_prefix;
	}
	public Integer getNw_dst_maskbits() {
		return nw_dst_maskbits;
	}
	public void setNw_dst_maskbits(Integer nw_dst_maskbits) {
		this.nw_dst_maskbits = nw_dst_maskbits;
	}
	public Integer getNw_proto() {
		return nw_proto;
	}
	public void setNw_proto(Integer nw_proto) {
		this.nw_proto = nw_proto;
	}
	public Integer getTp_src() {
		return tp_src;
	}
	public void setTp_src(Integer tp_src) {
		this.tp_src = tp_src;
	}
	public Integer getTp_dst() {
		return tp_dst;
	}
	public void setTp_dst(Integer tp_dst) {
		this.tp_dst = tp_dst;
	}
	public Boolean getWildcard_dpid() {
		return wildcard_dpid;
	}
	public void setWildcard_dpid(Boolean wildcard_dpid) {
		this.wildcard_dpid = wildcard_dpid;
	}
	public Boolean getWildcard_in_port() {
		return wildcard_in_port;
	}
	public void setWildcard_in_port(Boolean wildcard_in_port) {
		this.wildcard_in_port = wildcard_in_port;
	}
	public Boolean getWildcard_dl_src() {
		return wildcard_dl_src;
	}
	public void setWildcard_dl_src(Boolean wildcard_dl_src) {
		this.wildcard_dl_src = wildcard_dl_src;
	}
	public Boolean getWildcard_dl_dst() {
		return wildcard_dl_dst;
	}
	public void setWildcard_dl_dst(Boolean wildcard_dl_dst) {
		this.wildcard_dl_dst = wildcard_dl_dst;
	}
	public Boolean getWildcard_dl_type() {
		return wildcard_dl_type;
	}
	public void setWildcard_dl_type(Boolean wildcard_dl_type) {
		this.wildcard_dl_type = wildcard_dl_type;
	}
	public Boolean getWildcard_nw_src() {
		return wildcard_nw_src;
	}
	public void setWildcard_nw_src(Boolean wildcard_nw_src) {
		this.wildcard_nw_src = wildcard_nw_src;
	}
	public Boolean getWildcard_nw_dst() {
		return wildcard_nw_dst;
	}
	public void setWildcard_nw_dst(Boolean wildcard_nw_dst) {
		this.wildcard_nw_dst = wildcard_nw_dst;
	}
	public Boolean getWildcard_nw_proto() {
		return wildcard_nw_proto;
	}
	public void setWildcard_nw_proto(Boolean wildcard_nw_proto) {
		this.wildcard_nw_proto = wildcard_nw_proto;
	}
	public Boolean getWildcard_tp_src() {
		return wildcard_tp_src;
	}
	public void setWildcard_tp_src(Boolean wildcard_tp_src) {
		this.wildcard_tp_src = wildcard_tp_src;
	}
	public Boolean getWildcard_tp_dst() {
		return wildcard_tp_dst;
	}
	public void setWildcard_tp_dst(Boolean wildcard_tp_dst) {
		this.wildcard_tp_dst = wildcard_tp_dst;
	}
	public Integer getPriority() {
		return priority;
	}
	public void setPriority(Integer priority) {
		this.priority = priority;
	}
	public String getAction() {
		return action;
	}
	public void setAction(String action) {
		this.action = action;
	}
}
