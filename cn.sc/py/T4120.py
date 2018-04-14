from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4120   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4120.x',
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
        '夏伊',                                 # 9
        '史帕德',                               # 10
        '塞森',                                 # 11
        '多姆',                                 # 12
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
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01680 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01680P._CP',             # 04
    )

    DeclNpc(
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 129840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_2FD",          # 01, 1
        "Function_2_36A",          # 02, 2
        "Function_3_38E",          # 03, 3
        "Function_4_393",          # 04, 4
        "Function_5_163D",         # 05, 5
        "Function_6_1642",         # 06, 6
        "Function_7_1D2C",         # 07, 7
        "Function_8_1D31",         # 08, 8
        "Function_9_2211",         # 09, 9
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1DC")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_2FC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E6")
    Jump("loc_2FC")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1F0")
    Jump("loc_2FC")

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_1FA")
    Jump("loc_2FC")

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_22D")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)
    Jump("loc_2FC")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_237")
    Jump("loc_2FC")

    label("loc_237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_241")
    Jump("loc_2FC")

    label("loc_241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_24B")
    Jump("loc_2FC")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_27E")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)
    Jump("loc_2FC")

    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2B1")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)
    Jump("loc_2FC")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E8")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)
    Jump("loc_2FC")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2F2")
    Jump("loc_2FC")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2FC")
    Jump("loc_2FC")

    label("loc_2FC")

    Return()

    # Function_0_1BE end

    def Function_1_2FD(): pass

    label("Function_1_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_310")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_324")
    OP_64(0x2, 0x1)

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_340")
    OP_B1("t4120_y")
    Jump("loc_349")

    label("loc_340")

    OP_B1("t4120_n")

    label("loc_349")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)

    label("loc_369")

    Return()

    # Function_1_2FD end

    def Function_2_36A(): pass

    label("Function_2_36A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38D")
    OP_8D(0x9, 1470, 131290, -1690, 128210, 2000)
    Jump("Function_2_36A")

    label("loc_38D")

    Return()

    # Function_2_36A end

    def Function_3_38E(): pass

    label("Function_3_38E")

    Call(0, 4)
    Return()

    # Function_3_38E end

    def Function_4_393(): pass

    label("Function_4_393")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E5")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3C8")
    OP_A9(0xDB)
    Jump("loc_3CA")

    label("loc_3C8")

    OP_A9(0xC8)

    label("loc_3CA")

    TalkEnd(0xA)
    Return()

    label("loc_3D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E2")
    TalkEnd(0xA)
    Return()

    label("loc_3E2")

    Jump("loc_EDC")

    label("loc_3E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDC")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 60400, 0, -60, 270)
    SetChrPos(0x102, 60400, 0, 800, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C")
    SetChrPos(0xF9, 61510, 0, -60, 270)
    SetChrPos(0xF8, 61510, 0, 800, 270)
    Jump("loc_46E")

    label("loc_44C")

    SetChrPos(0xF8, 61510, 0, -60, 270)
    SetChrPos(0xF9, 61510, 0, 800, 270)

    label("loc_46E")

    OP_8C(0xA, 90, 0)
    OP_6D(60390, 0, 280, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0xA,
        (
            "啊，不好意思，\x01",
            "工房现在不能用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "前几天导力驱动的\x01",
            "器材就全部不动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "真是莫名其妙……\x01",
            "这样的话生意都没法做了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_566")

    ChrTalk(    #3
        0x101,
        (
            "#1018F#4P啊，那个不用担心。\x02\x03",

            "我们带了好东西来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        "好东西？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D5")

    label("loc_566")


    ChrTalk(    #5
        0x101,
        (
            "#1026F#4P啊，是吗……\x02\x03",

            "#1015F唔，不过还是很麻烦啊。\x02\x03",

            "结晶回路的合成和结晶孔的强化\x01",
            "都完全不能进行……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_632")

    ChrTalk(    #6
        0x103,
        (
            "#025F就算能用魔法，\x01",
            "像现在这样也有点不方便。\x02\x03",

            "难得的发生器也\x01",
            "也变宝为废了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F9")

    label("loc_632")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69A")

    ChrTalk(    #7
        0x108,
        (
            "#072F呼，就算能用魔法，\x01",
            "像现在这样也有点不方便。÷\x02\x03",

            "难得的发生器也\x01",
            "也变宝为废了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F9")

    label("loc_69A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F9")

    ChrTalk(    #8
        0x106,
        (
            "#552F就算能用魔法，\x01",
            "像现在这样也有点不方便。\x02\x03",

            "难得的发生器也\x01",
            "也变宝为废了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_740")

    ChrTalk(    #9
        0x107,
        (
            "#064F啊，可是姐姐……\x02\x03",

            "临时性的话\x01",
            "可能会有办法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77C")

    label("loc_740")


    ChrTalk(    #10
        0x102,
        (
            "#1043F#1P确实……\x02\x03",

            "#1040F不过临时性的话\x01",
            "可能会有办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F9")

    def lambda_7AC():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7AC)
    Sleep(120)

    def lambda_7BF():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7BF)

    def lambda_7CD():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7CD)
    Sleep(120)

    def lambda_7E0():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7E0)

    def lambda_7EE():
        TurnDirection(0xA, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7EE)
    Jump("loc_800")

    label("loc_7F9")

    TurnDirection(0x101, 0x102, 400)

    label("loc_800")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #11
        0x101,
        "#1004F#4P咦……什么意思！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_865")

    ChrTalk(    #12
        0x106,
        "#052F能让工房恢复使用吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C2")

    label("loc_865")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_895")

    ChrTalk(    #13
        0x103,
        "#023F能让工房恢复使用吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C2")

    label("loc_895")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C2")

    ChrTalk(    #14
        0x108,
        "#073F能让工房恢复使用吗？\x02",
    )

    CloseMessageWindow()

    label("loc_8C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_904")

    ChrTalk(    #15
        0x107,
        (
            "#060F是，是，大概……\x02\x03",

            "用那个发生器的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93B")

    label("loc_904")


    ChrTalk(    #16
        0x102,
        (
            "#1040F#1P是，恐怕……\x02\x03",

            "用那个发生器的花，有可能。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93B")


    ChrTalk(    #17
        0x101,
        "#1018F#4P啊，原来如此！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "喂，你们……\x01",
            "从刚才起在说些什么？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_985():
        TurnDirection(0x0, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_985)
    Sleep(120)

    def lambda_998():
        TurnDirection(0x1, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_998)

    def lambda_9A6():
        TurnDirection(0x2, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9A6)
    Sleep(120)

    def lambda_9B9():
        TurnDirection(0x3, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9B9)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_9D5")


    ChrTalk(    #19
        0x102,
        "#1040F#1P那个，是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05说明了使用『零力场发生器』\x01",
            "可暂时恢复工房机能的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #21
        0xA,
        "这是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "工房的器材就在那里。\x01",
            "你们能不能快点试试？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1006F#4P好的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD9")

    ChrTalk(    #24
        0x107,
        (
            "#560F那么～\x01",
            "请稍等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC")

    label("loc_AD9")


    ChrTalk(    #25
        0x102,
        "#1040F#1P那我们就借用一会儿。\x02",
    )

    CloseMessageWindow()

    label("loc_AFC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05使用『零力场发生器』将工房机能恢复了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #27
        0xA,
        (
            "哦哦……\x01",
            "导力好像确实恢复了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBF")
    TurnDirection(0xA, 0x0, 400)

    ChrTalk(    #28
        0xA,
        (
            "好，要调整导力器的话\x01",
            "就趁现在了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF1")

    label("loc_BBF")


    ChrTalk(    #29
        0x101,
        (
            "#1000F#4P听好了……\x01",
            "看来是成功了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")

    ChrTalk(    #30
        0x107,
        (
            "#063F嗯，不过是暂时\x01",
            "能用而已……\x02\x03",

            "#561F过一会儿应该\x01",
            "就会再度停下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C99")

    label("loc_C42")


    ChrTalk(    #31
        0x102,
        (
            "#1040F#1P虽然很顺利……\x01",
            "不过这也只能算是应急措施。\x02\x03",

            "过一会儿应该\x01",
            "就会再度停下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C99")

    TurnDirection(0xA, 0x0, 400)

    ChrTalk(    #32
        0xA,
        (
            "唔，是吗，\x01",
            "不是真的修好了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "不过你们可以趁现在\x01",
            "调整导力器什么的。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    label("loc_CF1")

    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x77)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #34
        0xA,
        (
            "即便如此，这个叫发生器的\x01",
            "东西还真了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "价钱是好商量……\x01",
            "不过你们多少钱肯卖？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1004F#4P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        (
            "就算价格高一些\x01",
            "我们也可以事先研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "因为只有我们的器材能\x01",
            "用的话说不定能发一笔大财。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1016F#4P那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#1040F#1P非常抱歉，\x01",
            "这是我们执行任务所必须的。\x02\x03",

            "而且就算工房营业，\x01",
            "市民们的导力器不能使用\x01",
            "也一样没有意义……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        "唔，我把这事给忘了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "那么你们来店里的话\x01",
            "就把那东西带过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "那样的话就能像过去一样地\x01",
            "使用工房了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20E5)
    EventEnd(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9B")

    ChrTalk(    #44
        0xA,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "导力停止的时候\x01",
            "顾客都涌进来问\x01",
            "是不是商品的缺陷和故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "不过在多姆的解释下，\x01",
            "大家似乎都理解了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "如果只有我一个人的话，\x01",
            "可能无法很好地说服他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_FED")

    label("loc_F9B")


    ChrTalk(    #48
        0xA,
        (
            "不过在这种情况下，\x01",
            "商品应该是卖不出去的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "我到现在为止\x01",
            "都干了些什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FED")

    Jump("loc_1639")

    label("loc_FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1112")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B3")

    ChrTalk(    #50
        0xA,
        (
            "昨晚在西街区\x01",
            "据说导力全停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "我记得前不久在蔡斯\x01",
            "也发生过类似的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        (
            "如果导力器不能用了的话\x01",
            "这店就要关门大吉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "我倾注在这座店里的\x01",
            "人生也算玩儿完了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_110F")

    label("loc_10B3")


    ChrTalk(    #54
        0xA,
        (
            "如果导力器不能用了的话\x01",
            "这店就要关门大吉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "我倾注在这座店里的\x01",
            "人生也算玩儿完了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110F")

    Jump("loc_1639")

    label("loc_1112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_111C")
    Jump("loc_1639")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_1126")
    Jump("loc_1639")

    label("loc_1126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_11D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 6)), scpexpr(EXPR_END)), "loc_119A")

    ChrTalk(    #56
        0xA,
        "……穿白色衣服的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "莫非，\x01",
            "就是你们以前带来过的那孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        "不，今天我没看见哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11D6")

    label("loc_119A")


    ChrTalk(    #59
        0xA,
        "……穿白色衣服的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        "不，应该说没来过店里吧。\x02",
    )

    CloseMessageWindow()

    label("loc_11D6")

    Jump("loc_1639")

    label("loc_11D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_121A")

    ChrTalk(    #61
        0xA,
        (
            "多姆昨天好像也\x01",
            "通宵修理商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        "真是个傻瓜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1639")

    label("loc_121A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1288")

    ChrTalk(    #63
        0xA,
        (
            "别看多姆那个样子，\x01",
            "他从小就很顽固……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "不过就算我们从小一起长大，\x01",
            "这次我也不能让着他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1639")

    label("loc_1288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_13C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1371")

    ChrTalk(    #65
        0xA,
        "……我和搭档多姆大吵了一架。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "最近那家伙整天就是修理修理的，\x01",
            "根本不过来我这边帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        (
            "如果顾客买新的\x01",
            "来替换坏了的东西，\x01",
            "店里的销售额就会上升。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "像他那么做的话，我就好像是\x01",
            "花钱养一个让我赔本的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_13C0")

    label("loc_1371")


    ChrTalk(    #69
        0xA,
        "我没做错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "……就算是工房，\x01",
            "也是一家店铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        "不赚钱就经营不下去。\x02",
    )

    CloseMessageWindow()

    label("loc_13C0")

    Jump("loc_1639")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_154F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F6")

    ChrTalk(    #72
        0xA,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x12F,
        (
            "#264F……这里是卖导力器的？\x02\x03",

            "比玲家的附近的店\x01",
            "货色更齐全呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xA, 0x12F, 400)
    Sleep(1000)

    ChrTalk(    #74
        0xA,
        (
            "小妹妹你莫非是\x01",
            "从外国来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "要不要买点利贝尔制的\x01",
            "导力器回去送人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12F,
        (
            "#260F这主意不错。\x01",
            "不过玲没带钱。\x02\x03",

            "等爸爸妈妈来接我时\x01",
            "我再过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        "嗯，我们等着你！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1646)
    Jump("loc_154C")

    label("loc_14F6")


    ChrTalk(    #78
        0xA,
        (
            "多姆那家伙昨晚修理\x01",
            "别人送来的东西到很晚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "就算急着修好，别人\x01",
            "也不会多加钱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154C")

    Jump("loc_1639")

    label("loc_154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E5")

    ChrTalk(    #80
        0xA,
        (
            "我的搭档多姆就算再忙\x01",
            "也不会拒绝修理的请求。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        (
            "明明卖出新产品比修理\x01",
            "来钱更快啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "我真希望多姆能学好\x01",
            "优先考虑利益啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1639")

    label("loc_15E5")


    ChrTalk(    #83
        0xA,
        (
            "……明明卖出新产品比修理\x01",
            "来钱更快啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "我真希望多姆能学好\x01",
            "优先考虑利益啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1639")

    TalkEnd(0xA)
    Return()

    # Function_4_393 end

    def Function_5_163D(): pass

    label("Function_5_163D")

    Call(0, 6)
    Return()

    # Function_5_163D end

    def Function_6_1642(): pass

    label("Function_6_1642")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1670")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1667")
    OP_A9(0xDA)
    Jump("loc_1669")

    label("loc_1667")

    OP_A9(0xC9)

    label("loc_1669")

    TalkEnd(0x8)
    Return()

    label("loc_1670")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1681")
    TalkEnd(0x8)
    Return()

    label("loc_1681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16DC")

    ChrTalk(    #85
        0x8,
        "和那个人在一起我就无所畏惧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "从前就没有导力器，\x01",
            "我们不也活得好好的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D28")

    label("loc_16DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_17B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1775")

    ChrTalk(    #87
        0x8,
        (
            "因为夫妻吵架，\x01",
            "我正准备离家出走，\x01",
            "他把我挽留下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "他因此终于\x01",
            "倾吐出了自己的心声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "原来他比我想象中的要\x01",
            "体贴人……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_17B2")

    label("loc_1775")


    ChrTalk(    #90
        0x8,
        (
            "说起来，吵架的时候\x01",
            "街上好像很吵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        "发生了什么呢？\x02",
    )

    CloseMessageWindow()

    label("loc_17B2")

    Jump("loc_1D28")

    label("loc_17B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_17BF")
    Jump("loc_1D28")

    label("loc_17BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_17C9")
    Jump("loc_1D28")

    label("loc_17C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1852")

    ChrTalk(    #92
        0x8,
        (
            "不论是夫妇还是别的关系，\x01",
            "有些话不说对方永远\x01",
            "不会知道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "一直沉默不语的话\x01",
            "就无法互相沟通了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "你不这么认为吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D28")

    label("loc_1852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_18D2")

    ChrTalk(    #95
        0x8,
        (
            "我们结婚\x01",
            "已经五年多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "可我先生无论是我发脾气\x01",
            "还是哭泣都不会过来问一句话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        "不知道他到底在想什么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D28")

    label("loc_18D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196E")

    ChrTalk(    #98
        0x8,
        (
            "我先生不仅沉默寡言，\x01",
            "还不愿意和人接触。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "今天好像也一直\x01",
            "在仓库里干活儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "我们要靠做买卖为生，\x01",
            "真希望他能再改进一点。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_19DE")

    label("loc_196E")


    ChrTalk(    #101
        0x8,
        (
            "就算沉默寡言改不了，\x01",
            "至少能变得更亲切一点也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "但是硬让他笑\x01",
            "也只像是在痉挛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        "我该怎么办才好？\x02",
    )

    CloseMessageWindow()

    label("loc_19DE")

    Jump("loc_1D28")

    label("loc_19E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1A3B")

    ChrTalk(    #104
        0x8,
        (
            "可能互不侵犯条约的签字仪式\x01",
            "临近了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "最近感觉城里似乎\x01",
            "挺有活力的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D28")

    label("loc_1A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BEC")

    ChrTalk(    #106
        0x8,
        "欢迎来到瓦伊斯武器商会！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0x8, 0x12F, 400)

    ChrTalk(    #107
        0x8,
        (
            "哎呀呀，\x01",
            "这小妹妹真可爱。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x8, 400)

    ChrTalk(    #108
        0x12F,
        (
            "#264F……莫非你是\x01",
            "在说玲？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "我要是也有一个\x01",
            "你这样的女儿就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        "怎么样？要不要当我的孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x12F,
        (
            "#267F玲有自己很喜欢的\x01",
            "爸爸和妈妈……\x02\x03",

            "#260F很遗憾，\x01",
            "不能当阿姨的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "哈哈，开玩笑啦。\x01",
            "我倒是想给你糖吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "不过不巧的是\x01",
            "这里只有武器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x12F,
        (
            "#261F呵呵，没关系的。\x01",
            "心领了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x164B)
    Jump("loc_1C5E")

    label("loc_1BEC")


    ChrTalk(    #116
        0x8,
        (
            "如果我有个女儿的话，就能\x01",
            "让她陪我买东西和聊天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "……我先生真的是沉默寡言，\x01",
            "至少有个孩子在我身边也好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5E")

    Jump("loc_1D28")

    label("loc_1C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_1CDA")

    ChrTalk(    #118
        0x8,
        "哎呀，你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "你是武术大会冠军队的\x01",
            "游击士小姐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "呵呵，欢迎欢迎。\x01",
            "你们能来真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D28")

    label("loc_1CDA")


    ChrTalk(    #121
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎来到瓦伊斯武器商会！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "这里有各种武器哟。\x01",
            "请慢慢选购。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D28")

    TalkEnd(0x8)
    Return()

    # Function_6_1642 end

    def Function_7_1D2C(): pass

    label("Function_7_1D2C")

    Call(0, 8)
    Return()

    # Function_7_1D2C end

    def Function_8_1D31(): pass

    label("Function_8_1D31")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1DD8")

    ChrTalk(    #123
        0xB,
        (
            "大家似乎都终于接受\x01",
            "导力器全部无法使用\x01",
            "这一事实了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "艾莉茜雅女王发布的\x01",
            "公告好像也有效果了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xB,
        (
            "总之现在只能一边努力\x01",
            "做力所能及的事一边忍耐了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_1DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1E28")

    ChrTalk(    #126
        0xB,
        (
            "自从吵架之后，\x01",
            "塞森都不理我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        (
            "不过我可没认为\x01",
            "自己做错了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_1E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_1E32")
    Jump("loc_220D")

    label("loc_1E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_1E3C")
    Jump("loc_220D")

    label("loc_1E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1ED6")

    ChrTalk(    #128
        0xB,
        (
            "塞森是和我从小一起长大的，\x01",
            "以前就经常吵架。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "那家伙就知道钱钱钱，\x01",
            "太沉溺在其中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xB,
        (
            "钱确实重要，\x01",
            "不过真正的工房不应该\x01",
            "只追求这个。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_1ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1F4D")

    ChrTalk(    #131
        0xB,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xB,
        "啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "……似乎在不知不觉中\x01",
            "睡着了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        "因为昨天睡得太晚了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_1F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA4")

    ChrTalk(    #135
        0xB,
        (
            "原来是……七耀石的\x01",
            "接合部分松了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        "换一下插座的话一定能……\x02",
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_1FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1FFE")

    ChrTalk(    #137
        0xB,
        (
            "我喜欢欣赏重要的东西\x01",
            "被修好时人们的笑容。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        (
            "那家伙为什么\x01",
            "就不理解呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220D")

    label("loc_1FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_21B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2163")

    ChrTalk(    #139
        0xB,
        (
            "……这边是这样的，\x01",
            "线路是那样的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0xB, 400)

    ChrTalk(    #140
        0x12F,
        "#264F大哥哥你在这里干什么？\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xB, 0x12F, 400)

    ChrTalk(    #141
        0xB,
        (
            "……我在修理赫穆特先生的\x01",
            "导力灯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xB,
        (
            "这好像是他珍藏了多年的,\x01",
            "充满回忆的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xB,
        "我一定要想办法帮他修好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x12F,
        (
            "#260F哦？\x01",
            "大哥哥你真了不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xB,
        "……咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        "啊，哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xB,
        (
            "哈哈，你这么说\x01",
            "我可不好意思了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_21B1")

    label("loc_2163")


    ChrTalk(    #148
        0xB,
        (
            "整天修理的话\x01",
            "塞森就会有意见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xB,
        (
            "不过我实在是不能\x01",
            "丢开修理的活儿不管。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B1")

    Jump("loc_220D")

    label("loc_21B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_220D")

    ChrTalk(    #150
        0xB,
        (
            "呀，欢迎。\x01",
            "这边是修理的接待窗口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "如果有导力产品损坏\x01",
            "可以拿来这里修理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220D")

    TalkEnd(0xB)
    Return()

    # Function_8_1D31 end

    def Function_9_2211(): pass

    label("Function_9_2211")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2245")

    ChrTalk(    #152
        0xFE,
        (
            "不管发生什么，\x01",
            "我都要保护妻子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_2245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_22D5")

    ChrTalk(    #153
        0xFE,
        (
            "我每天晚饭后\x01",
            "都要跟妻子聊天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "我虽然一直以来都\x01",
            "不太会表达自己的想法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "可是我的想法如果不\x01",
            "说出来的话\x01",
            "她就无法知道了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_22D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_22DF")
    Jump("loc_2564")

    label("loc_22DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_22E9")
    Jump("loc_2564")

    label("loc_22E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2349")

    ChrTalk(    #156
        0xFE,
        (
            "我想感谢妻子，\x01",
            "可我从来不擅长这些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "……那个……我究竟\x01",
            "该怎样做才好呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_2349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_239F")

    ChrTalk(    #158
        0xFE,
        (
            "这家店是我死去的父亲\x01",
            "留给我的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "我很感激帮我料理\x01",
            "店铺的妻子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_243F")

    ChrTalk(    #160
        0xFE,
        (
            "觉得肚子饿了\x01",
            "已经傍晚了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "可能是因为呆在这里\x01",
            "不了解外面的情况，\x01",
            "总觉得时间过得很快……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "虽然对我来说这种生活\x01",
            "很轻松、很自由……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_243F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_24B5")

    ChrTalk(    #163
        0xFE,
        "互不侵犯条约啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "不太了解详情，\x01",
            "不过和平当然好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "真希望我卖出去的武器\x01",
            "能用来消灭魔兽……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_24B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2516")

    ChrTalk(    #166
        0xFE,
        "……欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "想买武器的话就走上台阶\x01",
            "绕到店铺的正面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "我妻子应该在柜台的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2564")

    label("loc_2516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2564")

    ChrTalk(    #169
        0xFE,
        (
            "诞辰庆典结束后城市\x01",
            "也恢复了平静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "我喜欢这种程度的安静……\x02",
    )

    CloseMessageWindow()

    label("loc_2564")

    TalkEnd(0xFE)
    Return()

    # Function_9_2211 end

    SaveToFile()

Try(main)
