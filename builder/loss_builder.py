# -*- coding:utf-8 -*-
# author: Xinge
# @file: loss_builder.py 

import torch
from utils.lovasz_losses import lovasz_softmax


def build(wce=True, lovasz=True, num_class=20, ignore_label=0):
    
    
    ####add weights to loss function
    # weights = torch.tensor([0.000000003909961577, 0.000000002624572561, 0.0000005611360536, 0.0000002701413325, 0.00000009464693947,
    #                     0.0000000558845635, 0.0000003391193883, 0.000000654810236, 0.000002521495751, 0.0000000006033565441,
    #                     0.000000008024802933, 0.0000000008488103755, 0.00000003767766337, 0.0000000009669924, 0.000000001877186965,
    #                     0.0000000004337601619, 0.00000001693416953, 0.000000001508196626, 0.00000004238356704, 0.0000002032001999]).cuda()
    # loss_funs = torch.nn.CrossEntropyLoss(ignore_index=ignore_label,weight=weights)
    ############
    
    ####add weights to loss function(fixed)
    # weights = torch.tensor([0.00000006289911454, 0.00000008385747751, 0.0000455331937, 0.000009613997981, 0.000001660798512,
    #                     0.000001234849935, 0.000003959800109, 0.00001, 0.00001, 0.00000001008622461,
    #                     0.0000002089789913, 0.00000001580206061, 0.0000009835133655, 0.00000002071486459, 0.00000002804822106,
    #                     0.00000000647392053, 0.0000004055176352, 0.00000002381260187, 0.000000722841577, 0.000003110545683]).cuda()
    # loss_funs = torch.nn.CrossEntropyLoss(ignore_index=ignore_label,weight=weights)
    ############
    
    #### unweighted loss function
    # loss_funs = torch.nn.CrossEntropyLoss(ignore_index=ignore_label)
    #############3

    if wce and lovasz:
        return loss_funs, lovasz_softmax
    elif wce and not lovasz:
        return wce
    elif not wce and lovasz:
        return lovasz_softmax
    else:
        raise NotImplementedError
