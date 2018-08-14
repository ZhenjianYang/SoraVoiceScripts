from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '普利亚姆',                             # 9
        '爱玲',                                 # 10
        '列曼',                                 # 11
        '阿利瑟',                               # 12
        '温丝',                                 # 13
        '米优',                                 # 14
        '艾莉卡',                               # 15
        '丹',                                   # 16
        '拉赛尔博士',                           # 17
        '玛多克工房长',                         # 18
        '阿加特',                               # 19
        ' ',                                    # 20
        '有人着陆装置',                         # 21
        '有人着陆装置',                         # 22
        '有人着陆装置影子',                     # 23
        '有人着陆装置影子',                     # 24
        '目标用照相机',                         # 25
        '',                                     # 26
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT27/CH03970 ._CH',             # 02
        'ED6_DT27/CH03980 ._CH',             # 03
        'ED6_DT07/CH02020 ._CH',             # 04
        'ED6_DT07/CH02620 ._CH',             # 05
        'ED6_DT06/CH20141 ._CH',             # 06
        'ED6_DT06/CH20053 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01050 ._CH',             # 09
        'ED6_DT07/CH01130 ._CH',             # 0A
        'ED6_DT07/CH01470 ._CH',             # 0B
        'ED6_DT26/CH20751 ._CH',             # 0C
        'ED6_DT26/CH20752 ._CH',             # 0D
        'ED6_DT26/CH20758 ._CH',             # 0E
        'ED6_DT26/CH20759 ._CH',             # 0F
        'ED6_DT26/CH20698 ._CH',             # 10
        'ED6_DT26/CH20699 ._CH',             # 11
        'ED6_DT26/CH20753 ._CH',             # 12
        'ED6_DT26/CH20754 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT27/CH03970P._CP',             # 02
        'ED6_DT27/CH03980P._CP',             # 03
        'ED6_DT07/CH02020P._CP',             # 04
        'ED6_DT07/CH02620P._CP',             # 05
        'ED6_DT06/CH20141P._CP',             # 06
        'ED6_DT06/CH20053P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01050P._CP',             # 09
        'ED6_DT07/CH01130P._CP',             # 0A
        'ED6_DT07/CH01470P._CP',             # 0B
        'ED6_DT26/CH20751P._CP',             # 0C
        'ED6_DT26/CH20752P._CP',             # 0D
        'ED6_DT26/CH20758P._CP',             # 0E
        'ED6_DT26/CH20759P._CP',             # 0F
        'ED6_DT26/CH20698P._CP',             # 10
        'ED6_DT26/CH20699P._CP',             # 11
        'ED6_DT26/CH20753P._CP',             # 12
        'ED6_DT26/CH20754P._CP',             # 13
    )

    DeclNpc(
        X                   = -26340,
        Z                   = 8000,
        Y                   = 65489,
        Direction           = 74,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -18800,
        Z                   = 8000,
        Y                   = 64430,
        Direction           = 164,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -24430,
        Z                   = 8000,
        Y                   = 68160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -14900,
        Z                   = 8000,
        Y                   = 63190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16239,
        Z                   = 8000,
        Y                   = 63190,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -104390,
        Z                   = 0,
        Y                   = 8560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xE6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xE6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xE6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xE6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_36A",          # 00, 0
        "Function_1_3FA",          # 01, 1
        "Function_2_4BB",          # 02, 2
        "Function_3_4F3",          # 03, 3
        "Function_4_509",          # 04, 4
        "Function_5_5DC",          # 05, 5
        "Function_6_6C8",          # 06, 6
        "Function_7_770",          # 07, 7
        "Function_8_2147",         # 08, 8
        "Function_9_4ACA",         # 09, 9
        "Function_10_4B00",        # 0A, 10
        "Function_11_4B46",        # 0B, 11
        "Function_12_4C65",        # 0C, 12
        "Function_13_4CAD",        # 0D, 13
        "Function_14_4CF5",        # 0E, 14
        "Function_15_4D31",        # 0F, 15
        "Function_16_4D42",        # 10, 16
    )


    def Function_0_36A(): pass

    label("Function_0_36A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3A2")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -38800, 25000, 59000, 90)

    label("loc_3A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_3BE"),
        (105, "loc_3BE"),
        (SWITCH_DEFAULT, "loc_3D1"),
    )


    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3CE")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_3CE")

    Jump("loc_3D1")

    label("loc_3D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3F9")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_3F9")

    Return()

    # Function_0_36A end

    def Function_1_3FA(): pass

    label("Function_1_3FA")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFEF278, 0x230052)
    OP_6F(0x3, 0)
    OP_72(0x1003, 0x0)
    ExitThread()
    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x7530, 0x64, 0x0)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    OP_71(0x409, 0x0)
    ExitThread()
    OP_71(0x9, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0xA, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0xB, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0xC, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493")
    OP_10(0x9, 0x0)
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x8, 0x0)
    ExitThread()

    label("loc_493")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BA")
    OP_10(0x9, 0x0)
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x8, 0x0)
    ExitThread()

    label("loc_4BA")

    Return()

    # Function_1_3FA end

    def Function_2_4BB(): pass

    label("Function_2_4BB")

    OP_72(0x2005, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()

    label("loc_4C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F2")
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x28)
    OP_73(0x5)
    Jump("loc_4C7")

    label("loc_4F2")

    Return()

    # Function_2_4BB end

    def Function_3_4F3(): pass

    label("Function_3_4F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_508")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_3_4F3")

    label("loc_508")

    Return()

    # Function_3_4F3 end

    def Function_4_509(): pass

    label("Function_4_509")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_5D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_56C")

    ChrTalk(    #0
        0xFE,
        (
            "……哦，忘记了。\x01",
            "还得卖饮料呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "哥哥，\x01",
            "冰苏打水怎么样？\x02",
        )
    )

    Jump("loc_568")

    label("loc_568")

    CloseMessageWindow()
    Jump("loc_5D8")

    label("loc_56C")


    ChrTalk(    #2
        0xFE,
        (
            "久违的工房船\x01",
            "好像就要回来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "在那个异变之后，\x01",
            "工房船为了重建活动\x01",
            "似乎巡回了王国各地……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5D8")

    TalkEnd(0xFE)
    Return()

    # Function_4_509 end

    def Function_5_5DC(): pass

    label("Function_5_5DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_6C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_64E")

    ChrTalk(    #4
        0xFE,
        (
            "因为我慌忙藏起来了，\x01",
            "所以不太清楚后面的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "那、那些人到底\x01",
            "是什么来头啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C4")

    label("loc_64E")


    ChrTalk(    #6
        0xFE,
        (
            "我一直都在\x01",
            "这里经营花店……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "有一天，\x01",
            "突然有人从天而降！\x02",
        )
    )

    Jump("loc_69F")

    label("loc_69F")

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "我、我真是\x01",
            "吓了一大跳……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_6C4")

    TalkEnd(0xFE)
    Return()

    # Function_5_5DC end

    def Function_6_6C8(): pass

    label("Function_6_6C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_76C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_71E")

    ChrTalk(    #9
        0xFE,
        (
            "一会儿又得\x01",
            "马上出航了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "唔～接下来\x01",
            "会去哪里呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76C")

    label("loc_71E")


    ChrTalk(    #11
        0xFE,
        "呼，终于活过来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "最近实在太忙，\x01",
            "连喘口气的空闲都没有啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_76C")

    TalkEnd(0xFE)
    Return()

    # Function_6_6C8 end

    def Function_7_770(): pass

    label("Function_7_770")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-49000, 25140, 59860, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x106, 0x80)
    FadeToBright(2000, 0)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_7DC"),
        (105, "loc_85E"),
        (SWITCH_DEFAULT, "loc_8E7"),
    )


    label("loc_7DC")

    SetChrPos(0x106, -50970, 25000, 54170, 90)
    ClearChrFlags(0x106, 0x80)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3B)
    OP_73(0x3)
    Sleep(300)

    def lambda_80E():
        OP_8E(0xFE, 0xFFFF452A, 0x61A8, 0xD37C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_80E)
    Sleep(800)
    OP_6F(0x3, 59)
    OP_70(0x3, 0x0)
    WaitChrThread(0x106, 0x1)

    def lambda_841():
        OP_8E(0xFE, 0xFFFF4642, 0x625C, 0xE632, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_841)
    WaitChrThread(0x106, 0x1)
    Jump("loc_8E7")

    label("loc_85E")

    SetChrPos(0x106, -51070, 25000, 63810, 180)
    ClearChrFlags(0x106, 0x80)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3B)
    OP_73(0x3)
    Sleep(300)

    def lambda_890():
        OP_8E(0xFE, 0xFFFF3940, 0x61A8, 0xF032, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_890)
    WaitChrThread(0x106, 0x1)
    OP_6F(0x2, 59)
    OP_70(0x2, 0x0)

    def lambda_8BE():
        OP_8E(0xFE, 0xFFFF4642, 0x625C, 0xE632, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_8BE)
    WaitChrThread(0x106, 0x1)
    Sleep(300)
    OP_8C(0x106, 180, 400)
    Jump("loc_8E7")

    label("loc_8E7")

    Sleep(300)

    ChrTalk(    #13
        0x106,
        (
            "#552F#5P啧……\x01",
            "那些家伙跑哪儿去了……\x02\x03",

            "提妲和那个叫艾莉卡什么的\x01",
            "都没看到人影嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_51(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0xBB8)

    def lambda_9A9():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_9A9)

    def lambda_9B7():
        OP_6D(-41660, 25180, 59860, 2000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_9B7)
    WaitChrThread(0x20, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_11(0xA4, 0xB7, 0xFF, 0x9470, 0x249F0, 0x0)
    OP_6D(-46180, 25180, 59000, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    def lambda_A2B():
        OP_6D(-38510, 25000, 59800, 5000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_A2B)

    def lambda_A43():
        OP_6C(65000, 5000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A43)

    def lambda_A53():
        OP_6B(2650, 5000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_A53)

    def lambda_A63():
        OP_8F(0xFE, 0xFFFF60DC, 0x61A8, 0xE8EE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_A63)
    WaitChrThread(0x106, 0x1)
    Sleep(500)

    NpcTalk(    #14
        0x17,
        "穿工作服的男性",
        (
            "#1464F#5P哟……\x02\x03",

            "#1460F你就是阿加特吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #15
        0x106,
        (
            "#057F#6P（这家伙，\x01",
            "　不是普通的维修员……）\x02\x03",

            "………………………………\x02\x03",

            "#053F哦，是吗……\x01",
            "你就是丹吧。\x02\x03",

            "#051F我听过你的传闻。\x01",
            "据说你以前是游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x17,
        (
            "#1463F#5P啊啊，难道……\x01",
            "是卡西乌斯先生告诉你的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        (
            "#052F#6P不、不是……\x02\x03",

            "#050F……只是从提妲\x01",
            "和拉赛尔老爷子那儿\x01",
            "听说了一点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x17,
        (
            "#1464F#5P…………………………\x02\x03",

            "#1460F呵呵，倒也是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x106,
        (
            "#555F#6P（这么说来，\x01",
            "　这家伙好像是在10年前\x01",
            "　辞退了游击士的工作……）\x02\x03",

            "（刚好是和卡西乌斯大叔\x01",
            "　就任交替的时候啊……）\x02\x03",

            "#552F……………………………………\x02\x03",

            "（既然如此，\x01",
            "　应该不是太差劲的家伙………）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #20
        0x106,
        (
            "#053F#6P……你们正在\x01",
            "开发新兵器是吧。\x02\x03",

            "#050F听说提妲那小鬼也在帮忙，\x01",
            "是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x17,
        (
            "#1463F#5P嗯，是啊…………\x02\x03",

            "#1464F不过已经不是帮忙，\x01",
            "而是正式参加了。\x02\x03",

            "#1465F……提妲这两年\x01",
            "本事也大有长进呢。\x02\x03",

            "我能教的东西\x01",
            "也不多了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x106,
        "#552F#6P（啧，果然是这样吗……）\x02",
    )

    CloseMessageWindow()

    def lambda_ECF():
        OP_6D(-38220, 25000, 59930, 1200)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_ECF)

    def lambda_EE7():
        OP_8F(0xFE, 0xFFFF630C, 0x61A8, 0xE8EE, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_EE7)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x2)
    Sleep(500)

    ChrTalk(    #23
        0x106,
        (
            "#057F#6P……你们啊，\x01",
            "把自己女儿当成什么啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x17,
        "#1460F#5P…………嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x106,
        (
            "#053F#6P忙于工作很少回家，\x01",
            "这我还能理解。\x02\x03",

            "那家伙也很喜欢摆弄机械，\x01",
            "让她帮忙发明也没问题。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #26
        0x106,
        (
            "#054F#6P……但是啊，\x01",
            "开发兵器什么的不该让女儿来做吧！\x02\x03",

            "考虑一下常识啊，常识！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x17, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x17)
    Sleep(500)
    OP_1D(0x75)
    Sleep(500)

    ChrTalk(    #27
        0x17,
        "#1461F#5P呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        "#057F#6P笑什么……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 270, 400)
    Sleep(300)

    ChrTalk(    #29
        0x17,
        (
            "#1464F#11P阿加特，你……\x02\x03",

            "#1462F你信任\x01",
            "提妲吗？\x02",
        )
    )

    Jump("loc_110B")

    label("loc_110B")

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x106,
        (
            "#055F#6P……………………啊？\x02\x03",

            "#054F别转移话题啊！\x01",
            "你们把那家伙卷进来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x17,
        (
            "#1465F#11P阿加特，\x01",
            "你的事我从各处听说了不少。\x02\x03",

            "但是只有这件事\x01",
            "我想要亲自问你。\x02\x03",

            "#1464F你似乎因为各种机会，\x01",
            "和提妲一起\x01",
            "行动过很多次……\x02\x03",

            "是因为提妲不可靠\x01",
            "所以无法放下不管吗？\x01",
            "还是说只是顺其自然而已？\x02\x03",

            "#1462F…………你到底，\x01",
            "是做何打算的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x106,
        (
            "#055F#6P那、那种事我怎么知道。\x02\x03",

            "#552F只是………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFFFF)
    Sleep(500)

    ChrTalk(    #33
        0x106,
        (
            "#053F#6P……那家伙\x01",
            "也帮了我很多忙。\x02\x03",

            "一开始是\x01",
            "觉得放心不下，\x01",
            "只想保护她而已……\x02\x03",

            "#556F……怎么回事呢。\x01",
            "反倒是我受她照顾了。\x02",
        )
    )

    Jump("loc_139F")

    label("loc_139F")

    CloseMessageWindow()

    ChrTalk(    #34
        0x17,
        "#1463F#11P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x106,
        (
            "#051F#6P从这种意义上来说，\x01",
            "我是信任那家伙的。\x02\x03",

            "你们的女儿\x01",
            "其实是很了不起的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x17,
        "#1464F#11P原来如此啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #37
        0x106,
        (
            "#555F#6P（哼，本来还担心\x01",
            "　这是个不懂常识的家伙……）\x02\x03",

            "（看起来……\x01",
            "　好像不是那么回事啊。）\x02\x03",

            "#053F……………………………………\x02\x03",

            "#050F……喂，\x01",
            "提妲参加这种兵器开发\x01",
            "应该有什么理由吧。\x02\x03",

            "……跟我说说吧，丹。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x17)
    Sleep(500)

    ChrTalk(    #38
        0x17,
        (
            "#1464F#11P啊啊，这个嘛……\x02\x03",

            "#1465F……嗯，\x01",
            "还是告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15C0():
        OP_8E(0xFE, 0xFFFF5E0C, 0x61A8, 0xE678, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_15C0)
    Sleep(1000)
    Fade(1000)
    OP_6D(-41900, 25000, 60320, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(306000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0x17, 0x1)
    Sleep(300)

    ChrTalk(    #39
        0x17,
        (
            "#1462F#11P你知道『歼灭天使』玲\x01",
            "和『帕蒂尔·玛蒂尔』\x01",
            "的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x106,
        (
            "#052F#6P……啊、啊啊…………\x02\x03",

            "#551F是那个乱来的小丫头\x01",
            "和超巨大的人形兵器吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x17,
        (
            "#1464F#11P提妲呢，\x01",
            "一直把那个叫玲的女孩\x01",
            "当成自己的朋友。\x02\x03",

            "#1462F按常理来讲，\x01",
            "这种事是不可能的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x106,
        (
            "#552F#6P不……\x01",
            "…………我知道。\x02\x03",

            "那家伙虽然没有\x01",
            "特地提起过……\x02\x03",

            "#053F……但她总是不自然地\x01",
            "避开这个话题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x17,
        (
            "#1464F#11P……是吗，那就好说了。\x02\x03",

            "#1462F导力装甲计划，\x01",
            "本来是为了对抗结社惊人的技术、\x01",
            "军事力量而发起的。\x02\x03",

            "最终目标是要获得\x01",
            "足以对抗帕蒂尔·玛蒂尔的能力。\x02\x03",

            "#1464F而提妲亲自提出\x01",
            "希望参加这项计划。\x02\x03",

            "我和艾莉卡也反对过……\x02\x03",

            "但提妲说想做和玲相关的事，\x01",
            "而不听我们的劝阻。\x02\x03",

            "#1465F她说这是她力所能及\x01",
            "可以为玲所做的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x17)
    Sleep(500)

    ChrTalk(    #44
        0x17,
        (
            "#1465F#11P……其实，\x01",
            "提妲并不是想实际\x01",
            "对玲做些什么。\x02\x03",

            "只是，\x01",
            "参加导力装甲计划，\x01",
            "就能够继续挂念着玲的事。\x02\x03",

            "即使心情不能传达，即使不能见面，\x01",
            "两人还是相互联系着。\x02\x03",

            "#1464F虽然只是微小的联系……\x02\x03",

            "但这是那孩子\x01",
            "现在能做到的最大努力。\x02",
        )
    )

    Jump("loc_1A6B")

    label("loc_1A6B")

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        (
            "#552F#6P#40W………………………………\x02\x03",

            "……那家伙……………\x01",
            "为了这种事……………\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 19)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(    #46
        0x106,
        (
            "#551F#6P（……真傻…………）\x02\x03",

            "#556F（没想到不知不觉中，\x01",
            "  她竟背负着这种负担……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x17,
        (
            "#1464F#11P……提妲现在\x01",
            "正作为一名技师而努力着。\x02\x03",

            "这是艾莉卡的判断。\x02\x03",

            "#1460F既然她有如此的觉悟，\x01",
            "就不能再把她当小孩子来看待了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x106, 270, 400)
    Sleep(300)

    ChrTalk(    #48
        0x106,
        (
            "#053F#12P……丹，\x01",
            "再告诉我一件事。\x02\x03",

            "#051F那个导力装甲\x01",
            "在哪里？\x02",
        )
    )

    Jump("loc_1C9A")

    label("loc_1C9A")

    CloseMessageWindow()

    ChrTalk(    #49
        0x17,
        "#1465F#11P你要去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x106,
        (
            "#551F#12P嗯，\x01",
            "也无法置之不理吧。\x02\x03",

            "#556F要是放着那家伙不管，\x01",
            "她肯定又要乱来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x17,
        (
            "#1465F#11P……是吗。\x02\x03",

            "#1461F呵呵，\x01",
            "正如岳父所说的。\x02\x03",

            "你这个人啊，\x01",
            "还是相当有希望的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #52
        0x106,
        (
            "#055F#12P你，你说什么……？\x02\x03",

            "岳父……\x01",
            "是说拉赛尔老爷子吗？\x02",
        )
    )

    Jump("loc_1DFD")

    label("loc_1DFD")

    CloseMessageWindow()
    OP_8C(0x17, 90, 500)
    Sleep(500)

    ChrTalk(    #53
        0x17,
        "#1460F#5P这个给你吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x05从丹那里拿到了认证卡片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #55
        0x17,
        (
            "#1464F#5P在升降梯那里使用这个，\x01",
            "就可以去实验场所在的地下５层。\x02\x03",

            "提妲和艾莉卡\x01",
            "现在应该都在那里。\x02\x03",

            "#1465F……只不过，\x01",
            "要去的话最好有所觉悟。\x02\x03",

            "艾莉卡也很想\x01",
            "试探一下你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x106,
        (
            "#053F#12P哼……\x01",
            "那种事怎样都无所谓。\x02\x03",

            "#051F我只是想\x01",
            "陪着提妲做实验而已。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FA2():
        OP_6D(-43630, 25000, 60640, 2500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_1FA2)

    def lambda_1FBA():
        OP_8E(0xFE, 0xFFFF54C0, 0x61A8, 0xE95C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1FBA)
    WaitChrThread(0x106, 0x1)
    OP_62(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x106, 0x17, 400)
    Sleep(300)

    ChrTalk(    #57
        0x106,
        (
            "#052F#5P……丹，\x01",
            "你怎么样？\x02\x03",

            "不来参加实验吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x17,
        (
            "#1464F#6P不必担心。\x01",
            "我也会去参加实验的。\x02\x03",

            "#1465F……因为我也还没有\x01",
            "承认你呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x106,
        (
            "#551F#5P（说什么呢，\x01",
            "  什么承认的……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x106, 270, 400)
    Sleep(300)
    FadeToDark(2000, 0, -1)

    def lambda_2106():
        OP_6D(-47630, 25000, 60640, 3000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2106)

    def lambda_211E():
        OP_8E(0xFE, 0xFFFF44E4, 0x6270, 0xE95C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_211E)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_770 end

    def Function_8_2147(): pass

    label("Function_8_2147")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-27760, 8000, 59500, 0)
    OP_67(0, 9200, -10000, 0)
    OP_6B(3720, 0)
    OP_6C(298000, 0)
    OP_6E(862, 0)
    SetChrPos(0x107, 9040, -40, 56920, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SoundLoad(121)
    SoundLoad(124)
    SoundLoad(143)
    SoundLoad(276)
    SoundLoad(524)
    SoundLoad(275)
    SoundLoad(200)
    SoundLoad(209)
    SoundLoad(26)
    OP_AD(0x2400CD, 0x0, 0x0, 0x3E8)
    OP_22(0x79, 0x0, 0x64)

    def lambda_21ED():
        OP_6B(3620, 5000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_21ED)
    FadeToBright(2000, 0)
    OP_0D()
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #60
        "\x07\x05……看到了……\x02",
    )

    Jump("loc_2230")

    label("loc_2230")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 300, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #61
        (
            "\x07\x05还剩３２０……３１０……\x01",
            "……３００…………\x02",
        )
    )

    Jump("loc_227F")

    label("loc_227F")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_44(0x20, 0xFF)
    OP_6D(-2500, 4260, 56860, 0)
    OP_67(0, 11640, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(302000, 0)
    OP_6E(352, 0)
    SetChrPos(0x107, 1620, 3500, 56700, 270)
    Sleep(300)
    FadeToBright(0, 0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #62
        "\x07\x05…………有了……\x02",
    )

    Jump("loc_2329")

    label("loc_2329")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 300, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #63
        "\x07\x05操作开始。\x02",
    )

    Jump("loc_2357")

    label("loc_2357")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("声音")

    AnonymousTalk(    #64
        (
            "\x07\x05座标微调确认。\x01",
            "……推进器启动。\x02",
        )
    )

    Jump("loc_2391")

    label("loc_2391")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x114, 0x0, 0x46)
    Sleep(1000)

    def lambda_23AE():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_23AE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_AE(0x3E8)
    OP_23(0x79)
    Sleep(1500)
    OP_44(0x20, 0xFF)
    OP_6D(-22600, 8000, 59500, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(295000, 0)
    OP_6E(282, 0)

    def lambda_2417():
        OP_6D(-26600, 8000, 59500, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2417)

    def lambda_242F():
        OP_6C(315000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_242F)
    SetChrPos(0x107, -14640, 8000, 59000, 270)

    def lambda_2450():
        OP_8E(0xFE, 0xFFFF99F8, 0x1F40, 0xE678, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2450)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x113, 0x1, 0x1E)
    Sleep(200)
    OP_24(0x113, 0x28)
    Sleep(200)
    OP_24(0x113, 0x32)
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x46)
    OP_20(0xBB8)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x64)
    WaitChrThread(0x107, 0x1)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x107,
        (
            "#064F#0C咦……？\x02\x03",

            "嗯……什么声音？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2515():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2515)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x107, 0x2)
    OP_1D(0x56)

    def lambda_2538():
        OP_6D(-26000, 9000, 58940, 2000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2538)

    def lambda_2550():
        OP_67(0, 24980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2550)

    def lambda_2568():
        OP_6B(1700, 2000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_2568)

    def lambda_2578():
        OP_6E(490, 2000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2578)
    FadeToDark(2000, 0, -1)
    WaitChrThread(0x20, 0x0)
    Sleep(500)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_6D(-23000, 8500, 54280, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(180000, 0)
    OP_6E(278, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x20)
    ClearChrFlags(0x16, 0x1)
    SetChrFlags(0x16, 0x2)
    SetChrChipByIndex(0x16, 14)
    SetChrSubChip(0x16, 5)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 15)
    SetChrSubChip(0x17, 5)
    SetChrPos(0x107, -23000, 8000, 57300, 180)
    SetChrPos(0x16, -23880, 14120, 54340, 0)
    SetChrPos(0x17, -21300, 14200, 53800, 0)
    OP_A1(0x1C, 0x9)
    OP_72(0x409, 0x0)
    ExitThread()
    OP_72(0x9, 0x0)
    ExitThread()
    SetChrPos(0x1C, -23840, 14000, 54700, 0)
    OP_A1(0x1D, 0xA)
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0xA, 0x0)
    ExitThread()
    SetChrPos(0x1D, -21340, 14000, 54100, 0)
    LoadEffect(0x0, "map\\\\mp021_00.eff")
    LoadEffect(0x1, "map\\\\mp065_01.eff")

    def lambda_26D7():
        OP_6D(-23780, 8000, 54440, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_26D7)

    def lambda_26EF():
        OP_6C(225000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_26EF)
    PlayEffect(0x1, 0x2, 0x1C, 0, -200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x1D, 0, -200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)

    def lambda_2772():
        OP_8F(0xFE, 0xFFFFA2B8, 0x1FB7, 0xD444, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2772)

    def lambda_278D():
        OP_8F(0xFE, 0xFFFFA2E0, 0x1F40, 0xD5AC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_278D)
    Sleep(500)

    def lambda_27AD():
        OP_8F(0xFE, 0xFFFFACCC, 0x2008, 0xD228, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_27AD)

    def lambda_27C8():
        OP_8F(0xFE, 0xFFFFACA4, 0x1F40, 0xD354, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_27C8)
    OP_43(0x107, 0x3, 0x0, 0xE)
    Sleep(500)
    PlayEffect(0x0, 0x0, 0xFF, -23840, 8000, 54700, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x0, 0x1, 0xFF, -21340, 8000, 54100, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2875():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE290, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2875)
    WaitChrThread(0x107, 0x1)
    OP_43(0x107, 0x2, 0x0, 0xF)
    WaitChrThread(0x16, 0x1)
    OP_82(0x0, 0x2)
    OP_22(0xC8, 0x0, 0x46)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_A1(0x1E, 0xB)
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0xB, 0x0)
    ExitThread()
    SetChrPos(0x1E, -23840, 8100, 54700, 0)
    WaitChrThread(0x17, 0x1)
    OP_82(0x1, 0x2)
    OP_22(0xC8, 0x0, 0x46)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_A1(0x1F, 0xC)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_72(0xC, 0x0)
    ExitThread()
    SetChrPos(0x1F, -21340, 8100, 54100, 0)
    OP_23(0x113)
    OP_23(0xCC)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Fade(500)
    OP_22(0x1A, 0x0, 0x64)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x1)
    ClearChrFlags(0x16, 0x2)
    SetChrPos(0x16, -22920, 8000, 54840, 0)
    SetChrChipByIndex(0x16, 12)
    SetChrSubChip(0x16, 0)
    Sleep(600)
    Sleep(500)

    ChrTalk(    #66
        0x107,
        (
            "#065F#0C#3S咦咦～～～……！？#2S\x02\x03",

            "呃、呃，嗯…………？\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0x1A, 0x0, 0x64)
    ClearChrFlags(0x17, 0x20)
    SetChrFlags(0x17, 0x1)
    ClearChrFlags(0x17, 0x2)
    SetChrPos(0x17, -22560, 8000, 54020, 0)
    SetChrChipByIndex(0x17, 13)
    SetChrSubChip(0x17, 0)
    Sleep(800)

    NpcTalk(    #67
        0x16,
        "神秘的驾驶员",
        "#5C#5P嗡…………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #68
        0x17,
        "神秘的驾驶员",
        "#5C#5P嗡…………\x02",
    )

    CloseMessageWindow()

    def lambda_2A5C():
        OP_8E(0xFE, 0xFFFFA678, 0x1F40, 0xD96C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2A5C)
    Sleep(200)

    def lambda_2A7C():
        OP_8E(0xFE, 0xFFFFA970, 0x1F40, 0xD868, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2A7C)
    Sleep(1000)

    def lambda_2A9C():
        OP_6D(-23780, 8000, 54840, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2A9C)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2AC6():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE420, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2AC6)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)

    ChrTalk(    #69
        0x107,
        (
            "#065F#0C#12P哎，呃……\x02\x03",

            "#062F请、请问。\x01",
            "……您、您是哪位！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    def lambda_2B45():
        OP_8E(0xFE, 0xFFFFA628, 0x1F40, 0xDCF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2B45)
    Sleep(200)

    def lambda_2B65():
        OP_8E(0xFE, 0xFFFFA9AC, 0x1F40, 0xDB60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2B65)
    Sleep(800)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)

    NpcTalk(    #70
        0x16,
        "神秘的驾驶员",
        "#5C#5P嗡嗡…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #71
        0x107,
        "#065F#0C#12P啊、啊…………\x02",
    )

    CloseMessageWindow()

    def lambda_2BF4():
        OP_6D(-23780, 8000, 55240, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2BF4)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2C1E():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE5B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2C1E)
    WaitChrThread(0x107, 0x1)

    def lambda_2C3E():
        OP_6D(-23780, 8000, 55640, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2C3E)

    def lambda_2C56():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE740, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2C56)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x107, 0x1)
    Sleep(1000)
    OP_20(0x7D0)
    Sleep(500)

    NpcTalk(    #72
        0x17,
        "神秘的驾驶员",
        (
            "#5C#5P………………哈哈哈。\x02\x03",

            "#5C提妲，好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x107,
        "#064F#0C#12P咦…………？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #74
        0x16,
        "神秘的驾驶员",
        "#5C#5P……哎呀，这孩子真是的。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0x16,
        "神秘的驾驶员",
        "#5C#5P连我们的声音都忘了？\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x16, 16)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x17, 17)
    SetChrSubChip(0x17, 0)
    OP_6B(2700, 0)
    OP_67(0, 5580, -10000, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #76
        0x107,
        (
            "#064F#0C#12P爸、爸…………\x02\x03",

            "#061F#3S爸爸！　妈妈！！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xD)
    Sleep(1000)

    ChrTalk(    #77
        0x16,
        (
            "#1976F#5P呵呵……\x01",
            "好久不见呢，提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x17,
        (
            "#1625F#5P抱歉，\x01",
            "本打算给你个惊喜的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x107,
        (
            "#562F#12P真、真是的！\x01",
            "吓我一跳啦！\x02\x03",

            "居然突然从天上飞来。\x02\x03",

            "而、而且还戴着\x01",
            "这种防风眼镜……\x02\x03",

            "#560F……你们两个要是回来，\x01",
            "怎么不事先联络一下嘛！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #80
        0x16,
        "#1972F#5P…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x107,
        (
            "#064F#12P……妈妈？\x02\x03",

            "嗯，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x16,
        "#1972F#5P提妲……\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0x16)
    Sleep(500)
    SetChrFlags(0x16, 0x40)

    def lambda_2FF5():
        OP_8E(0xFE, 0xFFFFA628, 0x1F40, 0xE5B0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2FF5)

    def lambda_3010():
        OP_6D(-24020, 8000, 58480, 3000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_3010)

    def lambda_3028():
        OP_67(0, 5580, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3028)

    def lambda_3040():
        OP_6C(235000, 3000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_3040)

    def lambda_3050():
        OP_6B(2640, 3000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_3050)
    WaitChrThread(0x16, 0x1)
    Fade(100)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 18)
    SetChrSubChip(0x107, 0)
    OP_0D()
    OP_43(0x107, 0x3, 0x0, 0x10)
    Sleep(300)
    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    Sleep(1000)

    ChrTalk(    #83
        0x16,
        (
            "#1981F#5P……啊啊，好可爱！\x02\x03",

            "这孩子果然好可爱！！\x02\x03",

            "亲～～～～……！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3106():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3106)
    Sleep(1000)

    ChrTalk(    #84
        0x107,
        (
            "#562F#12P妈、妈妈……\x01",
            "……有点难过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x16,
        (
            "#1981F#5P丹，\x01",
            "生下她真是好啊。\x02\x03",

            "我现在好幸福哦……！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x17,
        (
            "#1621F#5P看起来也是。\x02\x03",

            "#1620F那么，\x01",
            "也让我打个招呼吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x16,
        (
            "#1974F#5P是、是啊。\x02\x03",

            "#1976F确实你也有\x01",
            "这个权利呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_59()
    OP_44(0x107, 0xFF)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    ClearChrFlags(0x16, 0x8)
    SetChrPos(0x16, -23000, 8000, 58600, 0)
    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    Sleep(800)

    def lambda_3270():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE2F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3270)
    WaitChrThread(0x16, 0x1)

    def lambda_3290():

        label("loc_3290")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_3290")

    QueueWorkItem2(0x16, 2, lambda_3290)

    def lambda_32A1():
        OP_8F(0xFE, 0xFFFFA178, 0x1F40, 0xE290, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_32A1)

    def lambda_32BC():
        OP_6D(-24860, 8000, 56540, 1500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_32BC)

    def lambda_32D4():
        OP_67(0, 5580, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_32D4)

    def lambda_32EC():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_32EC)

    def lambda_32FC():
        OP_6B(2740, 1500)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_32FC)

    def lambda_330C():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE150, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_330C)
    WaitChrThread(0x17, 0x1)
    OP_44(0x16, 0x2)
    Sleep(300)

    ChrTalk(    #88
        0x17,
        (
            "#1625F#5P提妲。\x02\x03",

            "#1621F……我回来了。\x01",
            "你长得这么大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x107,
        (
            "#560F#12P……嗯。\x02\x03",

            "#061F欢迎你们回来，\x01",
            "爸爸，妈妈。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #90
        0x16,
        (
            "#1981F#5P唉……\x01",
            "果然好可爱啊～！！\x02\x03",

            "再来一个～……㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_342A():
        OP_8E(0xFE, 0xFFFFA308, 0x1F40, 0xE420, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_342A)
    WaitChrThread(0x16, 0x1)
    TurnDirection(0x107, 0x16, 500)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #91
        0x107,
        (
            "#562F#6P真、真是的。\x01",
            "妈妈啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 400)
    Sleep(300)

    ChrTalk(    #92
        0x17,
        (
            "#1625F#5P艾莉卡，\x01",
            "要抱也等换了衣服再说吧。\x02\x03",

            "这个工作服里\x01",
            "可是装载了\x01",
            "各种各样的传感器呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x16,
        (
            "#1974F#5P啊、啊啊……\x01",
            "说得也是呢。\x02\x03",

            "#1977F那么………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_355A():
        OP_8F(0xFE, 0xFFFFA178, 0x1F40, 0xE290, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_355A)
    WaitChrThread(0x16, 0x1)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x16, 12)
    SetChrSubChip(0x16, 0)
    OP_0D()
    OP_8C(0x16, 100, 400)
    Sleep(300)

    ChrTalk(    #94
        0x16,
        (
            "#1977F#11P……就先把事情\x01",
            "解决掉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_35E7():

        label("loc_35E7")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_35E7")

    QueueWorkItem2(0x107, 2, lambda_35E7)

    def lambda_35F8():

        label("loc_35F8")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_35F8")

    QueueWorkItem2(0x17, 2, lambda_35F8)

    def lambda_3609():
        OP_8E(0xFE, 0xFFFFAF24, 0x1F40, 0xE290, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3609)

    def lambda_3624():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xDF0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3624)
    WaitChrThread(0x16, 0x1)
    OP_44(0x107, 0x2)

    def lambda_3648():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3648)
    OP_44(0x17, 0x2)

    ChrTalk(    #95
        0x16,
        (
            "#1978F#5P快说………\x01",
            "那个红毛小子在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x107,
        (
            "#064F#11P嗯……？？\x02\x03",

            "红毛，\x01",
            "是说阿加特大哥哥？\x02",
        )
    )

    Jump("loc_36D3")

    label("loc_36D3")

    CloseMessageWindow()

    ChrTalk(    #97
        0x16,
        (
            "#1971F#5P对，就是那个。\x02\x03",

            "既然回到利贝尔，\x01",
            "就要打个招呼才行呢～。\x02\x03",

            "#1985F……对敌模式开启……\x01",
            "………对象，红毛９８％。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x16, 0x3, 0x0, 0x9)
    Sleep(1500)

    ChrTalk(    #98
        0x107,
        (
            "#560F#11P阿加特大哥哥的话\x01",
            "应该还在柏斯……\x02\x03",

            "咦，妈妈？\x01",
            "为什么突然这样？？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x16,
        (
            "#1977F#5P啧…………\x01",
            "原来不在蔡斯啊。\x02\x03",

            "#1982F话说回来，\x01",
            "要是在的话才是大问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x17,
        (
            "#1624F#11P好了好了艾莉卡。\x02\x03",

            "#1620F下个月\x01",
            "我们俩一起去吧。\x02\x03",

            "我也想\x01",
            "见他一面啊。\x02",
        )
    )

    Jump("loc_38A1")

    label("loc_38A1")

    CloseMessageWindow()

    ChrTalk(    #101
        0x16,
        "#1977F#5P……是啊…………\x02",
    )

    CloseMessageWindow()
    Sleep(1200)
    OP_44(0x16, 0xFF)
    OP_8C(0x16, 100, 500)
    Fade(300)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x16, 16)
    SetChrSubChip(0x16, 0)
    Sleep(800)

    ChrTalk(    #102
        0x16,
        (
            "#1977F#5P政变骚动加上『辉之环』事件。\x01",
            "利贝尔也真是麻烦不断啊。\x02\x03",

            "这段时间，\x01",
            "提妲似乎受到他相当多的照顾……\x02\x03",

            "#1985F呼呼呼…………\x01",
            "可要好好道谢才是啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x107,
        (
            "#061F#11P嘿嘿，那下次介绍给你们。\x02\x03",

            "阿加特大哥哥的家，\x01",
            "虽然小但是很温暖，\x01",
            "是个非常好的地方哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_3A4A():
        OP_8C(0xFE, 290, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3A4A)

    def lambda_3A58():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3A58)
    WaitChrThread(0x17, 0x2)
    Sleep(300)

    ChrTalk(    #104
        0x17,
        "#1623F#5P咦……\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x16)
    OP_63(0x17)
    Sleep(500)

    ChrTalk(    #105
        0x16,
        "#1980F#6P咯咯……！！（磨牙）\x02",
    )

    OP_7C(0x0, 0x190, 0xFA0, 0x12C)
    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 500)
    Sleep(300)

    ChrTalk(    #106
        0x17,
        (
            "#1621F#11P哈哈哈，\x01",
            "冷静一下，冷静一下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x107, 400)
    Sleep(300)

    ChrTalk(    #107
        0x17,
        (
            "#1625F#5P提妲也是，\x01",
            "不要随便刺激她啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x107,
        "#064F#11P咦…………？？？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x16, 100, 500)

    def lambda_3BA7():
        OP_8E(0xFE, 0xFFFFB6F4, 0x1F40, 0xE290, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3BA7)
    WaitChrThread(0x16, 0x1)

    ChrTalk(    #109
        0x16,
        (
            "#1980F#11P阿加特大哥哥……\x01",
            "阿加特大哥哥………！？\x02\x03",

            "…………可、可恶……！\x01",
            "……居然敢对我的提妲！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C3D():
        OP_8E(0xFE, 0xFFFFC2AC, 0x1F40, 0xE290, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3C3D)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x107, 190, 500)
    Sleep(600)
    OP_8C(0x107, 100, 500)
    Sleep(600)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(700)
    OP_22(0x6D, 0x0, 0x64)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -35780, 10000, 58300, 270)

    def lambda_3CAC():
        OP_8E(0xFE, 0xFFFF9174, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3CAC)
    WaitChrThread(0x18, 0x1)
    OP_62(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #110
        0x18,
        "#103F#11P怎、怎么了，这是。\x02",
    )

    CloseMessageWindow()

    def lambda_3D10():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3D10)
    Sleep(100)

    def lambda_3D23():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3D23)
    WaitChrThread(0x17, 0x2)
    Sleep(300)

    ChrTalk(    #111
        0x107,
        (
            "#560F#6P啊，爷爷。\x01",
            "那个…………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D67():
        OP_6D(-25380, 8000, 57540, 2000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_3D67)

    def lambda_3D7F():
        OP_6C(240000, 2000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3D7F)

    def lambda_3D8F():
        OP_8E(0xFE, 0xFFFF9D2C, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3D8F)
    Sleep(1500)

    def lambda_3DAF():
        OP_8F(0xFE, 0xFFFFA498, 0x1F40, 0xE164, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3DAF)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x17, 0x1)
    Sleep(500)

    ChrTalk(    #112
        0x17,
        (
            "#1624F#6P岳父，\x01",
            "久疏问候了。\x02\x03",

            "#1625F回国时也没有联络，\x01",
            "真是对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x18,
        (
            "#101F#11P哎呀，丹。\x01",
            "这些都无所谓啦。\x02\x03",

            "#102F话说回来\x01",
            "那个装置是什么……？\x02\x03",

            "看起来像是\x01",
            "装备了推进器的交通工具……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x16, -13600, 8000, 56240, 270)

    NpcTalk(    #114
        0x16,
        "女性的声音",
        "#2P是我开发的载人着陆装置。\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3F1A():

        label("loc_3F1A")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_3F1A")

    QueueWorkItem2(0x107, 2, lambda_3F1A)
    Sleep(100)

    def lambda_3F30():

        label("loc_3F30")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_3F30")

    QueueWorkItem2(0x17, 2, lambda_3F30)
    Sleep(300)
    SetChrPos(0x16, -13600, 8000, 58300, 270)

    def lambda_3F57():
        OP_6D(-25980, 8000, 57400, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_3F57)

    def lambda_3F6F():
        OP_67(0, 4880, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3F6F)

    def lambda_3F87():
        OP_6B(2700, 6000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_3F87)

    def lambda_3F97():
        OP_8E(0xFE, 0xFFFFAA10, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3F97)
    Sleep(1000)

    def lambda_3FB7():
        OP_8F(0xFE, 0xFFFFA308, 0x1F40, 0xE9FC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3FB7)

    def lambda_3FD2():
        OP_8F(0xFE, 0xFFFFA308, 0x1F40, 0xDE94, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3FD2)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x16, 150, 400)
    Sleep(300)

    ChrTalk(    #115
        0x16,
        (
            "#1978F#6P在没有导力技术的边境，\x01",
            "别说飞艇的停机坪了，\x01",
            "经常连空地也找不到一块。\x02\x03",

            "即使出动我们的飞艇，\x01",
            "也没办法着陆吧？\x02\x03",

            "……所以就使用了这个。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x16, 285, 400)

    def lambda_40AC():
        OP_8E(0xFE, 0xFFFFA4FC, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_40AC)
    WaitChrThread(0x16, 0x1)
    OP_44(0x107, 0x2)
    OP_44(0x17, 0x2)
    OP_8C(0x107, 195, 500)
    Sleep(300)

    ChrTalk(    #116
        0x16,
        (
            "#1976F#6P呼呼，好久不见呢。\x01",
            "阿尔巴特·拉赛尔。\x02\x03",

            "看来你还活着，\x01",
            "真是太好了。\x02\x03",

            "……真是不巧，\x01",
            "这次比赛似乎是我赢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x18,
        (
            "#102F#11P哼，\x01",
            "又做出这种小家子气的东西。\x02\x03",

            "艾莉卡，\x01",
            "你以为这种程度的发明\x01",
            "就能赢我了吗！？\x02\x03",

            "#104F这种玩意，\x01",
            "有效运转时间最多只有５分钟而已。\x02\x03",

            "#101F根本不值一提。\x01",
            "不可能实用化的～\x02",
        )
    )

    Jump("loc_4244")

    label("loc_4244")

    CloseMessageWindow()

    ChrTalk(    #118
        0x16,
        (
            "#1971F#6P哎呀～真可惜。\x02\x03",

            "我今天就是用这个\x01",
            "从卡尔瓦德国境附近\x01",
            "飞到这里来的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x18,
        "#102F#11P你、你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x16,
        (
            "#1978F#6P呼呼呼……\x01",
            "这个装置的飞行能力\x01",
            "确实有限。\x02\x03",

            "#1976F……但是。\x01",
            "但是啊，阿尔巴特·拉赛尔。\x02\x03",

            "用飞艇上的导力式弹射器射出的话，\x01",
            "就能够飞行约１２０塞尔矩。\x02\x03",

            "#1984F通过这次的导力回路改良\x01",
            "得到了３８２．２秒运转时间的最高记录！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0x18,
        (
            "#103F#11P１２０塞尔矩，\x01",
            "３８２．２秒……你说什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x16,
        (
            "#1971F#6P哦～呵呵呵！\x01",
            "看来你到底还是吃惊了吧。\x02\x03",

            "对老人来说，\x01",
            "刺激是不是太强了点～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x18,
        (
            "#102F#11P哼！！　你说什么呢！！\x02\x03",

            "跟我开发的卡佩尔相比\x01",
            "这种东西不过是骗小孩的玩具罢了。\x02\x03",

            "#101F哇哈哈～\x01",
            "这种东西对我来说，\x01",
            "一边睡午觉一边都能做出来啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x16,
        (
            "#1980F#6P你、你说什么……！\x01",
            "这个臭老头……！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_459F():
        OP_8E(0xFE, 0xFFFFA2A4, 0x1F40, 0xE3BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_459F)

    def lambda_45BA():
        OP_8E(0xFE, 0xFFFF9F84, 0x1F40, 0xE3BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_45BA)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)
    OP_43(0x18, 0x3, 0x0, 0xA)
    Sleep(300)

    ChrTalk(    #125
        0x16,
        "#1980F#3P唔哦……！\x02",
    )


    ChrTalk(    #126
        0x18,
        "#102F#2P哦哦哦……！\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #127
        0x107,
        (
            "#562F#12P啊啊，真是的……\x01",
            "果然又开始了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_467B():
        OP_8E(0xFE, 0xFFFFA1DC, 0x1F40, 0xE7CC, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_467B)
    WaitChrThread(0x107, 0x1)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 190, 500)
    Sleep(500)

    ChrTalk(    #128
        0x107,
        (
            "#62F#12P妈妈……\x01",
            "爷爷……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #129
        0x16,
        (
            "#1979F#6P我看过资料了，\x01",
            "阿尔巴特·拉赛尔……\x02\x03",

            "把提妲置于\x01",
            "如此危险的境地\x01",
            "居然还好意思说……\x02\x03",

            "#1980F而且还让她\x01",
            "被臭男人粘上……！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x18,
        (
            "#102F#11P你、你说什么……\x02\x03",

            "至今为止，\x01",
            "在大陆上到处乱跑\x01",
            "弃她于不顾的不就是你吗……\x02\x03",

            "#105F我可没道理\x01",
            "听你教训……！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x18, 0xFF)
    OP_44(0x16, 0xFF)
    OP_A3(0x0)
    OP_43(0x18, 0x3, 0x0, 0xB)
    Sleep(3000)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #131
        0x107,
        (
            "#065F#12P爸、爸爸。\x01",
            "快想想办法啊～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x17,
        (
            "#1621F#5P哈哈哈，没关系啦。\x02\x03",

            "他们两个是因为好久不见\x01",
            "而感到害羞而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        (
            "#63F#12P但、但是在这种地方\x01",
            "吵起架来，\x01",
            "会妨碍通行的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x17,
        (
            "#1625F#5P嗯～也是啊。\x01",
            "再说着陆装置\x01",
            "也得收好才行……\x02\x03",

            "只好先把这两人\x01",
            "带回家了。\x02\x03",

            "#1621F提妲，帮我个忙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x107,
        "#067F#12P嗯，明白！\x02",
    )

    CloseMessageWindow()
    OP_43(0x107, 0x3, 0x0, 0xC)
    OP_43(0x17, 0x3, 0x0, 0xD)
    WaitChrThread(0x107, 0x3)
    WaitChrThread(0x17, 0x3)
    OP_A2(0x0)
    WaitChrThread(0x18, 0x3)
    OP_43(0x18, 0x3, 0x0, 0xA)
    Sleep(1000)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x16, 0x20)

    def lambda_49E3():

        label("loc_49E3")

        TurnDirection(0xFE, 0x16, 800)
        OP_48()
        Jump("loc_49E3")

    QueueWorkItem2(0x17, 2, lambda_49E3)

    def lambda_49F4():
        OP_8F(0xFE, 0xFFFFA754, 0x1F40, 0xE678, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_49F4)
    WaitChrThread(0x16, 0x1)

    def lambda_4A14():
        OP_8F(0xFE, 0xFFFFAA10, 0x1F40, 0xE3BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4A14)
    WaitChrThread(0x16, 0x1)
    OP_44(0x17, 0x2)
    Sleep(1000)

    def lambda_4A3D():
        OP_8F(0xFE, 0xFFFFD0BC, 0x1F40, 0xE3BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4A3D)

    def lambda_4A58():
        OP_8F(0xFE, 0xFFFFCEB4, 0x1F40, 0xE3BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A58)
    Sleep(600)

    def lambda_4A78():
        OP_8F(0xFE, 0xFFFFD0BC, 0x1F40, 0xE3BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4A78)

    def lambda_4A93():
        OP_8F(0xFE, 0xFFFFCEB4, 0x1F40, 0xE3BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4A93)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2147 end

    def Function_9_4ACA(): pass

    label("Function_9_4ACA")

    Sleep(600)

    label("loc_4ACF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AFF")
    OP_8C(0x16, 145, 500)
    Sleep(600)
    OP_8C(0x16, 45, 500)
    Sleep(600)
    OP_8C(0x16, 100, 500)
    Sleep(800)
    Jump("loc_4ACF")

    label("loc_4AFF")

    Return()

    # Function_9_4ACA end

    def Function_10_4B00(): pass

    label("Function_10_4B00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B45")

    def lambda_4B0F():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_4B0F)

    def lambda_4B29():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4B29)
    Sleep(2000)
    Jump("Function_10_4B00")

    label("loc_4B45")

    Return()

    # Function_10_4B00 end

    def Function_11_4B46(): pass

    label("Function_11_4B46")


    def lambda_4B4C():
        OP_8F(0xFE, 0xFFFFA4FC, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4B4C)

    def lambda_4B67():
        OP_8F(0xFE, 0xFFFF9D2C, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B67)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x18, 0x1)

    label("loc_4B86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C64")

    def lambda_4B95():
        OP_8F(0xFE, 0xFFFF9FE8, 0x1F40, 0xE3BC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4B95)
    WaitChrThread(0x16, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_4BBA():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_4BBA)

    def lambda_4BD4():
        OP_8F(0xFE, 0xFFFFA4FC, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4BD4)
    WaitChrThread(0x16, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4BF8")
    Jump("loc_4C64")

    label("loc_4BF8")


    def lambda_4BFE():
        OP_8F(0xFE, 0xFFFFA240, 0x1F40, 0xE3BC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4BFE)
    WaitChrThread(0x18, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_4C23():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4C23)

    def lambda_4C3D():
        OP_8F(0xFE, 0xFFFF9D2C, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4C3D)
    WaitChrThread(0x18, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4C61")
    Jump("loc_4C64")

    label("loc_4C61")

    Jump("loc_4B86")

    label("loc_4C64")

    Return()

    # Function_11_4B46 end

    def Function_12_4C65(): pass

    label("Function_12_4C65")


    def lambda_4C6B():
        OP_8E(0xFE, 0xFFFF9A0C, 0x1F40, 0xE7CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4C6B)
    WaitChrThread(0x107, 0x1)

    def lambda_4C8B():
        OP_8E(0xFE, 0xFFFF9A0C, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4C8B)
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x18, 500)
    Return()

    # Function_12_4C65 end

    def Function_13_4CAD(): pass

    label("Function_13_4CAD")


    def lambda_4CB3():
        OP_8E(0xFE, 0xFFFFA754, 0x1F40, 0xDE94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4CB3)
    WaitChrThread(0x17, 0x1)

    def lambda_4CD3():
        OP_8E(0xFE, 0xFFFFA754, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4CD3)
    WaitChrThread(0x17, 0x1)
    TurnDirection(0x17, 0x16, 500)
    Return()

    # Function_13_4CAD end

    def Function_14_4CF5(): pass

    label("Function_14_4CF5")

    OP_22(0xCC, 0x1, 0x28)
    Sleep(200)
    OP_24(0xCC, 0x32)
    Sleep(200)
    OP_24(0xCC, 0x3C)
    Sleep(200)
    OP_24(0xCC, 0x46)
    Sleep(200)
    OP_24(0xCC, 0x50)
    Sleep(200)
    OP_24(0xCC, 0x5A)
    Sleep(200)
    OP_24(0xCC, 0x64)
    Return()

    # Function_14_4CF5 end

    def Function_15_4D31(): pass

    label("Function_15_4D31")

    Sleep(1500)
    OP_82(0x2, 0x2)
    Sleep(500)
    OP_82(0x3, 0x2)
    Return()

    # Function_15_4D31 end

    def Function_16_4D42(): pass

    label("Function_16_4D42")


    def lambda_4D48():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D48)
    WaitChrThread(0xFE, 0x2)
    Sleep(400)

    label("loc_4D5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D7D")

    def lambda_4D6B():
        OP_99(0xFE, 0x4, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D6B)
    WaitChrThread(0xFE, 0x2)
    Jump("loc_4D5C")

    label("loc_4D7D")

    Return()

    # Function_16_4D42 end

    SaveToFile()

Try(main)
