from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4210   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '索蕾拉',                               # 9
        '亲卫队队员',                           # 10
        '亲卫队队员',                           # 11
        '希尔丹夫人',                           # 12
        '杜南公爵',                             # 13
        '科洛蒂娅公主',                         # 14
        '艾莉茜雅女王',                         # 15
        '管家菲利普',                           # 16
        '幻惑之铃露茜奥拉',                     # 17
        '瘦狼瓦鲁特',                           # 18
        '怪盗布卢布兰',                         # 19
        '歼灭天使玲',                           # 20
        '亲卫队队员',                           # 21
        '亲卫队队员',                           # 22
        '亲卫队队员',                           # 23
        '亲卫队队员',                           # 24
        '亲卫队队员',                           # 25
        '亲卫队队员',                           # 26
        '亲卫队队员',                           # 27
        '亲卫队队员',                           # 28
        '亲卫队队员',                           # 29
        '亲卫队队员',                           # 30
        '亲卫队队员',                           # 31
        '亲卫队队员',                           # 32
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
        'ED6_DT26/CH20447 ._CH',             # 00
        'ED6_DT26/CH20448 ._CH',             # 01
        'ED6_DT26/CH20449 ._CH',             # 02
        'ED6_DT07/CH01350 ._CH',             # 03
        'ED6_DT07/CH01320 ._CH',             # 04
        'ED6_DT07/CH02460 ._CH',             # 05
        'ED6_DT26/CH20421 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT26/CH20447P._CP',             # 00
        'ED6_DT26/CH20448P._CP',             # 01
        'ED6_DT26/CH20449P._CP',             # 02
        'ED6_DT07/CH01350P._CP',             # 03
        'ED6_DT07/CH01320P._CP',             # 04
        'ED6_DT07/CH02460P._CP',             # 05
        'ED6_DT26/CH20421P._CP',             # 06
    )

    DeclNpc(
        X                   = -170,
        Z                   = 1000,
        Y                   = 4390,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 5000,
        Z                   = 0,
        Y                   = -5000,
        Direction           = 182,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = 0,
        Y                   = -5000,
        Direction           = 182,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 9000,
        Y                   = 29200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -1880,
        Y                   = 8000,
        Z                   = 29100,
        Range               = 1580,
        Unknown_10          = 0x2AF8,
        Unknown_14          = 0x760C,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )


    ScpFunction(
        "Function_0_402",          # 00, 0
        "Function_1_49A",          # 01, 1
        "Function_2_51C",          # 02, 2
        "Function_3_540",          # 03, 3
        "Function_4_6C1",          # 04, 4
        "Function_5_7B3",          # 05, 5
        "Function_6_88D",          # 06, 6
        "Function_7_B10",          # 07, 7
        "Function_8_F7B",          # 08, 8
        "Function_9_1F85",         # 09, 9
        "Function_10_1FB3",        # 0A, 10
        "Function_11_1FE1",        # 0B, 11
        "Function_12_200F",        # 0C, 12
        "Function_13_21DA",        # 0D, 13
        "Function_14_2A39",        # 0E, 14
        "Function_15_2ACC",        # 0F, 15
        "Function_16_2B53",        # 10, 16
        "Function_17_2BAC",        # 11, 17
        "Function_18_2D13",        # 12, 18
        "Function_19_2E7A",        # 13, 19
        "Function_20_2FE1",        # 14, 20
    )


    def Function_0_402(): pass

    label("Function_0_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_41B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_427")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_427")
    ClearChrFlags(0xB, 0x80)

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 5)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43B")
    Call(0, 12)

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_44C")
    OP_A3(0x10F0)
    Event(0, 8)
    Jump("loc_499")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_45D")
    OP_A3(0x10F1)
    Event(0, 14)
    Jump("loc_499")

    label("loc_45D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_469"),
        (SWITCH_DEFAULT, "loc_499"),
    )


    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_481")
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_496")

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_496")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_496")

    Jump("loc_499")

    label("loc_499")

    Return()

    # Function_0_402 end

    def Function_1_49A(): pass

    label("Function_1_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B6")
    OP_B1("t4210_y")
    Jump("loc_4BF")

    label("loc_4B6")

    OP_B1("t4210_n")

    label("loc_4BF")

    OP_71(0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4F1")
    OP_22(0x87, 0x1, 0x1E)
    OP_22(0xAE, 0x1, 0x1E)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_77(0xFF, 0xBF, 0xB7, 0x0, 0x0)
    OP_72(0x6, 0x4)

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_END)), "loc_51B")
    OP_1B(0x1, 0x0, 0x11)
    OP_1B(0x2, 0x0, 0x12)
    OP_1B(0x8, 0x0, 0x12)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x13)
    OP_1B(0x5, 0x0, 0x13)
    OP_1B(0x6, 0x0, 0x13)

    label("loc_51B")

    Return()

    # Function_1_49A end

    def Function_2_51C(): pass

    label("Function_2_51C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53F")
    OP_8D(0xFE, -1790, 6330, 1580, 2190, 2000)
    Jump("Function_2_51C")

    label("loc_53F")

    Return()

    # Function_2_51C end

    def Function_3_540(): pass

    label("Function_3_540")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_57B")

    ChrTalk(    #0
        0xFE,
        "那位公爵大人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "还真不明事理呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BD")

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_614")

    ChrTalk(    #2
        0xFE,
        (
            "听说情报部的凯诺娜小姐\x01",
            "在昨天的事件中被捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "他说头头都一网打尽了，\x01",
            "一副很高兴的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "对了，特务部队的队长\x01",
            "好像还没被捉住？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 1)), scpexpr(EXPR_END)), "loc_634")

    ChrTalk(    #5
        0xFE,
        "呼，好忙好忙……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BD")

    label("loc_634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_6BD")

    ChrTalk(    #6
        0xFE,
        "咦，你问女佣室？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #7
        0xFE,
        (
            "从这里正面的会客室一直走，\x01",
            "能看到一个很大的入口吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 45, 400)

    ChrTalk(    #8
        0xFE,
        (
            "入口右侧的门进去\x01",
            "就是女佣室了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD")

    TalkEnd(0xFE)
    Return()

    # Function_3_540 end

    def Function_4_6C1(): pass

    label("Function_4_6C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_73B")

    ChrTalk(    #9
        0xFE,
        (
            "尤莉亚上尉\x01",
            "乘上了『埃尔赛尤』，\x01",
            "所以不在城堡内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "在上尉不在的这段时间，\x01",
            "我们一定会好好保卫这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AF")

    label("loc_73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_78E")

    ChrTalk(    #11
        0xFE,
        "好痛，伤口还没好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "不过能阻止那辆坦克\x01",
            "进入市区真是太好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AF")

    label("loc_78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_7AF")

    ChrTalk(    #13
        0xFE,
        "欢迎来到格兰赛尔城！\x02",
    )

    CloseMessageWindow()

    label("loc_7AF")

    TalkEnd(0xFE)
    Return()

    # Function_4_6C1 end

    def Function_5_7B3(): pass

    label("Function_5_7B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_81C")

    ChrTalk(    #14
        0xFE,
        (
            "前几天科洛蒂娅殿下带着\x01",
            "一副奇怪的表情回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "她最近好像一直在和\x01",
            "女王陛下说话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_889")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_851")

    ChrTalk(    #16
        0xFE,
        (
            "情报部还真是开发了个\x01",
            "了不起的东西……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_889")

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_889")

    ChrTalk(    #17
        0xFE,
        (
            "欢迎回来，亲卫队的尤莉亚上尉\x01",
            "现在不在这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_889")

    TalkEnd(0xFE)
    Return()

    # Function_5_7B3 end

    def Function_6_88D(): pass

    label("Function_6_88D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A92")

    ChrTalk(    #18
        0xFE,
        "#712F艾丝蒂尔小姐，还有约修亚先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        "#1040F好久不见了，希尔丹夫人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "#711F嗯，你能回来真好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1011F希尔丹夫人，科洛丝\x01",
            "在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "#710F……科洛蒂娅殿下\x01",
            "在前面的谒见室里。\x02\x03",

            "不过她现在正和女王陛下\x01",
            "进行着重要的谈话，\x01",
            "能不能请你们先不要进去？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1004F啊，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "#710F嗯，现在还不知道\x01",
            "她们何时会结束谈话。\x02\x03",

            "#713F你们难得来一次，\x01",
            "真不好意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1006F不，没关系的。\x02\x03",

            "我们只是因为到了王都\x01",
            "顺路过来看看。\x02\x03",

            "#1001F很抱歉，打扰了，\x01",
            "那我们就先走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1040F再见。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20DC)
    Jump("loc_B0C")

    label("loc_A92")


    ChrTalk(    #27
        0xFE,
        (
            "#710F科洛蒂娅殿下在前面的\x01",
            "谒见室里。\x02\x03",

            "不过她现在正和女王陛下\x01",
            "进行着重要的谈话。\x02\x03",

            "实在抱歉，\x01",
            "能不能请你们先不要进去？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0C")

    TalkEnd(0xFE)
    Return()

    # Function_6_88D end

    def Function_7_B10(): pass

    label("Function_7_B10")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x0, 0x7D0)
    OP_6D(350, 500, -3260, 0)
    OP_67(0, 7380, -10000, 0)
    OP_6B(4350, 0)
    OP_6C(45000, 0)
    OP_6E(513, 0)
    SetChrPos(0x101, 500, 0, -23600, 360)
    SetChrPos(0x105, -500, 0, -23650, 360)
    SetChrPos(0x104, -610, 0, -24600, 360)
    SetChrPos(0x108, 650, 0, -24680, 360)
    Sleep(500)
    FadeToBright(2000, 0)

    def lambda_BC6():
        OP_8E(0xFE, 0x258, 0x0, 0xFFFFB884, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC6)
    Sleep(300)

    def lambda_BE6():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFB884, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BE6)

    def lambda_C01():
        OP_8E(0xFE, 0x258, 0x0, 0xFFFFB370, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_C01)
    Sleep(300)

    def lambda_C21():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFB370, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C21)
    WaitChrThread(0x108, 0x1)
    Fade(1000)
    OP_6D(500, 0, -18600, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)

    def lambda_C8B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C8B)
    Sleep(50)

    def lambda_C9E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C9E)
    Sleep(50)

    def lambda_CB1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_CB1)
    Sleep(400)

    ChrTalk(    #28
        0x101,
        (
            "#1006F好了……\x01",
            "既然要在城里进行调查。\x02\x03",

            "那就先去和女王陛下\x01",
            "打个招呼，然后谈一谈……\x02\x03",

            "#1015F那个，我记得尤莉亚上尉\x01",
            "应该不在吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#542F嗯，她参加了埃尔赛尤的试飞，\x01",
            "现在去雷斯顿要塞出差了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x108,
        (
            "#073F那可真遗憾啊。\x02\x03",

            "如果那位大姐在的话\x01",
            "一定能帮上忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x104,
        (
            "#030F那还有没有其他\x01",
            "可以谈话的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        (
            "#040F我觉得也应该找\x01",
            "希尔丹夫人聊聊。\x02\x03",

            "如果玲的父母\x01",
            "去过格兰赛尔城堡的话\x01",
            "她一定会知道的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1006F确实，城堡里的事\x01",
            "没有希尔丹夫人不知道的。\x02\x03",

            "那么我们赶紧去找女王陛下\x01",
            "和希尔丹夫人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        (
            "#040F这种时间的话，我想祖母大人\x01",
            "应该在女王宫里。\x02\x03",

            "#047F希尔丹夫人嘛……让我想想。\x02\x03",

            "#542F到那边的女佣室问问的话\x01",
            "就能知道她在不在了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1001F嗯，明白了。\x02\x03",

            "#1011F那么我们就去女佣室和\x01",
            "女王宫吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1624)
    OP_28(0x8B, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_7_B10 end

    def Function_8_F7B(): pass

    label("Function_8_F7B")

    EventBegin(0x0)
    OP_D2(0x600E8, 0x600ED, 0x7)
    OP_D2(0x2701C8, 0x2701CD, 0x8)
    OP_D2(0x2701C6, 0x2701CB, 0x9)
    OP_D2(0x2701C9, 0x2701CE, 0xA)
    OP_D2(0x260003, 0x260008, 0xB)
    OP_D2(0x7035B, 0x70360, 0xC)
    OP_D2(0x7015A, 0x7015E, 0xD)
    OP_D2(0x6011B, 0x60120, 0xE)
    OP_D2(0x70141, 0x70145, 0xF)
    OP_D2(0x7035C, 0x70361, 0x10)
    OP_D2(0x2601BB, 0x2601C0, 0x11)
    OP_D2(0x2600A0, 0x2600A5, 0x12)
    OP_4A(0xB, 255)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x14, -5310, 0, -18490, 135)
    SetChrPos(0x15, -4080, 0, -17010, 180)
    SetChrPos(0x16, -5390, 0, -16770, 135)
    SetChrPos(0x17, -3760, 0, -15580, 180)
    SetChrPos(0x18, -2220, 0, -15380, 180)
    SetChrPos(0x19, -850, 0, -14430, 180)
    SetChrPos(0x1A, 1210, 0, -14490, 180)
    SetChrPos(0x1B, 2410, 0, -15390, 180)
    SetChrPos(0x1C, 3840, 0, -15090, 225)
    SetChrPos(0x1D, 4030, 0, -16540, 225)
    SetChrPos(0x1E, 5190, 0, -16930, 225)
    SetChrPos(0x1F, 5180, 0, -18310, 225)
    SetChrSubChip(0x14, 1)
    SetChrSubChip(0x15, 1)
    SetChrSubChip(0x16, 1)
    SetChrSubChip(0x17, 1)
    SetChrSubChip(0x18, 1)
    SetChrSubChip(0x19, 1)
    SetChrSubChip(0x1A, 1)
    SetChrSubChip(0x1B, 1)
    SetChrSubChip(0x1C, 1)
    SetChrSubChip(0x1D, 1)
    SetChrSubChip(0x1E, 1)
    SetChrSubChip(0x1F, 1)
    SetChrChipByIndex(0x14, 7)
    SetChrChipByIndex(0x15, 7)
    SetChrChipByIndex(0x16, 7)
    SetChrChipByIndex(0x17, 7)
    SetChrChipByIndex(0x18, 7)
    SetChrChipByIndex(0x19, 7)
    SetChrChipByIndex(0x1A, 7)
    SetChrChipByIndex(0x1B, 7)
    SetChrChipByIndex(0x1C, 7)
    SetChrChipByIndex(0x1D, 7)
    SetChrChipByIndex(0x1E, 7)
    SetChrChipByIndex(0x1F, 7)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0xC, -590, 9000, 10940, 180)
    SetChrPos(0xF, 810, 9000, 10940, 180)
    SetChrPos(0xD, -790, 9000, 12400, 180)
    SetChrPos(0xE, 350, 9000, 12440, 180)
    SetChrPos(0xB, 1460, 9000, 12700, 180)
    SetChrChipByIndex(0xC, 13)
    SetChrChipByIndex(0xF, 16)
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xE, 15)
    SetChrChipByIndex(0xD, 14)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(660, 0, -17440, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    OP_71(0x6, 0x4)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_23(0x87)
    OP_23(0xAE)
    FadeToBright(1000, 0)

    def lambda_1274():
        OP_6D(540, 9000, 12460, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1274)

    def lambda_128C():
        OP_67(0, 7060, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_128C)

    def lambda_12A4():
        OP_6B(2670, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12A4)

    def lambda_12B4():
        OP_6C(31000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12B4)
    OP_6E(280, 5000)
    Sleep(500)

    ChrTalk(    #36
        0xB,
        "#712F#5P难道城门……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        "#226F#5P可恶，守不住了吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 600)
    Sleep(300)

    ChrTalk(    #38
        0xC,
        (
            "#222F#6P科洛蒂娅！　希尔丹夫人！\x02\x03",

            "你们马、马上陪同陛下\x01",
            "前往女王宫！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1363():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1363)
    Sleep(50)

    def lambda_1376():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1376)
    Sleep(50)

    def lambda_1389():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1389)
    Sleep(50)

    def lambda_139C():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_139C)
    Sleep(500)

    ChrTalk(    #39
        0xD,
        "#409F#5P叔、叔叔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xE,
        "#093F#5P杜南，你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "#226F#6P我、我也是\x01",
            "利贝尔王室的一员！\x02\x03",

            "像这种公然侵犯王族权威之辈，\x01",
            "我又怎么可以视若不见！\x02\x03",

            "现在尤莉亚不在，\x01",
            "我来负责这里的指挥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        "#403F#5P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xC,
        (
            "#224F#6P哎呀！真讨厌！别磨磨蹭蹭的了！\x02\x03",

            "那些家伙的目的就是将\x01",
            "陛下和你劫持！\x02\x03",

            "他们要劫持利贝尔的女王和公主啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        "#402F#5P！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        (
            "#224F#6P你现在最重要的责任\x01",
            "就是保护好陛下和自己！\x02\x03",

            "不要忘记自己的使命，小丫头！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        "#406F#5P叔叔……谨遵吩咐。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)

    def lambda_1585():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1585)

    def lambda_1593():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1593)
    Sleep(300)

    ChrTalk(    #47
        0xD,
        (
            "#402F#6P祖母大人、希尔丹夫人！\x01",
            "我们赶快去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        (
            "#094F#5P嗯……好。\x02\x03",

            "#092F杜南……\x01",
            "请你一定要保重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xC,
        (
            "#221F#6P哈哈！我会让那些冒犯王族天威\x01",
            "的亡命之徒尝到苦头的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "#713F#5P……祝你们旗开得胜。\x02\x03",

            "#714F菲利普也要\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xB, 400)
    Sleep(300)

    ChrTalk(    #51
        0xF,
        "#720F#6P多谢关心。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 45, 600)

    def lambda_16C1():
        OP_6D(2750, 9000, 17440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16C1)
    OP_43(0xE, 0x0, 0x0, 0x9)
    Sleep(200)
    OP_8C(0xD, 45, 600)
    OP_43(0xD, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_8C(0xB, 45, 600)
    OP_43(0xB, 0x0, 0x0, 0xB)

    def lambda_1706():

        label("loc_1706")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_1706")

    QueueWorkItem2(0xF, 1, lambda_1706)

    def lambda_1717():

        label("loc_1717")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_1717")

    QueueWorkItem2(0xC, 1, lambda_1717)
    WaitChrThread(0x101, 0x1)
    Sleep(1500)
    OP_44(0xF, 0x1)
    OP_44(0xC, 0x1)

    def lambda_173A():
        OP_6D(430, 9000, 11240, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_173A)
    OP_6B(2550, 1500)
    TurnDirection(0xF, 0xC, 400)
    Sleep(300)

    ChrTalk(    #52
        0xF,
        (
            "#720F#2P……阁下，您真是太了不起了。\x02\x03",

            "我菲利普，此时此刻第一次\x01",
            "发自内心地感受到…能够侍奉阁下\x01",
            "真是我的幸运和荣耀。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xF, 400)
    Sleep(300)

    ChrTalk(    #53
        0xC,
        "#222F#6P咳咳……哼，别那么正经。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x88, 0x0, 0x50)
    OP_7C(0x0, 0x64, 0xBB8, 0x1F4)
    OP_72(0x6, 0x4)
    Sleep(500)
    OP_77(0xFF, 0xBF, 0xB7, 0x0, 0x1388)
    OP_22(0x87, 0x1, 0xA)
    OP_22(0xAE, 0x1, 0xA)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0x13C, 0x0, 0x50)
    Sleep(1000)
    OP_22(0xF6, 0x0, 0x50)
    OP_24(0x87, 0x14)
    OP_24(0xAE, 0x14)

    def lambda_1893():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1893)
    Sleep(50)

    def lambda_18A6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18A6)
    Sleep(2000)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x11, 9)
    SetChrChipByIndex(0x12, 10)
    SetChrChipByIndex(0x13, 11)
    SetChrPos(0x12, -100, 0, -32200, 0)
    SetChrPos(0x11, -160, 0, -34300, 0)
    SetChrPos(0x13, -1250, 0, -32860, 0)
    SetChrPos(0x10, 1220, 0, -33660, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Fade(1000)
    OP_6D(410, 0, -21270, 0)
    OP_67(0, 5250, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(148000, 0)
    OP_6E(331, 0)
    OP_24(0x87, 0x1E)
    OP_24(0xAE, 0x1E)

    def lambda_196F():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0xFFFFACF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_196F)
    Sleep(120)

    def lambda_198F():
        OP_8E(0xFE, 0xFFFFFB1E, 0x0, 0xFFFFA6B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_198F)
    Sleep(180)

    def lambda_19AF():
        OP_8E(0xFE, 0x4C4, 0x0, 0xFFFFA844, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19AF)
    Sleep(100)

    def lambda_19CF():
        OP_8E(0xFE, 0xFFFFFF60, 0x0, 0xFFFFA3BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19CF)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 18)
    SetChrSubChip(0x11, 0)
    Fade(500)
    OP_6D(130, 9000, 11060, 0)
    OP_67(0, 7350, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(31000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #54
        0xC,
        "#226F#5P他、他们来了吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "#720F#5P呼，好强烈的杀气……\x01",
            "简直就是些鬼气逼人的魔人。\x02\x03",

            "阁下…如果我被打倒的话，\x01",
            "请不要犹豫，马上逃走吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AD3():

        label("loc_1AD3")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_1AD3")

    QueueWorkItem2(0xC, 1, lambda_1AD3)

    ChrTalk(    #56
        0xC,
        "#223F#6P什么……！？\x02",
    )

    CloseMessageWindow()
    OP_8F(0xF, 0x410, 0x2328, 0x3516, 0x7D0, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x20)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 17)
    OP_0D()
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1B44():
        OP_99(0xFE, 0x1, 0x8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1B44)
    OP_8F(0xF, 0x410, 0x2328, 0x2C88, 0x1B58, 0x0)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrSubChip(0xF, 10)

    def lambda_1B7D():
        OP_6D(980, 1000, 3340, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B7D)

    def lambda_1B95():
        OP_67(0, 5250, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B95)

    def lambda_1BAD():
        OP_6B(2560, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BAD)

    def lambda_1BBD():
        OP_6C(33000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1BBD)

    def lambda_1BCD():
        OP_6E(331, 1000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1BCD)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0xF, 0xD2, 0x3E8, 0xB04, 0x3E8, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    OP_99(0xF, 0xB, 0xF, 0x5DC)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    def lambda_1C15():
        OP_6D(1040, 0, -17600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C15)

    def lambda_1C2D():
        OP_67(0, 4560, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C2D)

    def lambda_1C45():
        OP_6B(2590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C45)

    def lambda_1C55():
        OP_6E(390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C55)

    def lambda_1C65():

        label("loc_1C65")

        OP_99(0xFE, 0x1, 0x8, 0x9C4)
        OP_48()
        Jump("loc_1C65")

    QueueWorkItem2(0xF, 2, lambda_1C65)
    OP_8F(0xF, 0xBE, 0x0, 0xFFFFC1EE, 0x1F40, 0x0)
    OP_44(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1B, 0x20)

    def lambda_1DC7():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1DC7)
    Sleep(100)

    def lambda_1DDA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1DDA)
    WaitChrThread(0x1A, 0x1)

    ChrTalk(    #57
        0x1A,
        "#5P菲、菲利普先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x13,
        "#264F#6P咦？这不是细眼睛的爷爷吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        "#254F#4P老家伙，你是干什么的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xF,
        (
            "#720F#5P杜南公爵阁下的管家，\x01",
            "原·王室亲卫队大队长，\x01",
            "菲利普·雷纳尔参见！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0xF, 0x10, 0x17, 0x4B0)
    Sleep(500)

    ChrTalk(    #61
        0xF,
        (
            "#721F当年的本领……\x02\x03",

            "如今不知还剩下几成……\x01",
            "不如就在你们身上证实一下吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        "#252F#4P喔……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x12,
        "#231F#6P哈哈……这可有趣了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#241F#4P呵呵……\x01",
            "看来你能给我们带来一点乐趣呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x203C)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4200   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_8_F7B end

    def Function_9_1F85(): pass

    label("Function_9_1F85")

    OP_8E(0xFE, 0x143C, 0x2328, 0x6266, 0xFA0, 0x0)
    OP_8E(0xFE, 0x343A, 0x2328, 0x69C8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_1F85 end

    def Function_10_1FB3(): pass

    label("Function_10_1FB3")

    OP_8E(0xFE, 0x143C, 0x2328, 0x6266, 0xFA0, 0x0)
    OP_8E(0xFE, 0x343A, 0x2328, 0x69C8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_1FB3 end

    def Function_11_1FE1(): pass

    label("Function_11_1FE1")

    OP_8E(0xFE, 0x1360, 0x2328, 0x5CC6, 0xFA0, 0x0)
    OP_8E(0xFE, 0x343A, 0x2328, 0x69C8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_1FE1 end

    def Function_12_200F(): pass

    label("Function_12_200F")

    SetChrPos(0x14, 4280, 0, -19910, 45)
    SetChrPos(0x15, 5060, 0, -18690, 315)
    SetChrPos(0x16, 3940, 0, -17900, 225)
    SetChrPos(0x17, 3150, 0, -16390, 315)
    SetChrPos(0x18, 5220, 0, -14920, 180)
    SetChrPos(0x19, 3700, 0, -13350, 135)
    SetChrPos(0x1A, -3770, 0, -14210, 45)
    SetChrPos(0x1B, -5950, 0, -16070, 315)
    SetChrPos(0x1C, -4320, 0, -21290, 225)
    SetChrPos(0x1D, -5730, 0, -18970, 180)
    SetChrPos(0x1E, -3430, 0, -18480, 90)
    SetChrPos(0x1F, -4480, 0, -17140, 45)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x14, 0x1)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x16, 0x1)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    ClearChrFlags(0x1A, 0x1)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)
    ClearChrFlags(0x1D, 0x1)
    ClearChrFlags(0x1E, 0x1)
    ClearChrFlags(0x1F, 0x1)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrPos(0xF, -1100, 0, -7300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    ClearChrFlags(0xF, 0x1)
    SetChrChipByIndex(0xF, 6)
    SetChrSubChip(0xF, 5)
    SetChrPos(0xC, 940, 0, -6690, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xC, 0x20)
    Return()

    # Function_12_200F end

    def Function_13_21DA(): pass

    label("Function_13_21DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21FB")
    Call(0, 15)
    Call(0, 16)

    label("loc_21FB")

    SetChrPos(0x101, -380, 0, -33500, 0)
    SetChrPos(0x102, 480, 0, -33500, 0)
    SetChrPos(0xF8, -1190, 0, -34000, 0)
    SetChrPos(0xF9, 1290, 0, -34000, 0)
    SetChrPos(0xF, -750, 0, -6900, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 1)
    SetChrSubChip(0xF, 7)
    SetChrFlags(0xF, 0x1)
    OP_6D(400, 0, -28320, 0)
    OP_67(0, 7130, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_72(0x6, 0x4)

    def lambda_22B1():
        OP_8E(0xFE, 0xFFFFFE84, 0x0, 0xFFFFAB3C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22B1)
    Sleep(80)

    def lambda_22D1():
        OP_8E(0xFE, 0x370, 0x0, 0xFFFFAACE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22D1)
    Sleep(80)

    def lambda_22F1():
        OP_8E(0xFE, 0xFFFFFC72, 0x0, 0xFFFFA560, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_22F1)
    Sleep(80)

    def lambda_2311():
        OP_8E(0xFE, 0x384, 0x0, 0xFFFFA54C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2311)
    FadeToBright(1000, 0)

    def lambda_2335():
        OP_6D(810, 0, -20120, 2200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2335)

    def lambda_234D():
        OP_6E(293, 2200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_234D)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23C0")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_23FE")

    label("loc_23C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E7")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_23FE")

    label("loc_23E7")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_23FE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_242A")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2468")

    label("loc_242A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2451")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2468")

    label("loc_2451")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2468")

    Sleep(1000)

    ChrTalk(    #65
        0x101,
        "#1020F#6P这、这是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B8")

    ChrTalk(    #66
        0x107,
        (
            "#065F大、大家\x01",
            "都被打倒了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F1")

    ChrTalk(    #67
        0x106,
        (
            "#057F连王国军最强的\x01",
            "精锐部队也……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2560")

    label("loc_24F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_252A")

    ChrTalk(    #68
        0x103,
        (
            "#022F连王国军最强的\x01",
            "精锐部队也……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2560")

    label("loc_252A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2560")

    ChrTalk(    #69
        0x108,
        (
            "#072F连王国军最强的\x01",
            "精锐部队也……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2560")


    NpcTalk(    #70
        0xF,
        "男性的声音",
        "#4P艾、艾丝蒂尔小姐……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E2")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2620")

    label("loc_25E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2609")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2620")

    label("loc_2609")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2647")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2685")

    label("loc_2647")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2685")

    label("loc_266E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2685")

    Sleep(1000)

    def lambda_2690():
        OP_6B(2830, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2690)
    OP_6D(280, 0, -6850, 2000)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)

    def lambda_26C5():
        OP_6D(640, 0, -7360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26C5)

    def lambda_26DD():
        OP_67(0, 6310, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_26DD)

    def lambda_26F5():
        OP_8E(0xFE, 0xFFFFFD80, 0x0, 0xFFFFDE40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26F5)
    Sleep(80)

    def lambda_2715():
        OP_8E(0xFE, 0x1F4, 0x0, 0xFFFFDE2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2715)
    Sleep(80)

    def lambda_2735():
        OP_8E(0xFE, 0xFFFFFBE6, 0x0, 0xFFFFD800, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2735)
    Sleep(80)

    def lambda_2755():
        OP_8E(0xFE, 0x190, 0x0, 0xFFFFD800, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2755)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 400)
    WaitChrThread(0xF8, 0x1)
    OP_8C(0xF8, 0, 400)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0xF9, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #71
        0x101,
        (
            "#1020F#6P菲、菲利普先生！？\x01",
            "还有杜南公爵也……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#1042F莫非……\x01",
            "你们是打算拖住他们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xF,
        (
            "#722F#5P真、真惭愧……\x02\x03",

            "看来我还是老了……\x01",
            "没能拖久一点……\x02\x03",

            "#721F公、公爵阁下怎么样了……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2897")

    ChrTalk(    #74
        0x108,
        (
            "#070F不必担心。\x01",
            "看来只是被击晕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_2897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28D2")

    ChrTalk(    #75
        0x103,
        (
            "#524F他不要紧……\x01",
            "看来只是被击晕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2906")

    label("loc_28D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2906")

    ChrTalk(    #76
        0x106,
        (
            "#051F别担心。\x01",
            "看来只是被击晕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2906")


    ChrTalk(    #77
        0xF,
        (
            "#722F#5P那、那我就放心了……\x02\x03",

            "陛下她们去了女王宫……\x01",
            "请、请你们快点……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0xF, 0x1)
    SetChrChipByIndex(0xF, 6)
    SetChrSubChip(0xF, 5)
    SetChrPos(0xF, -1100, 0, -7300, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #78
        0x101,
        "#1020F#6P菲、菲利普先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        "#1035F没事的，只是晕过去了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #80
        0x102,
        (
            "#1042F#2P要赶快……\x01",
            "科洛丝她们很危险。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)

    ChrTalk(    #81
        0x101,
        "#1002F#6P嗯、嗯！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_21DA end

    def Function_14_2A39(): pass

    label("Function_14_2A39")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x0, 50, 0, -8940, 0)
    SetChrPos(0x1, 50, 0, -8940, 0)
    SetChrPos(0x2, 50, 0, -8940, 0)
    SetChrPos(0x3, 50, 0, -8940, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x203E)
    Sleep(200)
    FadeToBright(1000, 0)
    OP_1B(0x1, 0x0, 0x11)
    OP_1B(0x2, 0x0, 0x12)
    OP_1B(0x8, 0x0, 0x12)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x13)
    OP_1B(0x5, 0x0, 0x13)
    OP_1B(0x6, 0x0, 0x13)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_14_2A39 end

    def Function_15_2ACC(): pass

    label("Function_15_2ACC")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B46"),
        (1, "loc_2B4C"),
        (SWITCH_DEFAULT, "loc_2B52"),
    )


    label("loc_2B46")

    OP_A2(0x1200)
    Jump("loc_2B52")

    label("loc_2B4C")

    OP_A2(0x1201)
    Jump("loc_2B52")

    label("loc_2B52")

    Return()

    # Function_15_2ACC end

    def Function_16_2B53(): pass

    label("Function_16_2B53")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_16_2B53 end

    def Function_17_2BAC(): pass

    label("Function_17_2BAC")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2BCE"),
        (1, "loc_2C02"),
        (2, "loc_2C34"),
        (5, "loc_2C61"),
        (7, "loc_2C8E"),
        (6, "loc_2CBF"),
        (SWITCH_DEFAULT, "loc_2CF2"),
    )


    label("loc_2BCE")


    ChrTalk(    #82
        0x101,
        (
            "#1002F不，不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2C02")


    ChrTalk(    #83
        0x102,
        (
            "#1042F不对，不是这边。\x01",
            "……赶紧去女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2C34")


    ChrTalk(    #84
        0x103,
        (
            "#022F这边不对。\x01",
            "……赶紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2C61")


    ChrTalk(    #85
        0x106,
        (
            "#057F没时间磨蹭了，\x01",
            "赶快去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2C8E")


    ChrTalk(    #86
        0x108,
        (
            "#072F没空去别处了。\x01",
            "……抓紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2CBF")


    ChrTalk(    #87
        0x107,
        (
            "#062F不、不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2CF2")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_17_2BAC end

    def Function_18_2D13(): pass

    label("Function_18_2D13")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2D35"),
        (1, "loc_2D69"),
        (2, "loc_2D9B"),
        (5, "loc_2DC8"),
        (7, "loc_2DF5"),
        (6, "loc_2E26"),
        (SWITCH_DEFAULT, "loc_2E59"),
    )


    label("loc_2D35")


    ChrTalk(    #88
        0x101,
        (
            "#1002F不，不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E59")

    label("loc_2D69")


    ChrTalk(    #89
        0x102,
        (
            "#1042F不对，不是这边。\x01",
            "……赶紧去女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E59")

    label("loc_2D9B")


    ChrTalk(    #90
        0x103,
        (
            "#022F这边不对。\x01",
            "……赶紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E59")

    label("loc_2DC8")


    ChrTalk(    #91
        0x106,
        (
            "#057F没时间磨蹭了，\x01",
            "赶快去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E59")

    label("loc_2DF5")


    ChrTalk(    #92
        0x108,
        (
            "#072F没空去别处了。\x01",
            "……抓紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E59")

    label("loc_2E26")


    ChrTalk(    #93
        0x107,
        (
            "#062F不、不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E59")

    label("loc_2E59")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_18_2D13 end

    def Function_19_2E7A(): pass

    label("Function_19_2E7A")

    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2E9C"),
        (1, "loc_2ED0"),
        (2, "loc_2F02"),
        (5, "loc_2F2F"),
        (7, "loc_2F5C"),
        (6, "loc_2F8D"),
        (SWITCH_DEFAULT, "loc_2FC0"),
    )


    label("loc_2E9C")


    ChrTalk(    #94
        0x101,
        (
            "#1002F不，不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC0")

    label("loc_2ED0")


    ChrTalk(    #95
        0x102,
        (
            "#1042F不对，不是这边。\x01",
            "……赶紧去女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC0")

    label("loc_2F02")


    ChrTalk(    #96
        0x103,
        (
            "#022F这边不对。\x01",
            "……赶紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC0")

    label("loc_2F2F")


    ChrTalk(    #97
        0x106,
        (
            "#057F没时间磨蹭了，\x01",
            "赶快去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC0")

    label("loc_2F5C")


    ChrTalk(    #98
        0x108,
        (
            "#072F没空去别处了。\x01",
            "……抓紧去女王宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC0")

    label("loc_2F8D")


    ChrTalk(    #99
        0x107,
        (
            "#062F不、不是这边。\x01",
            "……得抓紧前往女王宫！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC0")

    label("loc_2FC0")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_19_2E7A end

    def Function_20_2FE1(): pass

    label("Function_20_2FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32BE")
    EventBegin(0x1)
    TurnDirection(0xB, 0x0, 400)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    OP_4A(0xB, 255)
    SetChrFlags(0xB, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3216")

    ChrTalk(    #100
        0xB,
        "#712F艾丝蒂尔小姐，还有约修亚先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        "#1040F好久不见了，希尔丹夫人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        "#711F嗯，你能回来真好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1011F希尔丹夫人，科洛丝\x01",
            "在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xB,
        (
            "#710F……科洛蒂娅殿下\x01",
            "在前面的谒见室里。\x02\x03",

            "不过她现在在和女王陛下\x01",
            "进行着重要的谈话，\x01",
            "能不能请你们先不要进去？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1004F啊，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xB,
        (
            "#710F嗯，现在还不知道\x01",
            "她们何时会结束谈话。\x02\x03",

            "#713F你们难得来一次，\x01",
            "真不好意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1006F不，没关系的。\x02\x03",

            "我们只是因为到了王都\x01",
            "顺路过来看看。\x02\x03",

            "#1001F很抱歉，打扰了，\x01",
            "那我们就先走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        "#1040F再见。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20DC)
    Jump("loc_3290")

    label("loc_3216")


    ChrTalk(    #109
        0xB,
        (
            "#710F科洛蒂娅殿下在前面的\x01",
            "谒见室里。\x02\x03",

            "不过她现在在和女王陛下\x01",
            "进行着重要的谈话。\x02\x03",

            "实在抱歉，\x01",
            "能不能请你们先不要进去？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3290")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8C(0xB, 180, 400)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0xB, 255)
    ClearChrFlags(0xB, 0x40)
    Jump("loc_32BE")

    label("loc_32BE")

    Return()

    # Function_20_2FE1 end

    SaveToFile()

Try(main)
