from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NATGatewaysApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def datacenters_natgateways_delete(self, datacenter_id, nat_gateway_id, **kwargs):  # noqa: E501
        """Remove a NAT gateway  # noqa: E501

        Removes the specified NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_delete(datacenter_id, nat_gateway_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_delete_with_http_info(datacenter_id, nat_gateway_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_delete_with_http_info(self, datacenter_id, nat_gateway_id, **kwargs):  # noqa: E501
        """Remove a NAT gateway  # noqa: E501

        Removes the specified NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_delete_with_http_info(datacenter_id, nat_gateway_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_delete`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_find_by_nat_gateway_id(self, datacenter_id, nat_gateway_id, **kwargs):  # noqa: E501
        """Retrieve a NAT gateway  # noqa: E501

        Retrieves the attributes of a given NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_find_by_nat_gateway_id(datacenter_id, nat_gateway_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGateway
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_find_by_nat_gateway_id_with_http_info(datacenter_id, nat_gateway_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_find_by_nat_gateway_id_with_http_info(self, datacenter_id, nat_gateway_id, **kwargs):  # noqa: E501
        """Retrieve a NAT gateway  # noqa: E501

        Retrieves the attributes of a given NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_find_by_nat_gateway_id_with_http_info(datacenter_id, nat_gateway_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGateway, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_find_by_nat_gateway_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_find_by_nat_gateway_id`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_find_by_nat_gateway_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_find_by_nat_gateway_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_find_by_nat_gateway_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGateway'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_flowlogs_delete(self, datacenter_id, nat_gateway_id, flow_log_id, **kwargs):  # noqa: E501
        """Remove Flow Log from NAT Gateway  # noqa: E501

        This will remove a flow log from the NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_delete(datacenter_id, nat_gateway_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param flow_log_id: The unique ID of the flow log (required)
        :type flow_log_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_flowlogs_delete_with_http_info(datacenter_id, nat_gateway_id, flow_log_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_flowlogs_delete_with_http_info(self, datacenter_id, nat_gateway_id, flow_log_id, **kwargs):  # noqa: E501
        """Remove Flow Log from NAT Gateway  # noqa: E501

        This will remove a flow log from the NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_delete_with_http_info(datacenter_id, nat_gateway_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param flow_log_id: The unique ID of the flow log (required)
        :type flow_log_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'flow_log_id',
            'pretty',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_flowlogs_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_flowlogs_delete`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_flowlogs_delete`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_natgateways_flowlogs_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_flowlogs_find_by_flow_log_id(self, datacenter_id, nat_gateway_id, flow_log_id, **kwargs):  # noqa: E501
        """Retrieve a Flow Log of the NAT Gateway  # noqa: E501

        This will return a Flow Log of the NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_find_by_flow_log_id(datacenter_id, nat_gateway_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param flow_log_id: The unique ID of the flow log (required)
        :type flow_log_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_flowlogs_find_by_flow_log_id_with_http_info(datacenter_id, nat_gateway_id, flow_log_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_flowlogs_find_by_flow_log_id_with_http_info(self, datacenter_id, nat_gateway_id, flow_log_id, **kwargs):  # noqa: E501
        """Retrieve a Flow Log of the NAT Gateway  # noqa: E501

        This will return a Flow Log of the NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_find_by_flow_log_id_with_http_info(datacenter_id, nat_gateway_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param flow_log_id: The unique ID of the flow log (required)
        :type flow_log_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'flow_log_id',
            'pretty',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_flowlogs_find_by_flow_log_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_flowlogs_find_by_flow_log_id`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_flowlogs_find_by_flow_log_id`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_natgateways_flowlogs_find_by_flow_log_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_find_by_flow_log_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_find_by_flow_log_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_flowlogs_get(self, datacenter_id, nat_gateway_id, **kwargs):  # noqa: E501
        """List NAT Gateway Flow Logs  # noqa: E501

        You can retrieve a list of Flow Logs of the NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_get(datacenter_id, nat_gateway_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with limit for pagination)
        :type offset: int
        :param limit: the maximum number of elements to return (use together with offset for pagination)
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FlowLogs
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_flowlogs_get_with_http_info(datacenter_id, nat_gateway_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_flowlogs_get_with_http_info(self, datacenter_id, nat_gateway_id, **kwargs):  # noqa: E501
        """List NAT Gateway Flow Logs  # noqa: E501

        You can retrieve a list of Flow Logs of the NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_get_with_http_info(datacenter_id, nat_gateway_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with limit for pagination)
        :type offset: int
        :param limit: the maximum number of elements to return (use together with offset for pagination)
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FlowLogs, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'pretty',
            'depth',
            'offset',
            'limit'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_flowlogs_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_flowlogs_get`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_flowlogs_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_natgateways_flowlogs_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_natgateways_flowlogs_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_natgateways_flowlogs_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLogs'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_flowlogs_patch(self, datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, **kwargs):  # noqa: E501
        """Partially modify a Flow Log of the NAT Gateway  # noqa: E501

        You can use to partially update a Flow Log of a NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_patch(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param flow_log_id: The unique ID of the flow log (required)
        :type flow_log_id: str
        :param nat_gateway_flow_log_properties: Properties of a Flow Log to be updated (required)
        :type nat_gateway_flow_log_properties: FlowLogProperties
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_flowlogs_patch_with_http_info(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, **kwargs)  # noqa: E501

    def datacenters_natgateways_flowlogs_patch_with_http_info(self, datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, **kwargs):  # noqa: E501
        """Partially modify a Flow Log of the NAT Gateway  # noqa: E501

        You can use to partially update a Flow Log of a NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_patch_with_http_info(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param flow_log_id: The unique ID of the flow log (required)
        :type flow_log_id: str
        :param nat_gateway_flow_log_properties: Properties of a Flow Log to be updated (required)
        :type nat_gateway_flow_log_properties: FlowLogProperties
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'flow_log_id',
            'nat_gateway_flow_log_properties',
            'pretty',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_flowlogs_patch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_natgateways_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'nat_gateway_flow_log_properties' is set
        if self.api_client.client_side_validation and ('nat_gateway_flow_log_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_flow_log_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_flow_log_properties` when calling `datacenters_natgateways_flowlogs_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway_flow_log_properties' in local_var_params:
            body_params = local_var_params['nat_gateway_flow_log_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_flowlogs_post(self, datacenter_id, nat_gateway_id, nat_gateway_flow_log, **kwargs):  # noqa: E501
        """Add a NAT Gateways Flow Log  # noqa: E501

        This will add a new Flow Log to the NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_post(datacenter_id, nat_gateway_id, nat_gateway_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_flow_log: Flow Log to add on NAT Gateway (required)
        :type nat_gateway_flow_log: FlowLog
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_flowlogs_post_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_flow_log, **kwargs)  # noqa: E501

    def datacenters_natgateways_flowlogs_post_with_http_info(self, datacenter_id, nat_gateway_id, nat_gateway_flow_log, **kwargs):  # noqa: E501
        """Add a NAT Gateways Flow Log  # noqa: E501

        This will add a new Flow Log to the NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_post_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_flow_log: Flow Log to add on NAT Gateway (required)
        :type nat_gateway_flow_log: FlowLog
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'nat_gateway_flow_log',
            'pretty',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_flowlogs_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_flowlogs_post`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_flowlogs_post`")  # noqa: E501
        # verify the required parameter 'nat_gateway_flow_log' is set
        if self.api_client.client_side_validation and ('nat_gateway_flow_log' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_flow_log'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_flow_log` when calling `datacenters_natgateways_flowlogs_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway_flow_log' in local_var_params:
            body_params = local_var_params['nat_gateway_flow_log']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_flowlogs_put(self, datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, **kwargs):  # noqa: E501
        """Modify a Flow Log of the NAT Gateway  # noqa: E501

        You can use to update a Flow Log of the NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_put(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param flow_log_id: The unique ID of the flow log (required)
        :type flow_log_id: str
        :param nat_gateway_flow_log: Modified NAT Gateway Flow Log (required)
        :type nat_gateway_flow_log: FlowLogPut
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_flowlogs_put_with_http_info(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, **kwargs)  # noqa: E501

    def datacenters_natgateways_flowlogs_put_with_http_info(self, datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, **kwargs):  # noqa: E501
        """Modify a Flow Log of the NAT Gateway  # noqa: E501

        You can use to update a Flow Log of the NAT Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_flowlogs_put_with_http_info(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param flow_log_id: The unique ID of the flow log (required)
        :type flow_log_id: str
        :param nat_gateway_flow_log: Modified NAT Gateway Flow Log (required)
        :type nat_gateway_flow_log: FlowLogPut
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'flow_log_id',
            'nat_gateway_flow_log',
            'pretty',
            'depth'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_flowlogs_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_natgateways_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'nat_gateway_flow_log' is set
        if self.api_client.client_side_validation and ('nat_gateway_flow_log' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_flow_log'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_flow_log` when calling `datacenters_natgateways_flowlogs_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_flowlogs_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway_flow_log' in local_var_params:
            body_params = local_var_params['nat_gateway_flow_log']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_get(self, datacenter_id, **kwargs):  # noqa: E501
        """List NAT Gateways  # noqa: E501

        Retrieve a list of NAT Gateways within the datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_get(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGateways
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_get_with_http_info(datacenter_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_get_with_http_info(self, datacenter_id, **kwargs):  # noqa: E501
        """List NAT Gateways  # noqa: E501

        Retrieve a list of NAT Gateways within the datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_get_with_http_info(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGateways, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGateways'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_patch(self, datacenter_id, nat_gateway_id, nat_gateway_properties, **kwargs):  # noqa: E501
        """Partially update a NAT gateway  # noqa: E501

        Partially update the attributes of a given NAT gateway  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_patch(datacenter_id, nat_gateway_id, nat_gateway_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_properties: NAT gateway properties to be updated (required)
        :type nat_gateway_properties: NatGatewayProperties
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGateway
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_patch_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_properties, **kwargs)  # noqa: E501

    def datacenters_natgateways_patch_with_http_info(self, datacenter_id, nat_gateway_id, nat_gateway_properties, **kwargs):  # noqa: E501
        """Partially update a NAT gateway  # noqa: E501

        Partially update the attributes of a given NAT gateway  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_patch_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_properties: NAT gateway properties to be updated (required)
        :type nat_gateway_properties: NatGatewayProperties
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGateway, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'nat_gateway_properties',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_patch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_patch`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_patch`")  # noqa: E501
        # verify the required parameter 'nat_gateway_properties' is set
        if self.api_client.client_side_validation and ('nat_gateway_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_properties` when calling `datacenters_natgateways_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway_properties' in local_var_params:
            body_params = local_var_params['nat_gateway_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGateway'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_post(self, datacenter_id, nat_gateway, **kwargs):  # noqa: E501
        """Create a NAT Gateway  # noqa: E501

        Creates a NAT Gateway within the datacenter. User should be the contract owner or a admin or a user with createInternetAccess privilege  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_post(datacenter_id, nat_gateway, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway: NAT gateway to be created (required)
        :type nat_gateway: NatGateway
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGateway
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_post_with_http_info(datacenter_id, nat_gateway, **kwargs)  # noqa: E501

    def datacenters_natgateways_post_with_http_info(self, datacenter_id, nat_gateway, **kwargs):  # noqa: E501
        """Create a NAT Gateway  # noqa: E501

        Creates a NAT Gateway within the datacenter. User should be the contract owner or a admin or a user with createInternetAccess privilege  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_post_with_http_info(datacenter_id, nat_gateway, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway: NAT gateway to be created (required)
        :type nat_gateway: NatGateway
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGateway, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_post`")  # noqa: E501
        # verify the required parameter 'nat_gateway' is set
        if self.api_client.client_side_validation and ('nat_gateway' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway` when calling `datacenters_natgateways_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway' in local_var_params:
            body_params = local_var_params['nat_gateway']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGateway'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_put(self, datacenter_id, nat_gateway_id, nat_gateway, **kwargs):  # noqa: E501
        """Update a NAT gateway  # noqa: E501

        Update the attributes of a given NAT gateway  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_put(datacenter_id, nat_gateway_id, nat_gateway, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway: Modified NAT Gateway (required)
        :type nat_gateway: NatGatewayPut
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGateway
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_put_with_http_info(datacenter_id, nat_gateway_id, nat_gateway, **kwargs)  # noqa: E501

    def datacenters_natgateways_put_with_http_info(self, datacenter_id, nat_gateway_id, nat_gateway, **kwargs):  # noqa: E501
        """Update a NAT gateway  # noqa: E501

        Update the attributes of a given NAT gateway  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_put_with_http_info(datacenter_id, nat_gateway_id, nat_gateway, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway: Modified NAT Gateway (required)
        :type nat_gateway: NatGatewayPut
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGateway, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'nat_gateway',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_put`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_put`")  # noqa: E501
        # verify the required parameter 'nat_gateway' is set
        if self.api_client.client_side_validation and ('nat_gateway' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway` when calling `datacenters_natgateways_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway' in local_var_params:
            body_params = local_var_params['nat_gateway']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGateway'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_rules_delete(self, datacenter_id, nat_gateway_id, nat_gateway_rule_id, **kwargs):  # noqa: E501
        """Remove rule from NAT Gateway  # noqa: E501

        This will remove a rule from the NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_delete(datacenter_id, nat_gateway_id, nat_gateway_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule_id: The unique ID of the NAT gateway rule (required)
        :type nat_gateway_rule_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_rules_delete_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_rules_delete_with_http_info(self, datacenter_id, nat_gateway_id, nat_gateway_rule_id, **kwargs):  # noqa: E501
        """Remove rule from NAT Gateway  # noqa: E501

        This will remove a rule from the NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_delete_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule_id: The unique ID of the NAT gateway rule (required)
        :type nat_gateway_rule_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'nat_gateway_rule_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_rules_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_rules_delete`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_rules_delete`")  # noqa: E501
        # verify the required parameter 'nat_gateway_rule_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_rule_id` when calling `datacenters_natgateways_rules_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501
        if 'nat_gateway_rule_id' in local_var_params:
            path_params['natGatewayRuleId'] = local_var_params['nat_gateway_rule_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_rules_find_by_nat_gateway_rule_id(self, datacenter_id, nat_gateway_id, nat_gateway_rule_id, **kwargs):  # noqa: E501
        """Retrieve a NAT Gateway Rule  # noqa: E501

        Retrieves the attributes of a given NAT gateway rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_find_by_nat_gateway_rule_id(datacenter_id, nat_gateway_id, nat_gateway_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule_id: The unique ID of the NAT gateway rule (required)
        :type nat_gateway_rule_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGatewayRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_rules_find_by_nat_gateway_rule_id_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_rules_find_by_nat_gateway_rule_id_with_http_info(self, datacenter_id, nat_gateway_id, nat_gateway_rule_id, **kwargs):  # noqa: E501
        """Retrieve a NAT Gateway Rule  # noqa: E501

        Retrieves the attributes of a given NAT gateway rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_find_by_nat_gateway_rule_id_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule_id: The unique ID of the NAT gateway rule (required)
        :type nat_gateway_rule_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGatewayRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'nat_gateway_rule_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_rules_find_by_nat_gateway_rule_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_rules_find_by_nat_gateway_rule_id`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_rules_find_by_nat_gateway_rule_id`")  # noqa: E501
        # verify the required parameter 'nat_gateway_rule_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_rule_id` when calling `datacenters_natgateways_rules_find_by_nat_gateway_rule_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_find_by_nat_gateway_rule_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_find_by_nat_gateway_rule_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501
        if 'nat_gateway_rule_id' in local_var_params:
            path_params['natGatewayRuleId'] = local_var_params['nat_gateway_rule_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGatewayRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_rules_get(self, datacenter_id, nat_gateway_id, **kwargs):  # noqa: E501
        """List NAT Gateways Rules  # noqa: E501

        Retrieve a list of rules of a NAT Gateway within the datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_get(datacenter_id, nat_gateway_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGatewayRules
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_rules_get_with_http_info(datacenter_id, nat_gateway_id, **kwargs)  # noqa: E501

    def datacenters_natgateways_rules_get_with_http_info(self, datacenter_id, nat_gateway_id, **kwargs):  # noqa: E501
        """List NAT Gateways Rules  # noqa: E501

        Retrieve a list of rules of a NAT Gateway within the datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_get_with_http_info(datacenter_id, nat_gateway_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGatewayRules, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_rules_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_rules_get`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_rules_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGatewayRules'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_rules_patch(self, datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, **kwargs):  # noqa: E501
        """Partially modify a rule of the NAT gateway  # noqa: E501

        You can use to partially update a rule of a NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_patch(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule_id: The unique ID of the NAT gateway rule (required)
        :type nat_gateway_rule_id: str
        :param nat_gateway_rule_properties: Properties of a NAT gateway rule to be updated (required)
        :type nat_gateway_rule_properties: NatGatewayRuleProperties
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGatewayRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_rules_patch_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, **kwargs)  # noqa: E501

    def datacenters_natgateways_rules_patch_with_http_info(self, datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, **kwargs):  # noqa: E501
        """Partially modify a rule of the NAT gateway  # noqa: E501

        You can use to partially update a rule of a NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_patch_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule_id: The unique ID of the NAT gateway rule (required)
        :type nat_gateway_rule_id: str
        :param nat_gateway_rule_properties: Properties of a NAT gateway rule to be updated (required)
        :type nat_gateway_rule_properties: NatGatewayRuleProperties
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGatewayRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'nat_gateway_rule_id',
            'nat_gateway_rule_properties',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_rules_patch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_rules_patch`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_rules_patch`")  # noqa: E501
        # verify the required parameter 'nat_gateway_rule_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_rule_id` when calling `datacenters_natgateways_rules_patch`")  # noqa: E501
        # verify the required parameter 'nat_gateway_rule_properties' is set
        if self.api_client.client_side_validation and ('nat_gateway_rule_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_rule_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_rule_properties` when calling `datacenters_natgateways_rules_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501
        if 'nat_gateway_rule_id' in local_var_params:
            path_params['natGatewayRuleId'] = local_var_params['nat_gateway_rule_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway_rule_properties' in local_var_params:
            body_params = local_var_params['nat_gateway_rule_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGatewayRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_rules_post(self, datacenter_id, nat_gateway_id, nat_gateway_rule, **kwargs):  # noqa: E501
        """Create a NAT Gateway Rule  # noqa: E501

        Creates a rule within the NAT Gateway of a datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_post(datacenter_id, nat_gateway_id, nat_gateway_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule: NAT gateway rule to be created (required)
        :type nat_gateway_rule: NatGatewayRule
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGatewayRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_rules_post_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule, **kwargs)  # noqa: E501

    def datacenters_natgateways_rules_post_with_http_info(self, datacenter_id, nat_gateway_id, nat_gateway_rule, **kwargs):  # noqa: E501
        """Create a NAT Gateway Rule  # noqa: E501

        Creates a rule within the NAT Gateway of a datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_post_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule: NAT gateway rule to be created (required)
        :type nat_gateway_rule: NatGatewayRule
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGatewayRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'nat_gateway_rule',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_rules_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_rules_post`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_rules_post`")  # noqa: E501
        # verify the required parameter 'nat_gateway_rule' is set
        if self.api_client.client_side_validation and ('nat_gateway_rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_rule` when calling `datacenters_natgateways_rules_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway_rule' in local_var_params:
            body_params = local_var_params['nat_gateway_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGatewayRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def datacenters_natgateways_rules_put(self, datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, **kwargs):  # noqa: E501
        """Modify a rule of the NAT gateway  # noqa: E501

        You can use to update a rule of the NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_put(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule_id: The unique ID of the NAT gateway rule (required)
        :type nat_gateway_rule_id: str
        :param nat_gateway_rule: Modified NAT Gateway Rule (required)
        :type nat_gateway_rule: NatGatewayRulePut
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NatGatewayRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_natgateways_rules_put_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, **kwargs)  # noqa: E501

    def datacenters_natgateways_rules_put_with_http_info(self, datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, **kwargs):  # noqa: E501
        """Modify a rule of the NAT gateway  # noqa: E501

        You can use to update a rule of the NAT gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_natgateways_rules_put_with_http_info(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param nat_gateway_id: The unique ID of the NAT gateway (required)
        :type nat_gateway_id: str
        :param nat_gateway_rule_id: The unique ID of the NAT gateway rule (required)
        :type nat_gateway_rule_id: str
        :param nat_gateway_rule: Modified NAT Gateway Rule (required)
        :type nat_gateway_rule: NatGatewayRulePut
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NatGatewayRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'nat_gateway_id',
            'nat_gateway_rule_id',
            'nat_gateway_rule',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_natgateways_rules_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_natgateways_rules_put`")  # noqa: E501
        # verify the required parameter 'nat_gateway_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_id` when calling `datacenters_natgateways_rules_put`")  # noqa: E501
        # verify the required parameter 'nat_gateway_rule_id' is set
        if self.api_client.client_side_validation and ('nat_gateway_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_rule_id` when calling `datacenters_natgateways_rules_put`")  # noqa: E501
        # verify the required parameter 'nat_gateway_rule' is set
        if self.api_client.client_side_validation and ('nat_gateway_rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['nat_gateway_rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nat_gateway_rule` when calling `datacenters_natgateways_rules_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_natgateways_rules_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'nat_gateway_id' in local_var_params:
            path_params['natGatewayId'] = local_var_params['nat_gateway_id']  # noqa: E501
        if 'nat_gateway_rule_id' in local_var_params:
            path_params['natGatewayRuleId'] = local_var_params['nat_gateway_rule_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nat_gateway_rule' in local_var_params:
            body_params = local_var_params['nat_gateway_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NatGatewayRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
