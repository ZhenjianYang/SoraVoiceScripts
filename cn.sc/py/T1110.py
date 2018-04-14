from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1110   ._SN',
        MapName             = 'Bose',
        Location            = 'T1110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 3,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1110_1 ._SN',
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
        '莉咏',                                 # 9
        '阿尔贝尔',                             # 10
        '博尔德',                               # 11
        '拉娜',                                 # 12
        '艾尔珂',                               # 13
        '泊尔',                                 # 14
        '塞西尔婆婆',                           # 15
        '库瓦诺老人',                           # 16
        '莫德娜',                               # 17
        '米拉诺',                               # 18
        '特里诺',                               # 19
        '西蒙',                                 # 20
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01480 ._CH',             # 04
        'ED6_DT07/CH01220 ._CH',             # 05
        'ED6_DT07/CH01010 ._CH',             # 06
        'ED6_DT07/CH01000 ._CH',             # 07
        'ED6_DT07/CH01183 ._CH',             # 08
        'ED6_DT07/CH01230 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01143 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01480P._CP',             # 04
        'ED6_DT07/CH01220P._CP',             # 05
        'ED6_DT07/CH01010P._CP',             # 06
        'ED6_DT07/CH01000P._CP',             # 07
        'ED6_DT07/CH01183P._CP',             # 08
        'ED6_DT07/CH01230P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01143P._CP',             # 0C
    )

    DeclNpc(
        X                   = -21340,
        Z                   = 0,
        Y                   = 72520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -11200,
        Z                   = 5250,
        Y                   = 72600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -22100,
        Z                   = 0,
        Y                   = 69250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 20970,
        Z                   = 0,
        Y                   = 67860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 27100,
        Z                   = 4000,
        Y                   = 72200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 20100,
        Z                   = 0,
        Y                   = 68410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -16400,
        Z                   = 0,
        Y                   = -1700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -22530,
        Z                   = 0,
        Y                   = -410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -18730,
        Z                   = 70,
        Y                   = 33060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 16329,
        Z                   = 0,
        Y                   = 31480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -21100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20200,
        Z                   = 0,
        Y                   = 30680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_3E7",          # 01, 1
        "Function_2_3E8",          # 02, 2
        "Function_3_41F",          # 03, 3
        "Function_4_475",          # 04, 4
        "Function_5_4CB",          # 05, 5
        "Function_6_568",          # 06, 6
        "Function_7_AC2",          # 07, 7
        "Function_8_F6C",          # 08, 8
        "Function_9_16D2",         # 09, 9
        "Function_10_1BAB",        # 0A, 10
        "Function_11_1EE7",        # 0B, 11
        "Function_12_21AA",        # 0C, 12
        "Function_13_2991",        # 0D, 13
        "Function_14_2AA7",        # 0E, 14
        "Function_15_2F91",        # 0F, 15
        "Function_16_3672",        # 10, 16
        "Function_17_3C1C",        # 11, 17
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0x9, 0x80)
    Jump("loc_3C5")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2BA")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_3C5")

    label("loc_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2F0")
    ClearChrFlags(0x13, 0x80)
    OP_43(0x13, 0x0, 0x6, 0x2)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xE, -22530, 0, 1020, 180)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    Jump("loc_3C5")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_343")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 12900, 0, 69780, 0)
    SetChrPos(0xC, 22510, 0, 68280, 270)
    ClearChrFlags(0x13, 0x80)
    OP_43(0x13, 0x0, 0x6, 0x2)
    SetChrPos(0xE, -22530, 0, 1020, 180)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_3C5")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3BE")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 12900, 0, 69780, 0)
    SetChrPos(0xC, 22510, 0, 68280, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 12)
    SetChrPos(0x13, -20800, 0, 34930, 225)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -21830, 0, 35100, 90)
    Jump("loc_3C5")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3C5")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3CF")
    Jump("loc_3E6")

    label("loc_3CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E6")
    SetChrFlags(0x11, 0x80)

    label("loc_3E6")

    Return()

    # Function_0_292 end

    def Function_1_3E7(): pass

    label("Function_1_3E7")

    Return()

    # Function_1_3E7 end

    def Function_2_3E8(): pass

    label("Function_2_3E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41A")

    label("loc_3F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_417")
    OP_8D(0xFE, 20900, 30000, 15300, 31700, 2000)
    Jump("loc_3F4")

    label("loc_417")

    Jump("loc_41E")

    label("loc_41A")

    Call(6, 2)

    label("loc_41E")

    Return()

    # Function_2_3E8 end

    def Function_3_41F(): pass

    label("Function_3_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_451")

    label("loc_42B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44E")
    OP_8D(0xFE, 21600, 67480, 22890, 69030, 2000)
    Jump("loc_42B")

    label("loc_44E")

    Jump("loc_474")

    label("loc_451")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_474")
    OP_8D(0xFE, 26200, 71400, 28400, 72600, 2000)
    Jump("loc_451")

    label("loc_474")

    Return()

    # Function_3_41F end

    def Function_4_475(): pass

    label("Function_4_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A7")

    label("loc_481")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A4")
    OP_8D(0xFE, 12210, 70500, 14370, 68720, 1500)
    Jump("loc_481")

    label("loc_4A4")

    Jump("loc_4CA")

    label("loc_4A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CA")
    OP_8D(0xFE, 17430, 68790, 23880, 64870, 1500)
    Jump("loc_4A7")

    label("loc_4CA")

    Return()

    # Function_4_475 end

    def Function_5_4CB(): pass

    label("Function_5_4CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_567")
    OP_8E(0xFE, 0xFFFFA6F0, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFAB8C, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFADE4, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAEC0, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFADE4, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAB8C, 0x0, 0x11B34, 0x7D0, 0x0)
    Jump("Function_5_4CB")

    label("loc_567")

    Return()

    # Function_5_4CB end

    def Function_6_568(): pass

    label("Function_6_568")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_68F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_632")

    ChrTalk(    #0
        0xFE,
        (
            "从大局来考虑的话，\x01",
            "老公的分析是正确的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "但是对市民来说，\x01",
            "首先要考虑的还是生活问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "像国际形势之类的问题\x01",
            "大概没人会顾得了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "也许正因如此\x01",
            "才会这么恐怖吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_68C")

    label("loc_632")


    ChrTalk(    #4
        0xFE,
        (
            "现在是最严重的是\x01",
            "市民的照明和供暖问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "国际形势什么的，\x01",
            "现在不是考虑的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68C")

    Jump("loc_ABE")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_75A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70B")

    ChrTalk(    #6
        0xFE,
        (
            "我家的导力器也全部\x01",
            "停止运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "我儿子阿尔贝尔\x01",
            "虽然去了工房，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "但似乎工房也不能\x01",
            "修理好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_757")

    label("loc_70B")


    ChrTalk(    #9
        0xFE,
        (
            "我家的导力器也全部\x01",
            "停止运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "要是修不好的话\x01",
            "那可就真麻烦了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_757")

    Jump("loc_ABE")

    label("loc_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_764")
    Jump("loc_ABE")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_86D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7C3")

    ChrTalk(    #11
        0xFE,
        (
            "米拉诺现在\x01",
            "真像个商人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "真希望我家的阿尔贝尔\x01",
            "也能变成像她那样呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_7C3")


    ChrTalk(    #13
        0xFE,
        (
            "米拉诺现在\x01",
            "真像个商人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "真希望我家的阿尔贝尔\x01",
            "也能变成像她那样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "呼，我相信他是大器晚成，\x01",
            "以后一定会有出息的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "所以才会让他去\x01",
            "王立学院进修。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_86A")

    Jump("loc_ABE")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_93C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8C3")

    ChrTalk(    #17
        0xFE,
        (
            "我们也都是从露天市场\x01",
            "起家的商人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "去支援也是自己的义务。\x02",
    )

    CloseMessageWindow()
    Jump("loc_939")

    label("loc_8C3")


    ChrTalk(    #19
        0xFE,
        (
            "和特里诺家协力\x01",
            "进行超市修复工作\x01",
            "的支援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "我们也都是从露天市场\x01",
            "起家的商人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "去支援也是自己的义务。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_939")

    Jump("loc_ABE")

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_98C")

    ChrTalk(    #22
        0xFE,
        (
            "超市似乎\x01",
            "发生了不得了的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "老公慌慌张张地就\x01",
            "跑出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABE")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9FD")

    ChrTalk(    #24
        0xFE,
        (
            "博尔德家和特里诺家\x01",
            "都是柏斯的著名商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "虽然关系还算不错，\x01",
            "但也是竞争激烈的商业劲敌。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABE")

    label("loc_9FD")


    ChrTalk(    #26
        0xFE,
        (
            "博尔德家和特里诺家\x01",
            "都是柏斯的著名商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "虽然关系还算不错，\x01",
            "但也是竞争激烈的商业劲敌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "最近我们\x01",
            "一直比较支持特里诺，不过…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "因为和帝国开展贸易，\x01",
            "博尔德似乎开始扭转局面了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_ABE")

    TalkEnd(0x8)
    Return()

    # Function_6_568 end

    def Function_7_AC2(): pass

    label("Function_7_AC2")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B20")

    ChrTalk(    #30
        0xFE,
        (
            "马上要开始真正的\x01",
            "考前冲刺了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "虽然信心十足，\x01",
            "但还是很紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA0")

    label("loc_B20")


    ChrTalk(    #32
        0xFE,
        (
            "城里好像又\x01",
            "恢复了活力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "那么，我也开始努力\x01",
            "准备考试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "父母对我抱有那么大期望，\x01",
            "要是考砸的话，就太丢脸了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_BA0")

    Jump("loc_F68")

    label("loc_BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_CD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C12")

    ChrTalk(    #35
        0xFE,
        (
            "总被拿来和米拉诺姐姐比较，\x01",
            "也很令人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "毕竟人和人是不一样的，\x01",
            "怎么能比来比去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD6")

    label("loc_C12")


    ChrTalk(    #37
        0xFE,
        (
            "虽然米拉诺姐姐\x01",
            "确实很了不起…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "但总让我和她比也有点…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "因为我和姐姐\x01",
            "完全是不同类型的两种人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "如果说我是性格内向话，\x01",
            "那米拉诺姐姐就是外向性格的人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "……感觉就是这样。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_CD6")

    Jump("loc_F68")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D4C")

    ChrTalk(    #42
        0xFE,
        (
            "昨天爸爸和特里诺先生\x01",
            "一直在商谈支援什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "多亏他们的决定，所以今天\x01",
            "就开始修复工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFE")

    label("loc_D4C")


    ChrTalk(    #44
        0xFE,
        (
            "昨天爸爸和特里诺先生\x01",
            "一直在商谈支援什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "多亏他们的决定，所以今天\x01",
            "就开始修复工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "看见这些，\x01",
            "我忽然觉得商人其实也不坏…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "……不过我还是当不了那种人。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_DFE")

    Jump("loc_F68")

    label("loc_E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_E6D")

    ChrTalk(    #48
        0xFE,
        (
            "刚才爸爸他们\x01",
            "惊慌地跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "我爸爸很少\x01",
            "会那么惊慌失措的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "难道发生什么大事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F68")

    label("loc_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EC3")

    ChrTalk(    #51
        0xFE,
        (
            "虽然爸爸希望我以后\x01",
            "也成为商人…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "但我自己却并没有那种打算。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F68")

    label("loc_EC3")


    ChrTalk(    #53
        0xFE,
        (
            "我的父母希望我学习经济，\x01",
            "所以让我进了\x01",
            "王立学院读书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "虽然爸爸希望我以后\x01",
            "也成为商人…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "但我自己却并没有那种打算。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "虽然如此，\x01",
            "但我却并没有兴趣。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F68")

    TalkEnd(0x9)
    Return()

    # Function_7_AC2 end

    def Function_8_F6C(): pass

    label("Function_8_F6C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_10A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104E")

    ChrTalk(    #57
        0xFE,
        (
            "现在很担心照明和供暖\x01",
            "的问题啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "王国内出现这种状况，\x01",
            "会有国际性的影响啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "从军事方面说，利贝尔王国\x01",
            "要是没有了飞行舰队那可是天大的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "如果是以前的帝国的话，\x01",
            "肯定马上就会攻来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_10A4")

    label("loc_104E")


    ChrTalk(    #61
        0xFE,
        (
            "这次导力停止现象有着\x01",
            "国际性的影响力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "就算只是照明和供暖问题\x01",
            "也够我们受了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A4")

    Jump("loc_16CE")

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117E")

    ChrTalk(    #63
        0xFE,
        (
            "导力器不能使用…\x01",
            "真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "对利贝尔王国来说，\x01",
            "导力器就等同于我们的生命线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "如果失去机能的话，\x01",
            "会影响到无数事情的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "……呼，总之要做好准备了，\x01",
            "这次可不是能轻松解决的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_11E0")

    label("loc_117E")


    ChrTalk(    #67
        0xFE,
        (
            "对利贝尔王国来说，\x01",
            "导力器就等同于我们的生命线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "如果失去机能的话，\x01",
            "会影响到无数事情的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E0")

    Jump("loc_16CE")

    label("loc_11E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1264")

    ChrTalk(    #69
        0xFE,
        (
            "定期船刚恢复航运，\x01",
            "和帝国的交易也再次开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "真是遗憾，没有获得\x01",
            "预期的成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "这次真是遗憾啊，。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1315")

    label("loc_1264")


    ChrTalk(    #72
        0xFE,
        (
            "定期船刚恢复航运，\x01",
            "和帝国的交易也再次开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "真是遗憾，没有获得\x01",
            "预期的成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "全是因为\x01",
            "米拉诺小姐的努力才会如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "哎呀呀，又多了一个\x01",
            "令人头疼的竞争对手。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1315")

    Jump("loc_16CE")

    label("loc_1318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_149C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1385")

    ChrTalk(    #76
        0xFE,
        (
            "定期船的停运\x01",
            "也不能阻止米拉诺小姐的斗志啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "呼，我也要仔细\x01",
            "思考一下对应策略了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1499")

    label("loc_1385")


    ChrTalk(    #78
        0xFE,
        (
            "定期船停运这件事\x01",
            "对我来说，的确是件棘手的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "和帝国的交易量正呈现增加趋势，\x01",
            "就在这节骨眼上发生这样的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "我和特里诺为了超市\x01",
            "的支持工作一直忙个不停。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "特里诺有个叫米拉诺的女儿。\x01",
            "也许她会帮上些什么忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "有个那么有出息的女儿，\x01",
            "实在太让人羡慕了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1499")

    Jump("loc_16CE")

    label("loc_149C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14F3")

    ChrTalk(    #83
        0xFE,
        (
            "修复工事马上\x01",
            "就要开始了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "追加支援的资金\x01",
            "也要赶快落实啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_14F3")


    ChrTalk(    #85
        0xFE,
        (
            "修复工事马上\x01",
            "就要开始了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "所需要的材料\x01",
            "我和特里诺已经提供了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "不过真正动工以后\x01",
            "肯定马上又会不够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "追加支援的资金\x01",
            "必须要好好思考一下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1596")

    Jump("loc_16CE")

    label("loc_1599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_16CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1638")

    ChrTalk(    #89
        0xFE,
        (
            "互不侵犯条约也签定了，\x01",
            "和帝国之间的交易更加宽松了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "这样下去的话，\x01",
            "最近在生意上感觉落后特里诺不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "趁这个机会可以挽回局面呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16CE")

    label("loc_1638")


    ChrTalk(    #92
        0xFE,
        (
            "互不侵犯条约签署之后，\x01",
            "和帝国之间的交易更加宽松了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "我已经和帝国方面\x01",
            "做了很长一段时间的生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "趁这个机会，\x01",
            "希望可以拓展业务规模。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_16CE")

    TalkEnd(0xA)
    Return()

    # Function_8_F6C end

    def Function_9_16D2(): pass

    label("Function_9_16D2")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_178E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1749")

    ChrTalk(    #95
        0xFE,
        (
            "刚才去过了附近\x01",
            "的工房，不过…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "场面非常混乱，\x01",
            "只能回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "似乎哪家都\x01",
            "很困惑呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_178B")

    label("loc_1749")


    ChrTalk(    #98
        0xFE,
        (
            "因为工房那里很混乱，\x01",
            "只能回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "似乎哪家都\x01",
            "很困惑呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178B")

    Jump("loc_1BA7")

    label("loc_178E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_18A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1843")

    ChrTalk(    #100
        0xFE,
        (
            "照明设施没有了，\x01",
            "一到晚上就什么也看不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "慌慌张张地去找油灯\x01",
            "还真是好辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "因为怕黑，\x01",
            "女儿一直哭个不停…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "真希望能\x01",
            "早点恢复原来的生活啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_18A1")

    label("loc_1843")


    ChrTalk(    #104
        0xFE,
        (
            "照明设施没有了，\x01",
            "一到晚上就什么也看不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "导力器会瘫痪这种事，\x01",
            "以前连想都没有想过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A1")

    Jump("loc_1BA7")

    label("loc_18A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_195C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_18F5")

    ChrTalk(    #106
        0xFE,
        (
            "老公今天带着\x01",
            "女儿去工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "很想看看重新\x01",
            "营业的超市。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1959")

    label("loc_18F5")


    ChrTalk(    #108
        0xFE,
        (
            "老公今天带着\x01",
            "女儿去工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "很想看看重新\x01",
            "营业的超市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "还好没给周围的店\x01",
            "添麻烦……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1959")

    Jump("loc_1BA7")

    label("loc_195C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_19E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1990")

    ChrTalk(    #111
        0xFE,
        (
            "老公去北街区\x01",
            "查看修复工事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E1")

    label("loc_1990")


    ChrTalk(    #112
        0xFE,
        (
            "老公去北街区\x01",
            "查看修复工事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "不过我丈夫真是\x01",
            "对商业买卖很有兴趣呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_19E1")

    Jump("loc_1BA7")

    label("loc_19E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1A45")

    ChrTalk(    #114
        0xFE,
        (
            "和他在一起这么长时间…\x01",
            "真是好久没有这样过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "呵呵，简直就像回到了恋人时代。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA7")

    label("loc_1A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1A97")

    ChrTalk(    #116
        0xFE,
        (
            "超市竟然被\x01",
            "怪物袭击了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "……和平的日子\x01",
            "为什么一去不复返了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA7")

    label("loc_1A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1AED")

    ChrTalk(    #118
        0xFE,
        (
            "我老公在超市\x01",
            "经营服装店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "是家名叫『泊尔·艾尔珂』的店哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA7")

    label("loc_1AED")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)

    ChrTalk(    #120
        0xFE,
        "啊～都是很不错的和服呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "我老公在超市\x01",
            "经营服装店哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "追求流行的话，\x01",
            "那里的服装一定可以满足你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "有兴趣的话\x01",
            "请一定去光顾啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1BA7")

    TalkEnd(0xB)
    Return()

    # Function_9_16D2 end

    def Function_10_1BAB(): pass

    label("Function_10_1BAB")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0D")

    ChrTalk(    #124
        0xFE,
        (
            "导力工房里\x01",
            "全都是客人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "爸爸的店里\x01",
            "要是也有那么多客人就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1C2C")

    label("loc_1C0D")


    ChrTalk(    #126
        0xFE,
        (
            "导力工房里\x01",
            "全都是客人哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2C")

    Jump("loc_1EE3")

    label("loc_1C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB1")

    ChrTalk(    #127
        0xFE,
        (
            "家里一片漆黑，\x01",
            "真是好可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "导力炉也不能用了，\x01",
            "冷得要命……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "呜～\x01",
            "为什么导力器都不能用了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1CF9")

    label("loc_1CB1")


    ChrTalk(    #130
        0xFE,
        (
            "家里一片漆黑，\x01",
            "真是好可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "呜～\x01",
            "为什么导力器都不能用了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF9")

    Jump("loc_1EE3")

    label("loc_1CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1D30")

    ChrTalk(    #132
        0xFE,
        (
            "爸爸出去了，\x01",
            "今天我留下看家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D70")

    label("loc_1D30")


    ChrTalk(    #133
        0xFE,
        (
            "爸爸出去了，\x01",
            "今天我留下看家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "啊啊～～好没意思啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1D70")

    Jump("loc_1EE3")

    label("loc_1D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1DBA")

    ChrTalk(    #135
        0xFE,
        (
            "超市真的\x01",
            "好大呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "嗯……\x01",
            "是谁把它弄坏的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E04")

    label("loc_1DBA")


    ChrTalk(    #137
        0xFE,
        (
            "超市被破坏了，\x01",
            "所以爸爸也不用工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "……是谁把它弄坏的呢？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1E04")

    Jump("loc_1EE3")

    label("loc_1E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1E33")

    ChrTalk(    #139
        0xFE,
        (
            "今天爸爸\x01",
            "会早回来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E6F")

    label("loc_1E33")


    ChrTalk(    #140
        0xFE,
        (
            "今天爸爸\x01",
            "会早回来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "嘿嘿～要让他陪我一起玩。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1E6F")

    Jump("loc_1EE3")

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1EA0")

    ChrTalk(    #142
        0xFE,
        (
            "爸爸在超市里\x01",
            "卖洋装哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE3")

    label("loc_1EA0")


    ChrTalk(    #143
        0xFE,
        (
            "爸爸在超市里\x01",
            "卖洋装哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "我以后也想\x01",
            "到爸爸的店里帮忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1EE3")

    TalkEnd(0xC)
    Return()

    # Function_10_1BAB end

    def Function_11_1EE7(): pass

    label("Function_11_1EE7")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F5B")

    ChrTalk(    #145
        0xFE,
        (
            "这也许是女神的意思吧，\x01",
            "那么暂时就先停业好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "一边照顾女儿，\x01",
            "一边等着超市重新开门吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2000")

    label("loc_1F5B")


    ChrTalk(    #147
        0xFE,
        (
            "其他的商人都在\x01",
            "找其它的地方继续营业。\x01",
            "但我却准备暂时休息一阵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "服饰和日用品不同，\x01",
            "偶尔停业也没关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "这也许是女神的意思吧，\x01",
            "还是好好休息一阵子吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2000")

    Jump("loc_21A6")

    label("loc_2003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_21A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 4)), scpexpr(EXPR_END)), "loc_2062")

    ChrTalk(    #150
        0xFE,
        (
            "所幸客人们\x01",
            "也顺利避难了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "市长的女佣小姐要是\x01",
            "也能早点恢复就好了…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A6")

    label("loc_2062")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #152
        0xFE,
        (
            "啊，你们……\x01",
            "在超市时真是多谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "要不是你们的话\x01",
            "也许就无法得救了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "这一定是女神\x01",
            "的保佑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#1007F嗯……\x01",
            "能赶上真是太好了。\x02\x03",

            "#1002F超市的各位\x01",
            "已经平安避难了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #156
        0xFE,
        "嗯，托你们的福，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "大家都已经逃离了。\x01",
            "现在暂时待在旅店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "市长的女佣小姐要是\x01",
            "也能早点恢复就好了…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A44)

    label("loc_21A6")

    TalkEnd(0xD)
    Return()

    # Function_11_1EE7 end

    def Function_12_21AA(): pass

    label("Function_12_21AA")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2288")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222D")

    ChrTalk(    #159
        0xFE,
        (
            "老头子他去工房\x01",
            "还没回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "一定又是去哪里\x01",
            "偷懒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "要是再去钓鱼的话，\x01",
            "这次就不让他进家门了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2285")

    label("loc_222D")


    ChrTalk(    #162
        0xFE,
        (
            "明明都答应过不再去了，\x01",
            "但又给忘掉了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "真是的，老头子他\x01",
            "一天到晚什么都不干。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2285")

    Jump("loc_298D")

    label("loc_2288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2373")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231C")

    ChrTalk(    #164
        0xFE,
        (
            "隔壁的特里诺家的导力器\x01",
            "好像也出现故障了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "好像哪里都是\x01",
            "这个样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "还以为他老老实实在家，\x01",
            "但老头子竟然去工房了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2370")

    label("loc_231C")


    ChrTalk(    #167
        0xFE,
        (
            "本以为是导力器的故障，\x01",
            "但老头子竟然去工房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "算了，\x01",
            "应该马上就回来了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2370")

    Jump("loc_298D")

    label("loc_2373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_273C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 3)), scpexpr(EXPR_END)), "loc_2420")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_23C9")

    ChrTalk(    #169
        0xFE,
        (
            "钓杆的事\x01",
            "不用在意啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "对老头子来说\x01",
            "这样才是为他好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241D")

    label("loc_23C9")


    ChrTalk(    #171
        0xFE,
        "啊，是你们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "那个钓杆\x01",
            "随你们处置吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "对老头子来说\x01",
            "这样才是为他好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_241D")

    Jump("loc_2739")

    label("loc_2420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2484")

    ChrTalk(    #174
        0xFE,
        (
            "刚还在想去买东西，\x01",
            "这才发现老头子不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "要是看见他的话，\x01",
            "麻烦告诉我一声好吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2739")

    label("loc_2484")


    ChrTalk(    #176
        0xFE,
        "哎呀，真是已经没办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "刚还在想去买东西，\x01",
            "这才发现老头子不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "看来得用绳子\x01",
            "把他给绑住才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "要是看见他的话，\x01",
            "麻烦告诉我一声好吗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2736")

    ChrTalk(    #180
        0x101,
        (
            "#1011F啊，如果说是老爷爷的话，\x01",
            "我在『川蝉亭』见到过。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #181
        0xFE,
        (
            "什么？\x01",
            "真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1015F嗯、嗯……\x01",
            "似乎是去钓鱼的…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "呼～果然啊，\x01",
            "和我想的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "谢谢你们。\x01",
            "帮了我大忙啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "那么，把这个拿去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #186
        "\x07\x00得到了\x1F\x51\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x251, 1)

    ChrTalk(    #187
        0x101,
        "#1004F这、这是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "这是老头子珍藏的钓杆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "已经不想再把它\x01",
            "留在家里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "不用介意，拿走吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #191
        0x101,
        "#1016F可、可是～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "没关系啦，拿走吧。\x01",
            "这样对老头子也好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    OP_A2(0x1C33)

    label("loc_2736")

    OP_A2(0x6)

    label("loc_2739")

    Jump("loc_298D")

    label("loc_273C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_27D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2786")

    ChrTalk(    #193
        0xFE,
        (
            "不然他除了钓鱼\x01",
            "什么都不做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "已经拿他没办法了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27CF")

    label("loc_2786")


    ChrTalk(    #195
        0xFE,
        (
            "为什么我们非要去\x01",
            "湖边小屋啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "钓鱼什么的\x01",
            "一点兴趣也没有啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_27CF")

    Jump("loc_298D")

    label("loc_27D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_281A")

    ChrTalk(    #197
        0xFE,
        (
            "老头子好像完全不\x01",
            "清楚事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "还是那么悠闲。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2865")

    label("loc_281A")


    ChrTalk(    #199
        0xFE,
        (
            "老头子好像完全不\x01",
            "清楚事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "我还那么担心他，\x01",
            "简直就是笨蛋。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2865")

    Jump("loc_298D")

    label("loc_2868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_292B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_28C9")

    ChrTalk(    #201
        0xFE,
        (
            "老头子他就是个一根经，\x01",
            "只知道钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "哎呀呀，这样的人生\x01",
            "还真是轻松啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2928")

    label("loc_28C9")


    ChrTalk(    #203
        0xFE,
        (
            "明明都发生了\x01",
            "那么重大的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "老头子他就是那种\x01",
            "只知道钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "一根经的性格。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2928")

    Jump("loc_298D")

    label("loc_292B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_298D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2955")

    ChrTalk(    #206
        0xFE,
        (
            "老头子\x01",
            "又去钓鱼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298D")

    label("loc_2955")


    ChrTalk(    #207
        0xFE,
        (
            "老头子\x01",
            "又去钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "这可以算是一种病了吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_298D")

    TalkEnd(0xE)
    Return()

    # Function_12_21AA end

    def Function_13_2991(): pass

    label("Function_13_2991")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_29DE")

    ChrTalk(    #209
        0xFE,
        "『川蝉亭』真是个好地方。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "婆婆一定\x01",
            "也很喜欢吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3D")

    label("loc_29DE")


    ChrTalk(    #211
        0xFE,
        "啊，婆婆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "不如两个人\x01",
            "一起去『川蝉亭』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "偶尔扔下家事，\x01",
            "休息一下也不错吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2A3D")

    Jump("loc_2AA3")

    label("loc_2A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2A68")

    ChrTalk(    #214
        0xFE,
        (
            "超市究竟\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AA3")

    label("loc_2A68")


    ChrTalk(    #215
        0xFE,
        (
            "超市究竟\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "我才刚回来，\x01",
            "什么都不知道。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2AA3")

    TalkEnd(0xF)
    Return()

    # Function_13_2991 end

    def Function_14_2AA7(): pass

    label("Function_14_2AA7")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B15")

    ChrTalk(    #217
        0xFE,
        (
            "利贝尔国内的流通网\x01",
            "几乎已经全部瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "商品的安排全乱了，\x01",
            "大家都忙得要死。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2B71")

    label("loc_2B15")


    ChrTalk(    #219
        0xFE,
        (
            "利贝尔国内的流通网\x01",
            "几乎已经全部瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "想想日用品和食品的事，\x01",
            "就让人很不安呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B71")

    Jump("loc_2F8D")

    label("loc_2B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BFC")

    ChrTalk(    #221
        0xFE,
        (
            "城里的导力器好像已经\x01",
            "全部瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "而且原因\x01",
            "好像还是未知…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "出现这样的骚乱，大家的心情\x01",
            "我也可以理解。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2C40")

    label("loc_2BFC")


    ChrTalk(    #224
        0xFE,
        (
            "城里的导力器好像已经\x01",
            "全部瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "而且原因\x01",
            "好像还是未知…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C40")

    Jump("loc_2F8D")

    label("loc_2C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2C96")

    ChrTalk(    #226
        0xFE,
        (
            "今天准备去超市\x01",
            "买东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "总算是重新\x01",
            "开始营业了，\x01",
            "去买些东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8D")

    label("loc_2C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2CF3")

    ChrTalk(    #228
        0xFE,
        (
            "我们的人为了超市的复兴\x01",
            "一直努力忙碌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "不过米拉诺已经\x01",
            "完成了代理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D73")

    label("loc_2CF3")


    ChrTalk(    #230
        0xFE,
        (
            "我们的人为了超市的复兴\x01",
            "一直努力忙碌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "不过米拉诺已经\x01",
            "完成了代理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "之前和博尔德一家可是\x01",
            "一直处于对立地位的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2D73")

    Jump("loc_2F8D")

    label("loc_2D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2DD9")

    ChrTalk(    #233
        0xFE,
        (
            "我们的人和博尔德大叔\x01",
            "正在协力做支援工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "这就是\x01",
            "柏斯商人的可贵之处了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6D")

    label("loc_2DD9")


    ChrTalk(    #235
        0xFE,
        (
            "我们的人和博尔德大叔\x01",
            "正在协力做支援工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "只要是值得尊敬的人，\x01",
            "即使是商业对手也可以协力合作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "呵呵，这就是\x01",
            "柏斯商人的可贵之处了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2E6D")

    Jump("loc_2F8D")

    label("loc_2E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2ECD")

    ChrTalk(    #238
        0xFE,
        (
            "西蒙也在超市\x01",
            "不幸受伤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "不过只是轻伤而已，\x01",
            "算是不幸中的万幸了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F35")

    label("loc_2ECD")


    ChrTalk(    #240
        0xFE,
        (
            "西蒙也在超市\x01",
            "不幸受伤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "虽然只是轻伤，但似乎\x01",
            "还有人被压在瓦砾下了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "真是可怕啊… \x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2F35")

    Jump("loc_2F8D")

    label("loc_2F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2F8D")

    ChrTalk(    #243
        0xFE,
        (
            "柏斯商人们的视线\x01",
            "现在全都在帝国那里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "为此大家也都\x01",
            "在拼命努力呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8D")

    TalkEnd(0x10)
    Return()

    # Function_14_2AA7 end

    def Function_15_2F91(): pass

    label("Function_15_2F91")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2FC0")
    Call(1, 1)
    Jump("loc_2FC4")

    label("loc_2FC0")

    Call(1, 0)

    label("loc_2FC4")

    Jump("loc_366E")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_30C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3063")

    ChrTalk(    #245
        0xFE,
        (
            "就算找到了替代的输送管道，\x01",
            "接下来也会困难重重吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "一会也只有去仓库\x01",
            "使用人海战术运货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "西蒙要是回来的话\x01",
            "就让他帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_30C5")

    label("loc_3063")


    ChrTalk(    #248
        0xFE,
        (
            "就算找到了替代的输送管道，\x01",
            "接下来也会困难重重吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "一会也只有去仓库\x01",
            "使用人海战术运货了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C5")

    Jump("loc_366E")

    label("loc_30C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_319F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315A")

    ChrTalk(    #250
        0xFE,
        (
            "城里出现奇怪现象，\x01",
            "好像又是定期船事件…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "老实说，\x01",
            "我有种不好的预感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "这样下去的话，\x01",
            "恐怕还会发生不得了的事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_319C")

    label("loc_315A")


    ChrTalk(    #253
        0xFE,
        (
            "呼，还有在空中出现\x01",
            "的浮游岛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "总让人有种\x01",
            "不祥的预感呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319C")

    Jump("loc_366E")

    label("loc_319F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3210")

    ChrTalk(    #255
        0xFE,
        (
            "如我所想，飞船已经恢复了，\x01",
            "和帝国商人的合作也大获成功。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "博尔德大叔\x01",
            "这下可要后悔了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3296")

    label("loc_3210")


    ChrTalk(    #257
        0xFE,
        (
            "啊哈哈哈～～\x01",
            "这次真是不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "如我所想，飞船已经恢复了，\x01",
            "和帝国商人的合作也大获成功。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "博尔德大叔\x01",
            "这下可要后悔了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3296")

    Jump("loc_366E")

    label("loc_3299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_33DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3300")

    ChrTalk(    #260
        0xFE,
        (
            "飞船什么时候恢复呢……\x01",
            "关键就看这次了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "不能让博尔德大叔\x01",
            "他一个人笑到最后。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33DB")

    label("loc_3300")


    ChrTalk(    #262
        0xFE,
        (
            "可能的话我想先出手，\x01",
            "和帝国的人缔结协议……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "假如恢复贸易有所延误的话，\x01",
            "仓库的存货数量将难以承受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "话虽这么说，什么也不做的话，\x01",
            "笑到最后的就是博尔德大叔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "飞船什么时候恢复呢……\x01",
            "关键就看这次了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_33DB")

    Jump("loc_366E")

    label("loc_33DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_346E")

    ChrTalk(    #266
        0xFE,
        "不愧是小姐，真有本事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "我佩服的五体投地，\x01",
            "不快点发展生意不行了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "要是一直发呆的话，\x01",
            "博尔德大叔\x01",
            "就什么都没了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3526")

    label("loc_346E")


    ChrTalk(    #269
        0xFE,
        (
            "超市的修复工作，\x01",
            "今早好像开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "不愧是小姐，\x01",
            "手段之高明当真王国第一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "好了，佩服归佩服，\x01",
            "我也得快点去经营生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "要是一直发呆的话，\x01",
            "博尔德大叔\x01",
            "就什么都没了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3526")

    Jump("loc_366E")

    label("loc_3529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3581")

    ChrTalk(    #273
        0xFE,
        (
            "西蒙，\x01",
            "这点小事要忍耐，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "这么大个儿人哭得稀哩哗啦的，\x01",
            "不觉得羞耻吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_366E")

    label("loc_3581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_366E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_35D3")

    ChrTalk(    #275
        0xFE,
        (
            "和帝国间的贸易，\x01",
            "是我们的弱点啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "好想和老爸商量商量。\x02",
    )

    CloseMessageWindow()
    Jump("loc_366E")

    label("loc_35D3")


    ChrTalk(    #277
        0xFE,
        (
            "和帝国间的贸易，\x01",
            "对我们来说是弱点啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "在这点上，博尔德叔叔，\x01",
            "在很早以前就有一条很宽广的渠道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "超市的事\x01",
            "交给西蒙，\x01",
            "必须要制定出对策才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_366E")

    TalkEnd(0x11)
    Return()

    # Function_15_2F91 end

    def Function_16_3672(): pass

    label("Function_16_3672")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_378E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373E")

    ChrTalk(    #280
        0xFE,
        (
            "当前最大的问题是流通。\x01",
            "也就是搬运货物的手段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "火车和飞船都不行的话，\x01",
            "那就什么也运不了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "我们在某种程度上\x01",
            "做过心理准备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "……但这比想象的还要\x01",
            "严重也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_378B")

    label("loc_373E")


    ChrTalk(    #284
        0xFE,
        "当前最大的问题是流通。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        (
            "火车和飞船都不行的话，\x01",
            "那就什么也运不了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_378B")

    Jump("loc_3C18")

    label("loc_378E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3817")

    ChrTalk(    #286
        0xFE,
        (
            "城里不仅是导力器，\x01",
            "就连定期船好像也停了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "好不容易才重新和帝国商人\x01",
            "开始做买卖……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "……这真是糟糕啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_3883")

    label("loc_3817")


    ChrTalk(    #289
        0xFE,
        (
            "城里不仅是导力器，\x01",
            "就连定期船好像也停了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "这样的话，等到恢复\x01",
            "可能需要花费很长一段时间也说不定了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3883")

    Jump("loc_3C18")

    label("loc_3886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3956")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_38E2")

    ChrTalk(    #291
        0xFE,
        (
            "米拉诺出人意料的\x01",
            "擅长和帝国商人打交道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "啊哈哈，不愧是我女儿。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3953")

    label("loc_38E2")


    ChrTalk(    #293
        0xFE,
        (
            "米拉诺出人意料的\x01",
            "擅长和帝国商人打交道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "啊哈哈，不愧是我女儿。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "博尔德那家伙\x01",
            "肯定很不甘心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3953")

    Jump("loc_3C18")

    label("loc_3956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_39B5")

    ChrTalk(    #296
        0xFE,
        (
            "我们的贸易方针\x01",
            "完全交给米拉诺了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "希望能够让博尔德那家伙\x01",
            "大吃一惊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A32")

    label("loc_39B5")


    ChrTalk(    #298
        0xFE,
        (
            "这段时间\x01",
            "修复超市的工作\x01",
            "异常的繁忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "我们的贸易方针\x01",
            "完全交给米拉诺了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "希望能够让博尔德那家伙\x01",
            "大吃一惊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3A32")

    Jump("loc_3C18")

    label("loc_3A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3B36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3A9A")

    ChrTalk(    #301
        0xFE,
        (
            "和博尔德联手，\x01",
            "修复工作总算开工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "必须得趁早计划一下\x01",
            "接下来的支援策略。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B33")

    label("loc_3A9A")


    ChrTalk(    #303
        0xFE,
        (
            "和博尔德联手，\x01",
            "修复工作总算开工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "在座的各位，\x01",
            "假如无法筹集到建材的话，\x01",
            "很快瓦斯就会不够用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "必须得趁早计划一下\x01",
            "接下来的支援策略。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3B33")

    Jump("loc_3C18")

    label("loc_3B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3B8C")

    ChrTalk(    #306
        0xFE,
        "今后和帝国做生意是关键。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "对抗博尔德，\x01",
            "必须要耍点手段才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C18")

    label("loc_3B8C")


    ChrTalk(    #308
        0xFE,
        (
            "有互不侵犯条约在，\x01",
            "今后和帝国做生意是关键。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "不过，应酬帝国商人\x01",
            "从来就是博尔德的强项。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "是的，这样我们也\x01",
            "必须做点什么才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3C18")

    TalkEnd(0x12)
    Return()

    # Function_16_3672 end

    def Function_17_3C1C(): pass

    label("Function_17_3C1C")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3D81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3C89")

    ChrTalk(    #311
        0xFE,
        (
            "飞船没有恢复的这段时间\x01",
            "对买卖来说是个很大的考验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        "米拉诺也在烦恼，真是少见呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D7E")

    label("loc_3C89")


    ChrTalk(    #313
        0xFE,
        (
            "飞船没有恢复的这段时间\x01",
            "对买卖来说是个很大的考验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "假如恢复工作延迟的话，\x01",
            "虽然会有大量商品积压在库……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "但现在大家都在观望，\x01",
            "反而可以找到机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "是冒着风险决一胜负呢，\x01",
            "还是应该避开风险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        "米拉诺也正在烦恼，真是少见呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3D7E")

    Jump("loc_3EC1")

    label("loc_3D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3E38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3DAF")

    ChrTalk(    #318
        0xFE,
        (
            "嗯……\x01",
            "脖子还是很痛啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E35")

    label("loc_3DAF")


    ChrTalk(    #319
        0xFE,
        (
            "呵呵，因为在超市里\x01",
            "受伤了这才痛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        (
            "还好只受了这点伤，\x01",
            "我感谢还来不及呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "……但是，没办法啊。\x01",
            "痛总归还是痛的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3E35")

    Jump("loc_3EC1")

    label("loc_3E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3EC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3E59")

    ChrTalk(    #322
        0xFE,
        "痛，好痛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EC1")

    label("loc_3E59")


    ChrTalk(    #323
        0xFE,
        "啊，真痛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        (
            "米，米拉诺。\x01",
            "很感谢你帮我治疗，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        "但能不能稍微温柔点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        "……啊，痛啊！\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3EC1")

    TalkEnd(0x13)
    Return()

    # Function_17_3C1C end

    SaveToFile()

Try(main)
