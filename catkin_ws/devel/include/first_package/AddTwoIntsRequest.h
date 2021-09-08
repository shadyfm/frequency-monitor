// Generated by gencpp from file first_package/AddTwoIntsRequest.msg
// DO NOT EDIT!


#ifndef FIRST_PACKAGE_MESSAGE_ADDTWOINTSREQUEST_H
#define FIRST_PACKAGE_MESSAGE_ADDTWOINTSREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace first_package
{
template <class ContainerAllocator>
struct AddTwoIntsRequest_
{
  typedef AddTwoIntsRequest_<ContainerAllocator> Type;

  AddTwoIntsRequest_()
    : a(0)
    , b(0)  {
    }
  AddTwoIntsRequest_(const ContainerAllocator& _alloc)
    : a(0)
    , b(0)  {
  (void)_alloc;
    }



   typedef int64_t _a_type;
  _a_type a;

   typedef int64_t _b_type;
  _b_type b;





  typedef boost::shared_ptr< ::first_package::AddTwoIntsRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::first_package::AddTwoIntsRequest_<ContainerAllocator> const> ConstPtr;

}; // struct AddTwoIntsRequest_

typedef ::first_package::AddTwoIntsRequest_<std::allocator<void> > AddTwoIntsRequest;

typedef boost::shared_ptr< ::first_package::AddTwoIntsRequest > AddTwoIntsRequestPtr;
typedef boost::shared_ptr< ::first_package::AddTwoIntsRequest const> AddTwoIntsRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::first_package::AddTwoIntsRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::first_package::AddTwoIntsRequest_<ContainerAllocator1> & lhs, const ::first_package::AddTwoIntsRequest_<ContainerAllocator2> & rhs)
{
  return lhs.a == rhs.a &&
    lhs.b == rhs.b;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::first_package::AddTwoIntsRequest_<ContainerAllocator1> & lhs, const ::first_package::AddTwoIntsRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace first_package

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::first_package::AddTwoIntsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::first_package::AddTwoIntsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::first_package::AddTwoIntsRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "36d09b846be0b371c5f190354dd3153e";
  }

  static const char* value(const ::first_package::AddTwoIntsRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x36d09b846be0b371ULL;
  static const uint64_t static_value2 = 0xc5f190354dd3153eULL;
};

template<class ContainerAllocator>
struct DataType< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "first_package/AddTwoIntsRequest";
  }

  static const char* value(const ::first_package::AddTwoIntsRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 a\n"
"int64 b\n"
;
  }

  static const char* value(const ::first_package::AddTwoIntsRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.a);
      stream.next(m.b);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AddTwoIntsRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::first_package::AddTwoIntsRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::first_package::AddTwoIntsRequest_<ContainerAllocator>& v)
  {
    s << indent << "a: ";
    Printer<int64_t>::stream(s, indent + "  ", v.a);
    s << indent << "b: ";
    Printer<int64_t>::stream(s, indent + "  ", v.b);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FIRST_PACKAGE_MESSAGE_ADDTWOINTSREQUEST_H
