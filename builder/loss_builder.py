# -*- coding:utf-8 -*-
# author: Xinge
# @file: loss_builder.py 

import torch
from utils.lovasz_losses import lovasz_softmax


def build(wce=True, lovasz=True, num_class=20, ignore_label=0):
    
    ####weighted loss function
    weights = torch.tensor([0.000000003909961577, 0.000000002624572561, 0.0000005611360536, 0.0000002701413325, 0.00000009464693947,
                        0.0000000558845635, 0.0000003391193883, 0.000000654810236, 0.000002521495751, 0.0000000006033565441,
                        0.000000008024802933, 0.0000000008488103755, 0.00000003767766337, 0.0000000009669924, 0.000000001877186965,
                        0.0000000004337601619, 0.00000001693416953, 0.000000001508196626, 0.00000004238356704, 0.0000002032001999]).cuda()
    loss_funs = torch.nn.CrossEntropyLoss(ignore_index=ignore_label,weight=weights)
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
