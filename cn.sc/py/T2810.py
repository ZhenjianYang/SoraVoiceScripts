from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2810   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '拉迪奥老师',                           # 9
        '碧欧拉老师',                           # 10
        '米丽亚老师',                           # 11
        '科林兹校长',                           # 12
        '亚吉鲁',                               # 13
        '巴克斯',                               # 14
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
        'ED6_DT07/CH01663 ._CH',             # 00
        'ED6_DT07/CH01213 ._CH',             # 01
        'ED6_DT07/CH01433 ._CH',             # 02
        'ED6_DT07/CH02603 ._CH',             # 03
        'ED6_DT07/CH01360 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01663P._CP',             # 00
        'ED6_DT07/CH01213P._CP',             # 01
        'ED6_DT07/CH01433P._CP',             # 02
        'ED6_DT07/CH02603P._CP',             # 03
        'ED6_DT07/CH01360P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
    )

    DeclNpc(
        X                   = 87640,
        Z                   = 200,
        Y                   = 2820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 84430,
        Z                   = 200,
        Y                   = 1120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 84510,
        Z                   = 200,
        Y                   = 2890,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 2540,
        Z                   = 0,
        Y                   = 33300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2120,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    DeclActor(
        TriggerX            = 116010,
        TriggerZ            = 0,
        TriggerY            = 2750,
        TriggerRange        = 400,
        ActorX              = 116010,
        ActorZ              = 1700,
        ActorY              = 4800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1E3",          # 01, 1
        "Function_2_1E4",          # 02, 2
        "Function_3_260",          # 03, 3
        "Function_4_2F3",          # 04, 4
        "Function_5_62E",          # 05, 5
        "Function_6_67D",          # 06, 6
        "Function_7_6D6",          # 07, 7
        "Function_8_70E",          # 08, 8
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Return()

    # Function_0_1E2 end

    def Function_1_1E3(): pass

    label("Function_1_1E3")

    Return()

    # Function_1_1E3 end

    def Function_2_1E4(): pass

    label("Function_2_1E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_21C")

    ChrTalk(    #0
        0xFE,
        (
            "这种时候要是碰上什么人\x01",
            "肯定会吓一跳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C")

    label("loc_21C")

    OP_A2(0x2)

    ChrTalk(    #1
        0xFE,
        (
            "哎呀，这样的夜晚\x01",
            "来这里干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "我在检查门户呢。\x02",
    )

    CloseMessageWindow()

    label("loc_25C")

    TalkEnd(0xFE)
    Return()

    # Function_2_1E4 end

    def Function_3_260(): pass

    label("Function_3_260")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A4")

    ChrTalk(    #3
        0xFE,
        (
            "好了，要是没事\x01",
            "就赶快走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "别夺走我的孤独。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF")

    label("loc_2A4")

    OP_A2(0x1)

    ChrTalk(    #5
        0xFE,
        (
            "呼呼呼……\x01",
            "黑暗真令人安定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "果然，毫无人气的\x01",
            "夜晚校舍最棒了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF")

    TalkEnd(0xFE)
    Return()

    # Function_3_260 end

    def Function_4_2F3(): pass

    label("Function_4_2F3")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_383")
    Jump("loc_3C5")

    label("loc_383")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39F")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C5")

    label("loc_39F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BB")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C5")

    label("loc_3BB")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C5")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_42F")

    ChrTalk(    #7
        0xB,
        (
            "#780F旧校舍里可能\x01",
            "潜伏着魔兽。\x02\x03",

            "一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_625")

    label("loc_42F")

    OP_A2(0x0)

    ChrTalk(    #8
        0xB,
        (
            "#780F我问过老师了，\x01",
            "据说你们准备前往旧校舍探索了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x105, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    SetChrSubChip(0xB, 1)
    Jump("loc_4BD")

    label("loc_497")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")
    SetChrSubChip(0xB, 2)
    Jump("loc_4BD")

    label("loc_4B8")

    SetChrSubChip(0xB, 0)

    label("loc_4BD")

    OP_8C(0xB, 180, 0)
    SetChrFlags(0xB, 0x10)
    Sleep(200)

    ChrTalk(    #9
        0xB,
        "#780F科洛丝，你也去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        (
            "#040F是的，旧校舍的事\x01",
            "我最清楚了，\x01",
            "应该能帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        (
            "#780F唔，原来如此。\x01",
            "那样也好。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_55C")
    TurnDirection(0xB, 0x103, 0)
    Jump("loc_563")

    label("loc_55C")

    TurnDirection(0xB, 0x106, 0)

    label("loc_563")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_584")
    SetChrSubChip(0xB, 1)
    Jump("loc_5AA")

    label("loc_584")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A5")
    SetChrSubChip(0xB, 2)
    Jump("loc_5AA")

    label("loc_5A5")

    SetChrSubChip(0xB, 0)

    label("loc_5AA")

    OP_8C(0xB, 180, 0)
    SetChrFlags(0xB, 0x10)
    Sleep(200)

    ChrTalk(    #12
        0xB,
        (
            "#780F那么各位，\x01",
            "科洛丝就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_608")

    ChrTalk(    #13
        0x103,
        "#020F嗯嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_625")

    label("loc_608")


    ChrTalk(    #14
        0x106,
        "#050F啊啊，交给我们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_625")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_4_2F3 end

    def Function_5_62E(): pass

    label("Function_5_62E")

    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        (
            "这次我们班\x01",
            "看来相当努力了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "这样就能赢过\x01",
            "碧欧拉的班级了嘛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_62E end

    def Function_6_67D(): pass

    label("Function_6_67D")

    TalkBegin(0xFE)

    ChrTalk(    #17
        0xFE,
        (
            "哼哼，我们班\x01",
            "这次也干得不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "至少赢过米丽亚\x01",
            "的班应该是毫无疑问的了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_67D end

    def Function_7_6D6(): pass

    label("Function_7_6D6")

    TalkBegin(0xFE)

    ChrTalk(    #19
        0xFE,
        (
            "呼～总算\x01",
            "快打完分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "哎呀，肩膀好硬。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_6D6 end

    def Function_8_70E(): pass

    label("Function_8_70E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #21
        (
            "\x07\x05　　走　\x01",
            "　　廊　\x01",
            "　　里　\x01",
            "　　请　\x01",
            "　　安　\x01",
            "　学静　\x01",
            "　生！　\x01",
            "　指　　\x01",
            "　导　　\x01",
            "　部　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_70E end

    SaveToFile()

Try(main)
