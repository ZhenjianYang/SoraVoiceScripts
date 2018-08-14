from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4130   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '主编',                                 # 9
        '诺蒂亚',                               # 10
        '法露茨',                               # 11
        '莎莉亚',                               # 12
        '巴拉尔',                               # 13
        '科尼嘉',                               # 14
        '科蕾迪',                               # 15
        '彭瑟',                                 # 16
        '',                                     # 17
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH01023 ._CH',             # 01
        'ED6_DT07/CH01100 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01143 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH02070 ._CH',             # 06
        'ED6_DT07/CH01540 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH01023P._CP',             # 01
        'ED6_DT07/CH01100P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01143P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH02070P._CP',             # 06
        'ED6_DT07/CH01540P._CP',             # 07
    )

    DeclNpc(
        X                   = -54100,
        Z                   = 200,
        Y                   = 61000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -56570,
        Z                   = 0,
        Y                   = 64660,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -59030,
        Z                   = 100,
        Y                   = 59540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -56630,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 65800,
        Z                   = 100,
        Y                   = -3410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -56840,
        TriggerZ            = 0,
        TriggerY            = 3500,
        TriggerRange        = 400,
        ActorX              = -56630,
        ActorZ              = 1500,
        ActorY              = 5500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57530,
        TriggerZ            = 0,
        TriggerY            = 400,
        TriggerRange        = 800,
        ActorX              = 57290,
        ActorZ              = 900,
        ActorY              = 340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2480,
        TriggerZ            = -250,
        TriggerY            = -3810,
        TriggerRange        = 800,
        ActorX              = 2480,
        ActorZ              = 1100,
        ActorY              = -3810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_29E",          # 00, 0
        "Function_1_29F",          # 01, 1
        "Function_2_2AC",          # 02, 2
        "Function_3_429",          # 03, 3
        "Function_4_42E",          # 04, 4
        "Function_5_539",          # 05, 5
        "Function_6_653",          # 06, 6
        "Function_7_658",          # 07, 7
        "Function_8_7FF",          # 08, 8
        "Function_9_9DE",          # 09, 9
        "Function_10_AE0",         # 0A, 10
        "Function_11_C29",         # 0B, 11
        "Function_12_D72",         # 0C, 12
        "Function_13_D77",         # 0D, 13
        "Function_14_E3A",         # 0E, 14
        "Function_15_F81",         # 0F, 15
    )


    def Function_0_29E(): pass

    label("Function_0_29E")

    Return()

    # Function_0_29E end

    def Function_1_29F(): pass

    label("Function_1_29F")

    OP_B1("t4130_n")
    OP_82(0x82, 0x0)
    Return()

    # Function_1_29F end

    def Function_2_2AC(): pass

    label("Function_2_2AC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_413")

    label("loc_2D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EA")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_413")

    label("loc_2EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_413")

    label("loc_303")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_413")

    label("loc_31C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_413")

    label("loc_335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_413")

    label("loc_34E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_367")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_413")

    label("loc_367")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_413")

    label("loc_380")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_413")

    label("loc_399")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_413")

    label("loc_3B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CB")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_413")

    label("loc_3CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_413")

    label("loc_3E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FD")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_413")

    label("loc_3FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_413")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_413")

    label("loc_428")

    Return()

    # Function_2_2AC end

    def Function_3_429(): pass

    label("Function_3_429")

    Call(0, 4)
    Return()

    # Function_3_429 end

    def Function_4_42E(): pass

    label("Function_4_42E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_51A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4B2")

    ChrTalk(    #0
        0x14,
        (
            "这么说来，\x01",
            "昨天傍晚好像有过很大的声响……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x14,
        "……是怎么回事呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x14,
        (
            "总感觉这一带最近\x01",
            "不太安宁啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_517")

    label("loc_4B2")


    ChrTalk(    #3
        0x14,
        (
            "啊，欢迎光临。\x01",
            "要吃早餐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x14,
        (
            "我们这里的特色\x01",
            "是咖啡和咖喱饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x14,
        "都很值得推荐哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_517")

    Jump("loc_535")

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_524")
    Jump("loc_535")

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_52E")
    Jump("loc_535")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_535")

    label("loc_535")

    TalkEnd(0x14)
    Return()

    # Function_4_42E end

    def Function_5_539(): pass

    label("Function_5_539")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5A3")

    ChrTalk(    #6
        0xFE,
        (
            "那个人在各业界\x01",
            "都有广泛的人脉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "真担心利贝尔的产业\x01",
            "会因此失去凝聚力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_631")

    label("loc_5A3")


    ChrTalk(    #8
        0xFE,
        (
            "昨天在利贝尔通讯上看到那条消息，\x01",
            "真是让我大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "有名的大富豪霍尔登先生\x01",
            "似乎去世了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "原来他已经\x01",
            "那么大年纪了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_631")

    Jump("loc_64F")

    label("loc_634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_63E")
    Jump("loc_64F")

    label("loc_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_648")
    Jump("loc_64F")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_64F")

    label("loc_64F")

    TalkEnd(0xFE)
    Return()

    # Function_5_539 end

    def Function_6_653(): pass

    label("Function_6_653")

    Call(0, 7)
    Return()

    # Function_6_653 end

    def Function_7_658(): pass

    label("Function_7_658")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_665")
    Jump("loc_7FB")

    label("loc_665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_72B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6B1")

    ChrTalk(    #11
        0x16,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x16,
        (
            "想吃午餐的话，\x01",
            "请务必光临本餐馆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_6B1")


    ChrTalk(    #13
        0x16,
        (
            "欢迎光临。\x01",
            "这里是『阳光铃铛酒廊』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x16,
        (
            "午餐要不要试试\x01",
            "新出品的『劲霸浓鱼汤』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x16,
        "这可是本店名菜哦！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_728")

    Jump("loc_7FB")

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_735")
    Jump("loc_7FB")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_7FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_791")

    ChrTalk(    #16
        0x16,
        (
            "最近来王都观光的人\x01",
            "好像越来越多了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x16,
        "果然有活力还是好啊～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FB")

    label("loc_791")


    ChrTalk(    #18
        0x16,
        (
            "最近似乎经常看到\x01",
            "外国来的客人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x16,
        "呵呵，都是来观光的吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x16,
        "果然有活力还是最好啊～。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7FB")

    TalkEnd(0x16)
    Return()

    # Function_7_658 end

    def Function_8_7FF(): pass

    label("Function_8_7FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_80C")
    Jump("loc_9DA")

    label("loc_80C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_882")

    ChrTalk(    #21
        0xFE,
        (
            "刚才在格兰赛尔城前面\x01",
            "看到不少穿着\x01",
            "黑衣服的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "那是怎么回事呢……\x01",
            "感觉好像有点危险呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E3")

    label("loc_882")


    ChrTalk(    #23
        0xFE,
        (
            "刚才在格兰赛尔城前面\x01",
            "看到一些奇怪的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "怎么回事呢，\x01",
            "好像全都穿着黑色的衣服……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8E3")

    Jump("loc_9DA")

    label("loc_8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_8F0")
    Jump("loc_9DA")

    label("loc_8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_9DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_965")

    ChrTalk(    #25
        0xFE,
        (
            "难道大家都忘记\x01",
            "百日战役时的事了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "还是说，\x01",
            "把痛苦的事情忘掉比较好吗？\x02",
        )
    )

    Jump("loc_961")

    label("loc_961")

    CloseMessageWindow()
    Jump("loc_9DA")

    label("loc_965")


    ChrTalk(    #27
        0xFE,
        (
            "世间已经渐渐\x01",
            "忘掉了战争带来的灾祸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "但这个王都还曾经\x01",
            "收留了很多难民。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "难道大家都忘了吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9DA")

    TalkEnd(0xFE)
    Return()

    # Function_8_7FF end

    def Function_9_9DE(): pass

    label("Function_9_9DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A3D")

    ChrTalk(    #30
        0xFE,
        (
            "后面的编辑会议\x01",
            "就等奈尔回来再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "他大概下午就会回来了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABE")

    label("loc_A3D")


    ChrTalk(    #32
        0xFE,
        (
            "今天我和别人约好\x01",
            "一会儿见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "他可是得过菲利策奖的\x01",
            "有名的记者哦。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "哎呀，\x01",
            "真是好久没见面了呢。\x02",
        )
    )

    Jump("loc_ABA")

    label("loc_ABA")

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_ABE")

    Jump("loc_ADC")

    label("loc_AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_ACB")
    Jump("loc_ADC")

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_AD5")
    Jump("loc_ADC")

    label("loc_AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_ADC")

    label("loc_ADC")

    TalkEnd(0xFE)
    Return()

    # Function_9_9DE end

    def Function_10_AE0(): pass

    label("Function_10_AE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_C0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_B4B")

    ChrTalk(    #35
        0xFE,
        (
            "要写出好的报道，\x01",
            "光靠情报收集和分析可不行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "要经常保持新鲜的感觉才行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C07")

    label("loc_B4B")


    ChrTalk(    #37
        0xFE,
        "奈尔啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "那种东西，\x01",
            "没办法做报导啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "他实在是太好心了， \x01",
            "总是对别人的每个意见\x01",
            "和每个情报投入到无法自拔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "不过，\x01",
            "这种感觉应该也\x01",
            "是慢慢培养出来的。\x02",
        )
    )

    Jump("loc_C03")

    label("loc_C03")

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_C07")

    Jump("loc_C25")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_C14")
    Jump("loc_C25")

    label("loc_C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_C1E")
    Jump("loc_C25")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_C25")

    label("loc_C25")

    TalkEnd(0xFE)
    Return()

    # Function_10_AE0 end

    def Function_11_C29(): pass

    label("Function_11_C29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_CA3")

    ChrTalk(    #41
        0xFE,
        (
            "我、我是负责文化方面的，\x01",
            "所以不会卷入这样的争论……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "不过奈尔前辈\x01",
            "可是每次都够辛苦啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D50")

    label("loc_CA3")


    ChrTalk(    #43
        0xFE,
        (
            "昨天的编辑会议上\x01",
            "也是大吵大闹……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "奈尔前辈\x01",
            "总是找到很好的材料，\x01",
            "但是却常常无法刊载。\x02",
        )
    )

    Jump("loc_D11")

    label("loc_D11")

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "因为诺蒂亚前辈是那个样子，\x01",
            "主编又是个很严格的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_D50")

    Jump("loc_D6E")

    label("loc_D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_D5D")
    Jump("loc_D6E")

    label("loc_D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_D67")
    Jump("loc_D6E")

    label("loc_D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_D6E")

    label("loc_D6E")

    TalkEnd(0xFE)
    Return()

    # Function_11_C29 end

    def Function_12_D72(): pass

    label("Function_12_D72")

    Call(0, 13)
    Return()

    # Function_12_D72 end

    def Function_13_D77(): pass

    label("Function_13_D77")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_E1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_DD0")

    ChrTalk(    #46
        0x13,
        (
            "奈尔前辈，\x01",
            "还是没回来呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x13,
        "是不是又喝了一晚上的酒呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E18")

    label("loc_DD0")


    ChrTalk(    #48
        0x13,
        "欢迎光临利贝尔通讯社。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x13,
        (
            "这里一楼是接待，\x01",
            "二楼是编辑室。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_E18")

    Jump("loc_E36")

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_E25")
    Jump("loc_E36")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_E2F")
    Jump("loc_E36")

    label("loc_E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_E36")

    label("loc_E36")

    TalkEnd(0x13)
    Return()

    # Function_13_D77 end

    def Function_14_E3A(): pass

    label("Function_14_E3A")

    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE0")
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #50
        (
            "\x07\x05巴拉尔咖啡厅的特产料理！\x01",
            "『巨匠咖喱饭』　１０００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #51
        (
            "\x07\x05使用秘传的香辛料精心烹制的辣味咖喱，\x01",
            "请您走过路过不要错过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_F6B")

    label("loc_EE0")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #52
        (
            "\x07\x05巴拉尔咖啡厅的特产料理！\x01",
            "『完熟咖喱饭』　９００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #53
        (
            "\x07\x05使用秘传的香辛料精心烹制的辣味咖喱，\x01",
            "请您走过路过不要错过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F6B")

    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_E3A end

    def Function_15_F81(): pass

    label("Function_15_F81")

    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1026")
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #54
        (
            "\x07\x05～　菜单　～\x01",
            "　混合鸡尾酒　　　７５０米拉\x01",
            "　香草派　　　　　４５０米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "\x07\x05～　新品　～\x01",
            "　劲霸浓鱼汤　　　１０００米拉\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10BA")

    label("loc_1026")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #56
        (
            "\x07\x05～　菜单　～\x01",
            "　仿手工制派　　　４００米拉\x01",
            "　苦西红柿三明治　１４００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #57
        (
            "\x07\x05～　本店推荐　～\x01",
            "　热海汁　　　　　１２００米拉\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_10BA")

    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_F81 end

    SaveToFile()

Try(main)
