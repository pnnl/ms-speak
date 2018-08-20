/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association
Copyright (C) 2014-2016, Cigital, Inc
*/
package com.essence.services.dtos;

/**
 * Created by BWintemberg on 12/9/2015.
 */
public class AnalyzerResultDTO {
    public AnalyzerResultDTO(Long id, Long runTime, String detectorType, String srcIPAddress, String dstIPAddress,
                             Integer numberOfPacketsForDoS, Long timeWindowInSeconds, Integer refRuleId) {
        this.id = id;
        this.runTime = runTime;
        this.detectorType = detectorType;
        this.srcIPAddress = srcIPAddress;
        this.dstIPAddress = dstIPAddress;
        this.numberOfPacketsForDoS = numberOfPacketsForDoS;
        this.timeWindowInSeconds = timeWindowInSeconds;
        this.refRuleId = refRuleId;
    }

    public AnalyzerResultDTO() {
    }

    private Long	   id;

    private	Long runTime;

    private String detectorType; // type of detection in categorization

    private String srcIPAddress; 	// of packet / message, can be "ANY"

    private String dstIPAddress; 	// of packet / message, can be "ANY"

    private Integer numberOfPacketsForDoS;	// how many packets within the specific period to be considered DoS

    private	Long timeWindowInSeconds;	// number of seconds for the detection time window

    private Integer refRuleId;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getRunTime() {
        return runTime;
    }

    public void setRunTime(Long runTime) {
        this.runTime = runTime;
    }

    public String getDetectorType() {
        return detectorType;
    }

    public void setDetectorType(String detectorType) {
        this.detectorType = detectorType;
    }

    public String getSrcIPAddress() {
        return srcIPAddress;
    }

    public void setSrcIPAddress(String srcIPAddress) {
        this.srcIPAddress = srcIPAddress;
    }

    public String getDstIPAddress() {
        return dstIPAddress;
    }

    public void setDstIPAddress(String dstIPAddress) {
        this.dstIPAddress = dstIPAddress;
    }

    public Integer getNumberOfPacketsForDoS() {
        return numberOfPacketsForDoS;
    }

    public void setNumberOfPacketsForDoS(Integer numberOfPacketsForDoS) {
        this.numberOfPacketsForDoS = numberOfPacketsForDoS;
    }

    public Long getTimeWindowInSeconds() {
        return timeWindowInSeconds;
    }

    public void setTimeWindowInSeconds(Long timeWindowInSeconds) {
        this.timeWindowInSeconds = timeWindowInSeconds;
    }

    public Integer getRefRuleId() {
        return refRuleId;
    }

    public void setRefRuleId(Integer refRuleId) {
        this.refRuleId = refRuleId;
    }
}
