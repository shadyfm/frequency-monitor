// Generated by gencpp from file first_package/AddTwoInts.msg
// DO NOT EDIT!


#ifndef FIRST_PACKAGE_MESSAGE_ADDTWOINTS_H
#define FIRST_PACKAGE_MESSAGE_ADDTWOINTS_H

#include <ros/service_traits.h>


#include <first_package/AddTwoIntsRequest.h>
#include <first_package/AddTwoIntsResponse.h>


namespace first_package
{

struct AddTwoInts
{

typedef AddTwoIntsRequest Request;
typedef AddTwoIntsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddTwoInts
} // namespace first_package


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::first_package::AddTwoInts > {
  static const char* value()
  {
    return "6a2e34150c00229791cc89ff309fff21";
  }

  static const char* value(const ::first_package::AddTwoInts&) { return value(); }
};

template<>
struct DataType< ::first_package::AddTwoInts > {
  static const char* value()
  {
    return "first_package/AddTwoInts";
  }

  static const char* value(const ::first_package::AddTwoInts&) { return value(); }
};


// service_traits::MD5Sum< ::first_package::AddTwoIntsRequest> should match
// service_traits::MD5Sum< ::first_package::AddTwoInts >
template<>
struct MD5Sum< ::first_package::AddTwoIntsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::first_package::AddTwoInts >::value();
  }
  static const char* value(const ::first_package::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::first_package::AddTwoIntsRequest> should match
// service_traits::DataType< ::first_package::AddTwoInts >
template<>
struct DataType< ::first_package::AddTwoIntsRequest>
{
  static const char* value()
  {
    return DataType< ::first_package::AddTwoInts >::value();
  }
  static const char* value(const ::first_package::AddTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::first_package::AddTwoIntsResponse> should match
// service_traits::MD5Sum< ::first_package::AddTwoInts >
template<>
struct MD5Sum< ::first_package::AddTwoIntsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::first_package::AddTwoInts >::value();
  }
  static const char* value(const ::first_package::AddTwoIntsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::first_package::AddTwoIntsResponse> should match
// service_traits::DataType< ::first_package::AddTwoInts >
template<>
struct DataType< ::first_package::AddTwoIntsResponse>
{
  static const char* value()
  {
    return DataType< ::first_package::AddTwoInts >::value();
  }
  static const char* value(const ::first_package::AddTwoIntsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // FIRST_PACKAGE_MESSAGE_ADDTWOINTS_H
