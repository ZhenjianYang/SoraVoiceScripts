from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M4112   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M4112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '赛雷斯托',                             # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT07/CH02891 ._CH',             # 00
        'ED6_DT29/CH14360 ._CH',             # 01
        'ED6_DT29/CH14360 ._CH',             # 02
        'ED6_DT29/CH14690 ._CH',             # 03
        'ED6_DT29/CH14691 ._CH',             # 04
        'ED6_DT29/CH14460 ._CH',             # 05
        'ED6_DT29/CH14461 ._CH',             # 06
        'ED6_DT29/CH14620 ._CH',             # 07
        'ED6_DT29/CH14621 ._CH',             # 08
        'ED6_DT29/CH14630 ._CH',             # 09
        'ED6_DT29/CH14631 ._CH',             # 0A
        'ED6_DT29/CH14010 ._CH',             # 0B
        'ED6_DT29/CH14011 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02891P._CP',             # 00
        'ED6_DT29/CH14360P._CP',             # 01
        'ED6_DT29/CH14360P._CP',             # 02
        'ED6_DT29/CH14690P._CP',             # 03
        'ED6_DT29/CH14691P._CP',             # 04
        'ED6_DT29/CH14460P._CP',             # 05
        'ED6_DT29/CH14461P._CP',             # 06
        'ED6_DT29/CH14620P._CP',             # 07
        'ED6_DT29/CH14621P._CP',             # 08
        'ED6_DT29/CH14630P._CP',             # 09
        'ED6_DT29/CH14631P._CP',             # 0A
        'ED6_DT29/CH14010P._CP',             # 0B
        'ED6_DT29/CH14011P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 23080,
        Z                   = 0,
        Y                   = -20490,
        Unknown_0C          = 180,
        Unknown_0E          = 1,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x258,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15070,
        Z                   = 0,
        Y                   = 3360,
        Unknown_0C          = 180,
        Unknown_0E          = 11,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34390,
        Z                   = 30,
        Y                   = 30910,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42360,
        Z                   = -10,
        Y                   = 8320,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x259,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 33760,
        Z                   = 0,
        Y                   = -44190,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 24020,
        TriggerZ            = 500,
        TriggerY            = 54480,
        TriggerRange        = 1500,
        ActorX              = 24020,
        ActorZ              = 4000,
        ActorY              = 54480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3540,
        TriggerZ            = 500,
        TriggerY            = -67980,
        TriggerRange        = 1500,
        ActorX              = 3540,
        ActorZ              = 4000,
        ActorY              = -67980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35940,
        TriggerZ            = 0,
        TriggerY            = -43500,
        TriggerRange        = 1000,
        ActorX              = 35940,
        ActorZ              = 1000,
        ActorY              = -43500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22A",          # 00, 0
        "Function_1_27E",          # 01, 1
        "Function_2_2D3",          # 02, 2
        "Function_3_1571",         # 03, 3
        "Function_4_1CF2",         # 04, 4
        "Function_5_2019",         # 05, 5
        "Function_6_2239",         # 06, 6
        "Function_7_2F24",         # 07, 7
        "Function_8_369F",         # 08, 8
        "Function_9_39CF",         # 09, 9
        "Function_10_3BF0",        # 0A, 10
        "Function_11_3D29",        # 0B, 11
        "Function_12_3E10",        # 0C, 12
        "Function_13_3EF7",        # 0D, 13
        "Function_14_400D",        # 0E, 14
    )


    def Function_0_22A(): pass

    label("Function_0_22A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_246"),
        (103, "loc_24D"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_246")

    Event(0, 11)
    Jump("loc_254")

    label("loc_24D")

    Event(0, 12)
    Jump("loc_254")

    label("loc_254")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_260"),
        (SWITCH_DEFAULT, "loc_268"),
    )


    label("loc_260")

    SetMapFlags(0x10000000)
    Jump("loc_268")

    label("loc_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_27D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 10)

    label("loc_27D")

    Return()

    # Function_0_22A end

    def Function_1_27E(): pass

    label("Function_1_27E")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDE8D8, 0x230065)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1")
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x8A, 0x0)

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE")
    OP_79(0x0, 0x2)
    OP_7B()

    label("loc_2AE")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB")
    OP_6F(0x3, 0)
    Jump("loc_2D2")

    label("loc_2CB")

    OP_6F(0x3, 60)

    label("loc_2D2")

    Return()

    # Function_1_27E end

    def Function_2_2D3(): pass

    label("Function_2_2D3")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp263_05.eff")
    LoadEffect(0x1, "map\\mp259_01.eff")
    Fade(500)
    OP_6D(24000, 250, 54700, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0x109, 23500, 0, 51000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    SetChrPos(0xEF, 24540, 0, 51000, 0)
    SetChrPos(0xF0, 22920, 0, 49820, 0)
    SetChrPos(0xF1, 25000, 0, 49890, 0)
    Jump("loc_44D")

    label("loc_392")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D6")
    SetChrPos(0xF0, 24540, 0, 51000, 0)
    SetChrPos(0xEF, 22920, 0, 49820, 0)
    SetChrPos(0xF1, 25000, 0, 49890, 0)
    Jump("loc_44D")

    label("loc_3D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41A")
    SetChrPos(0xF1, 24540, 0, 51000, 0)
    SetChrPos(0xEF, 22920, 0, 49820, 0)
    SetChrPos(0xF0, 25000, 0, 49890, 0)
    Jump("loc_44D")

    label("loc_41A")

    SetChrPos(0xEF, 24540, 0, 51000, 0)
    SetChrPos(0xF0, 22920, 0, 49820, 0)
    SetChrPos(0xF1, 25000, 0, 49890, 0)

    label("loc_44D")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 28000, 800, 50660, 270)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_474():

        label("loc_474")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_474")

    QueueWorkItem2(0x10, 3, lambda_474)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        (
            "\x07\x05石碑表面的表盘发出了光芒，\x01",
            "逐渐浮现出了一段文章。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W\x01",
            "#40W     前方为无色的学舍。\x01",
            "#500W\x01",
            "#40W       请与洁白之翼\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #2
        0x109,
        (
            "#1063F#6P这是……\x01",
            "是那家伙留下的信息吗。\x02\x03",

            "可是，『洁白之翼』所指的是……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #3
        (
            "\x07\x0C嗯……\x01",
            "应该是指我的后裔。\x07\x00\x02",
        )
    )

    Jump("loc_637")

    label("loc_637")

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67E")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6E5")

    label("loc_67E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A6")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6E5")

    label("loc_6A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6E5")

    label("loc_6CE")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6E5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_779")

    label("loc_712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_779")

    label("loc_73A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_762")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_779")

    label("loc_762")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_779")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A6")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_80D")

    label("loc_7A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CE")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_80D")

    label("loc_7CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F6")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_80D")

    label("loc_7F6")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_80D")

    Sleep(1000)
    Fade(500)
    OP_6D(27000, 0, 52130, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(44000, 0)
    OP_6E(268, 0)
    SetChrPos(0x109, 23500, 0, 51400, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A9")
    SetChrPos(0xEF, 24870, 0, 51190, 0)
    SetChrPos(0xF0, 23070, 0, 49780, 0)
    SetChrPos(0xF1, 24930, 0, 49800, 0)
    Jump("loc_964")

    label("loc_8A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED")
    SetChrPos(0xF0, 24870, 0, 51190, 0)
    SetChrPos(0xEF, 23000, 0, 49780, 0)
    SetChrPos(0xF1, 24930, 0, 49800, 0)
    Jump("loc_964")

    label("loc_8ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_931")
    SetChrPos(0xF1, 24870, 0, 51190, 0)
    SetChrPos(0xEF, 23070, 0, 49780, 0)
    SetChrPos(0xF0, 24930, 0, 49800, 0)
    Jump("loc_964")

    label("loc_931")

    SetChrPos(0xEF, 24870, 0, 51190, 0)
    SetChrPos(0xF0, 23070, 0, 49780, 0)
    SetChrPos(0xF1, 24930, 0, 49800, 0)

    label("loc_964")

    OP_0D()
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x10, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_9AA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9AA)
    Sleep(100)

    def lambda_9BD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9BD)
    Sleep(100)

    def lambda_9D0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_9D0)
    Sleep(100)
    OP_8C(0xF0, 90, 400)
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)

    def lambda_9F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xB4, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9F4)
    PlayEffect(0x1, 0x7, 0x10, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x10, 0x1)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #4
        0x109,
        "#1064F#6P啊……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A96")

    ChrTalk(    #5
        0x105,
        "#1164F#6P始祖大人……！？\x02",
    )

    CloseMessageWindow()

    label("loc_A96")


    ChrTalk(    #6
        0x10,
        (
            "\x07\x0C#1611F#11P呵呵……\x01",
            "这只是类似我的影子那样的存在罢了。\x02\x03",

            "我的本体现在还在『庭院』里面。\x02\x03",

            "#1616F既然已经取回了力量，\x01",
            "这点雕虫小技可难不倒我。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1078F#6P是、是吗。\x02\x03",

            "#1063F这样的话……\x01",
            "这石碑莫非是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "\x07\x0C#1615F#11P嗯嗯……\x01",
            "好像是通往『影之王』创立的领域的\x01",
            "类似『门』那样的东西。\x02\x03",

            "#1612F为了通过这个『门』，\x01",
            "身边非要伴有特定的人不可……\x02\x03",

            "这东西好像和放置在各地的『门』一样，\x01",
            "都遵从同一种开启规则。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE0")

    ChrTalk(    #9
        0x109,
        "#1063F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        (
            "#1162F#6P就是说，要继续前进的话，\x01",
            "必须有我同行对不对？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D")

    label("loc_CE0")


    ChrTalk(    #11
        0x109,
        (
            "#1065F#6P原来如此……\x02\x03",

            "#1063F想要继续前进的话，\x01",
            "必须要有科洛蒂娅公主\x01",
            "一起同行才可以对吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4D")


    ChrTalk(    #12
        0x10,
        (
            "\x07\x0C#1616F嗯，就是这样。\x02\x03",

            "#1610F恐怕，\x01",
            "其它的石碑也是遵守同样的规则……\x02\x03",

            "但是，它们暂时没有发光，\x01",
            "我们也只能先调查这个看看了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E1B")

    ChrTalk(    #13
        0x105,
        "#1383F#6P……我明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_E1B")


    ChrTalk(    #14
        0x109,
        "#1060F#6P明白。\x02",
    )

    CloseMessageWindow()

    label("loc_E37")


    ChrTalk(    #15
        0x10,
        (
            "\x07\x0C#1616F#11P那么，一路顺风。\x02\x03",

            "#1611F我会留在『庭院』，\x01",
            "如果你们有什么不清楚的事情，\x01",
            "可以随时向我询问。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x10, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x99, 0x0, 0x64)

    def lambda_F02():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F02)
    OP_82(0x7, 0x2)
    OP_82(0x0, 0x2)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    Sleep(1500)

    def lambda_F29():
        OP_6D(25500, 0, 52040, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F29)

    def lambda_F41():
        OP_67(0, 7100, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105E")

    def lambda_F67():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_F67)

    def lambda_F75():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_F75)

    def lambda_F83():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_F83)
    OP_8C(0x105, 270, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #16
        0x105,
        (
            "#1383F#11P凯文先生。\x01",
            "我已经做好准备了。\x02\x03",

            "#1162F要是打算继续前行的话，\x01",
            "随时都可以和我说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        (
            "#1075F#6P明白了。\x02\x03",

            "#1078F做好准备之后，\x01",
            "大家一起继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B04)
    Jump("loc_155A")

    label("loc_105E")


    def lambda_1064():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1064)
    Sleep(50)

    def lambda_1077():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1077)
    Sleep(50)

    def lambda_108A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_108A)
    Sleep(50)
    OP_8C(0xF1, 315, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #18
        0x109,
        (
            "#1075F#5P那么……\x02\x03",

            "#1060F看来我们要\x01",
            "暂时撤回据点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114A")

    ChrTalk(    #19
        0x10F,
        (
            "#1443F需要向科洛蒂娅公主\x01",
            "说明一下事情经过，\x01",
            "请她过来才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_114A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1199")

    ChrTalk(    #20
        0x101,
        (
            "#1006F要向科洛丝说明事情经过，\x01",
            "把她带过来才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_1199")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EC")

    ChrTalk(    #21
        0x102,
        (
            "#1500F要向科洛丝说明事情经过，\x01",
            "请她和我们一起来才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_11EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1232")

    ChrTalk(    #22
        0x10B,
        (
            "#210F要回去请公主殿下\x01",
            "和我们一起来才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_1232")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1280")

    ChrTalk(    #23
        0x110,
        (
            "#261F嘻嘻，那就回去和公主说一声，\x01",
            "把她带过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_1280")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D2")

    ChrTalk(    #24
        0x107,
        (
            "#560F要回去说明情况，\x01",
            "让科洛丝姐姐和我们一起来才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_12D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1329")

    ChrTalk(    #25
        0x10A,
        (
            "#1310F去和公主殿下说明一下情况，\x01",
            "请她和我们一起来一趟吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_1329")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1380")

    ChrTalk(    #26
        0x103,
        (
            "#1527F回去和公主殿下说明一下缘由，\x01",
            "让她和我们一起过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_1380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C6")

    ChrTalk(    #27
        0x106,
        (
            "#051F那就跟公主说一声，\x01",
            "让她过来一趟吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_13C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1412")

    ChrTalk(    #28
        0x108,
        (
            "#070F要和公主殿下说明一下原因，\x01",
            "请她过来一趟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_1412")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1462")

    ChrTalk(    #29
        0x10E,
        (
            "#176F……要和殿下说明一下，\x01",
            "然后请她到这里来才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_1462")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B3")

    ChrTalk(    #30
        0x104,
        (
            "#1540F呵，那就去和公主说明一下，\x01",
            "然后请她到这里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_14B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1507")

    ChrTalk(    #31
        0x10D,
        (
            "#277F要和公主殿下说明一下缘由，\x01",
            "然后请她来到这里才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155A")

    label("loc_1507")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155A")

    ChrTalk(    #32
        0x10C,
        (
            "#115F……要和公主殿下说明一下缘由，\x01",
            "然后请她来这里才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155A")

    OP_A2(0x2B03)
    OP_28(0x37, 0x1, 0x4)
    OP_28(0x37, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_2D3 end

    def Function_3_1571(): pass

    label("Function_3_1571")

    EventBegin(0x0)
    Fade(500)
    OP_6D(24000, 250, 54700, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0x109, 24010, 0, 51600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160A")
    SetChrPos(0xEF, 24000, 480, 53280, 0)
    SetChrPos(0xF0, 23250, 0, 50400, 0)
    SetChrPos(0xF1, 24860, 0, 50220, 0)
    Jump("loc_168F")

    label("loc_160A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164E")
    SetChrPos(0xF0, 24000, 480, 53280, 0)
    SetChrPos(0xEF, 23250, 0, 50400, 0)
    SetChrPos(0xF1, 24860, 0, 50220, 0)
    Jump("loc_168F")

    label("loc_164E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168F")
    SetChrPos(0xF1, 24000, 480, 53280, 0)
    SetChrPos(0xEF, 23250, 0, 50400, 0)
    SetChrPos(0xF0, 24860, 0, 50220, 0)

    label("loc_168F")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #33
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W\x01",
            "#40W     前方为无色的学舍。\x01",
            "#500W\x01",
            "#40W       请与洁白之翼\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1790")
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #34
        0x105,
        "#1162F#6P………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    label("loc_1790")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CEF")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "触摸表盘\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    Jump("loc_17D9")

    label("loc_17D9")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17FF"),
        (SWITCH_DEFAULT, "loc_1CDA"),
    )


    label("loc_17FF")

    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1877")

    def lambda_1865():
        OP_6D(24000, 10250, 54700, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1865)

    label("loc_1877")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DB")
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_18CA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18CA)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1920():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1920)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1976():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1976)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_19CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_19CC)
    Jump("loc_1CA0")

    label("loc_19DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3F")
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1A2E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1A2E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1A84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A84)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1ADA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1ADA)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1B30():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1B30)
    Jump("loc_1CA0")

    label("loc_1B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA0")
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1B92():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1B92)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1BE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1BE8)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1C3E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1C3E)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1C94():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1C94)

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB0")
    Sleep(1500)
    Jump("loc_1CB5")

    label("loc_1CB0")

    Sleep(500)

    label("loc_1CB5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x3)
    NewScene("ED6_DT21/U2500   ._SN", 130, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CEC")

    label("loc_1CDA")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CEC")

    label("loc_1CEC")

    Jump("loc_17A3")

    label("loc_1CEF")

    EventEnd(0x0)
    Return()

    # Function_3_1571 end

    def Function_4_1CF2(): pass

    label("Function_4_1CF2")

    EventBegin(0x0)
    Fade(500)
    OP_6D(24000, 250, 54700, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0x0, 24000, 480, 53280, 0)
    SetChrPos(0x1, 24010, 0, 51600, 0)
    SetChrPos(0x2, 23250, 0, 50400, 0)
    SetChrPos(0x3, 24860, 0, 50220, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #35
        "\x07\x05石碑上的表盘散发着光芒。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2016")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "触摸表盘\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    Jump("loc_1E0A")

    label("loc_1E0A")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E30"),
        (SWITCH_DEFAULT, "loc_2001"),
    )


    label("loc_1E30")

    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x8B, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1ECD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1ECD)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1F23():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1F23)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1F79():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1F79)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1FCF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1FCF)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/U2500   ._SN", 130, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2013")

    label("loc_2001")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2013")

    label("loc_2013")

    Jump("loc_1DD4")

    label("loc_2016")

    EventEnd(0x0)
    Return()

    # Function_4_1CF2 end

    def Function_5_2019(): pass

    label("Function_5_2019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2028")
    Call(0, 4)
    Return()

    label("loc_2028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_END)), "loc_2109")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2045")
    Call(0, 3)
    Return()

    label("loc_2045")

    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #36
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W\x01",
            "#40W     前方为无色的学舍。\x01",
            "#500W\x01",
            "#40W       请与洁白之翼\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_2238")

    label("loc_2109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D9")
    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #37
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W\x01",
            "#40W     前方为无色的学舍。\x01",
            "#500W\x01",
            "#40W       请与洁白之翼\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_2238")

    label("loc_21D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E9")
    Call(0, 2)
    Return()

    label("loc_21E9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #38
        "\x07\x05苍耀石的石碑上没有刻任何的东西。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_2238")

    Return()

    # Function_5_2019 end

    def Function_6_2239(): pass

    label("Function_6_2239")

    EventBegin(0x0)
    Fade(500)
    OP_6D(4300, 480, -68030, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(269000, 0)
    OP_6E(354, 0)
    SetChrPos(0x109, 6730, 0, -68020, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D2")
    SetChrPos(0xEF, 7950, 0, -68780, 270)
    SetChrPos(0xF0, 7900, 0, -67230, 270)
    SetChrPos(0xF1, 9000, 0, -67960, 270)
    Jump("loc_238D")

    label("loc_22D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2316")
    SetChrPos(0xF0, 7950, 0, -68780, 270)
    SetChrPos(0xEF, 7900, 0, -67230, 270)
    SetChrPos(0xF1, 9000, 0, -67960, 270)
    Jump("loc_238D")

    label("loc_2316")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235A")
    SetChrPos(0xF1, 7950, 0, -68780, 270)
    SetChrPos(0xEF, 7900, 0, -67230, 270)
    SetChrPos(0xF0, 9000, 0, -67960, 270)
    Jump("loc_238D")

    label("loc_235A")

    SetChrPos(0xEF, 7950, 0, -68780, 270)
    SetChrPos(0xF0, 7900, 0, -67230, 270)
    SetChrPos(0xF1, 9000, 0, -67960, 270)

    label("loc_238D")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #39
        (
            "\x07\x05石碑表面的表盘发出了光芒，\x01",
            "逐渐浮现出了一段文章。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #40
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W\x01",
            "#40W      前方为铁壁要塞。\x01",
            "#500W\x01",
            "#40W     请与剑圣的继承者\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25CB")
    OP_A2(0x2B17)

    ChrTalk(    #41
        0x109,
        "#1079F#6P这是……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #42
        0x109,
        (
            "#1060F#5P姑且不论『铁壁要塞』，\x01",
            "所指的人物应该是不言自明的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10C,
        (
            "#113F#6P可、可是……\x02\x03",

            "#115F……啊，也罢。\x01",
            "先不说是否有继承的资格，\x01",
            "看来这里只有我符合这个条件。\x02\x03",

            "#110F那就先触摸文字表盘试试看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F0D")

    label("loc_25CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AF3")

    ChrTalk(    #44
        0x109,
        "#1079F#6P这是……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #45
        0x109,
        (
            "#1060F#5P姑且不论『铁壁要塞』，\x01",
            "所谓『剑圣的继承者』\x01",
            "应该是不言自明的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2729")

    ChrTalk(    #46
        0x10E,
        (
            "#179F#6P是啊……\x02\x03",

            "#170F虽说我也曾承蒙准将的教导，\x01",
            "但是，说到继承者这点上，\x01",
            "其资格必然非理查德大人莫属了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_2729")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27A8")
    OP_A2(0x0)

    ChrTalk(    #47
        0x10A,
        (
            "#816F#6P是啊……\x02\x03",

            "说到继承者这一点，\x01",
            "除了理查德先生之外,\x01",
            "也没有其他人能够符合这个条件。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_27A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2823")
    OP_A2(0x1)

    ChrTalk(    #48
        0x101,
        (
            "#1012F#6P……嗯。\x02\x03",

            "#1006F从继承爸爸的剑技\x01",
            "这一点来说，\x01",
            "除了上校以外就没有其他人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_2823")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2895")
    OP_A2(0x2)

    ChrTalk(    #49
        0x102,
        (
            "#1505F#6P的确如此……\x02\x03",

            "#1500F继承父亲的剑技……\x01",
            "这指的一定就是理查德先生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_2895")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2931")

    ChrTalk(    #50
        0x103,
        (
            "#1526F#6P说的没错……\x02\x03",

            "#1520F我也只是在游击士方面受过老师的教导，\x01",
            "论到剑技的继承这一点，\x01",
            "我觉得只有理查德上校才有资格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_2931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2998")

    ChrTalk(    #51
        0x106,
        (
            "#053F#6P是啊……\x02\x03",

            "#051F继承那个大叔的剑技……\x01",
            "应该就是指理查德吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_2998")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A10")

    ChrTalk(    #52
        0x108,
        (
            "#573F#6P没错……\x02\x03",

            "#070F有资格继承卡西乌斯大人的剑技……\x01",
            "能想到的人也只有理查德上校了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A88")

    ChrTalk(    #53
        0x109,
        (
            "#1075F#5P果然如此吗……\x02\x03",

            "#1078F好吧，那我们就马上返回据点，\x01",
            "把理查德先生叫过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF0")

    label("loc_2A88")


    ChrTalk(    #54
        0x109,
        (
            "#1075F#5P果然是这样啊……\x02\x03",

            "#1078F好吧，那我们就马上返回据点，\x01",
            "把理查德先生叫过来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF0")

    Jump("loc_2D36")

    label("loc_2AF3")


    ChrTalk(    #55
        0x109,
        "#1079F#6P这是……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #56
        0x109,
        (
            "#1060F#5P姑且不论『铁壁要塞』，\x01",
            "所谓『剑圣的继承者』\x01",
            "应该是不言自明的吧。\x02\x03",

            "一定指的就是理查德先生了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BFD")

    ChrTalk(    #57
        0x10F,
        (
            "#1446F#6P原来如此……\x02\x03",

            "#1448F那么，我们先回据点，\x01",
            "把他叫来这里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D36")

    label("loc_2BFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C6B")

    ChrTalk(    #58
        0x105,
        (
            "#1383F#6P的确……\x02\x03",

            "#1382F那么，\x01",
            "我们最好先返回据点，\x01",
            "把理查德先生叫过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D36")

    label("loc_2C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CD0")

    ChrTalk(    #59
        0x10B,
        (
            "#210F#6P呼，是这样啊。\x02\x03",

            "#211F好吧，我们回据点去，\x01",
            "把他叫过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D36")

    label("loc_2CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D36")

    ChrTalk(    #60
        0x104,
        (
            "#1541F#6P呵呵，没错。\x02\x03",

            "#1540F那么，我们先回据点去，\x01",
            "把他叫来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F0D")

    ChrTalk(    #61
        0x110,
        (
            "#263F#6P嘻嘻……\x02\x03",

            "#1306F假如将这位哥哥比喻成葱的话，\x01",
            "那么那个上校就是洋葱了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0x109,
        (
            "#1064F#5P这、这个是什么比喻啊……？\x02\x03",

            "#1068F这不是我特意弄的发型，\x01",
            "自出娘胎头发就是这么竖起来的，\x01",
            "我都已经懒得管了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E7C")

    ChrTalk(    #63
        0x101,
        "#1016F#6P是、是吗……\x02",
    )

    CloseMessageWindow()

    label("loc_2E7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBB")

    ChrTalk(    #64
        0x10F,
        (
            "#1806F#6P呵呵……\x01",
            "以前就是这样的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBB")


    ChrTalk(    #65
        0x110,
        (
            "#261F#6P嘻嘻，是吗。\x02\x03",

            "#265F那么，\x01",
            "难道上校先生也是这个原因吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F0D")

    OP_A2(0x2B16)
    OP_28(0x39, 0x1, 0x2)
    OP_28(0x39, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_6_2239 end

    def Function_7_2F24(): pass

    label("Function_7_2F24")

    EventBegin(0x0)
    Fade(500)
    OP_6D(2670, 250, -68000, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(269000, 0)
    OP_6E(311, 0)
    SetChrPos(0x109, 6520, 0, -68050, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FBD")
    SetChrPos(0xEF, 4750, 480, -68000, 270)
    SetChrPos(0xF0, 7840, 0, -68700, 270)
    SetChrPos(0xF1, 7910, 0, -67330, 270)
    Jump("loc_3042")

    label("loc_2FBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3001")
    SetChrPos(0xF0, 4750, 480, -68000, 270)
    SetChrPos(0xEF, 7840, 0, -68700, 270)
    SetChrPos(0xF1, 7910, 0, -67330, 270)
    Jump("loc_3042")

    label("loc_3001")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3042")
    SetChrPos(0xF1, 4750, 480, -68000, 270)
    SetChrPos(0xEF, 7840, 0, -68700, 270)
    SetChrPos(0xF0, 7910, 0, -67330, 270)

    label("loc_3042")

    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #66
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W\x01",
            "#40W      前方为铁壁要塞。\x01",
            "#500W\x01",
            "#40W     请与剑圣的继承者\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3141")
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #67
        0x10C,
        "#112F#6P……………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    label("loc_3141")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3154")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_369C")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "触摸表盘\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    Jump("loc_318A")

    label("loc_318A")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31B0"),
        (SWITCH_DEFAULT, "loc_3687"),
    )


    label("loc_31B0")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3228")

    def lambda_3216():
        OP_6D(2670, 10000, -68000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3216)

    label("loc_3228")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_338C")
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_327B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_327B)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_32D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_32D1)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3327():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3327)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_337D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_337D)
    Jump("loc_3651")

    label("loc_338C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F0")
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_33DF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_33DF)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3435():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3435)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_348B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_348B)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_34E1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_34E1)
    Jump("loc_3651")

    label("loc_34F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3651")
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3543():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3543)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3599():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3599)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_35EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_35EF)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3645():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3645)

    label("loc_3651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3661")
    Sleep(1500)
    Jump("loc_3666")

    label("loc_3661")

    Sleep(500)

    label("loc_3666")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M3100   ._SN", 103, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3699")

    label("loc_3687")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3699")

    label("loc_3699")

    Jump("loc_3154")

    label("loc_369C")

    EventEnd(0x0)
    Return()

    # Function_7_2F24 end

    def Function_8_369F(): pass

    label("Function_8_369F")

    EventBegin(0x0)
    Fade(500)
    OP_6D(3970, 250, -67060, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2630, 0)
    OP_6C(314000, 0)
    OP_6E(310, 0)
    SetChrPos(0x0, 4940, 490, -68160, 270)
    SetChrPos(0x1, 6400, 0, -68310, 270)
    SetChrPos(0x2, 7810, 0, -69300, 270)
    SetChrPos(0x3, 7950, 0, -67840, 270)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #68
        "\x07\x05石碑上的表盘散发着光芒。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_378A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39CC")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "触摸表盘\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    Jump("loc_37C0")

    label("loc_37C0")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_37E6"),
        (SWITCH_DEFAULT, "loc_39B7"),
    )


    label("loc_37E6")

    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3883():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3883)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_38D9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_38D9)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_392F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_392F)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3985():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3985)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/M3100   ._SN", 103, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39C9")

    label("loc_39B7")

    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39C9")

    label("loc_39C9")

    Jump("loc_378A")

    label("loc_39CC")

    EventEnd(0x0)
    Return()

    # Function_8_369F end

    def Function_9_39CF(): pass

    label("Function_9_39CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_39DE")
    Call(0, 8)
    Return()

    label("loc_39DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_END)), "loc_3AC0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39FB")
    Call(0, 7)
    Return()

    label("loc_39FB")

    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #69
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W\x01",
            "#40W      前方为铁壁要塞。\x01",
            "#500W\x01",
            "#40W     请与剑圣的继承者\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_3BEF")

    label("loc_3AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B91")
    TalkBegin(0xFF)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #70
        (
            "\x07\x02#40W     『影之王』宣告──\x01",
            "#500W\x01",
            "#40W      前方为铁壁要塞。\x01",
            "#500W\x01",
            "#40W     请与剑圣的继承者\x01",
            "       一起触摸表盘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_3BEF")

    label("loc_3B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_3BA0")
    Call(0, 6)
    Return()

    label("loc_3BA0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #71
        "\x07\x05红耀石的石碑上没有刻任何的东西。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_3BEF")

    Return()

    # Function_9_39CF end

    def Function_10_3BF0(): pass

    label("Function_10_3BF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(4740, 5300, -68000, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(269000, 0)
    OP_6E(356, 0)

    def lambda_3C53():
        OP_6D(4000, 1750, -68000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3C53)

    def lambda_3C6B():
        OP_67(0, 5320, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3C6B)

    def lambda_3C83():
        OP_6B(2390, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3C83)

    def lambda_3C93():
        OP_6E(359, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3C93)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    def lambda_3CB7():
        OP_6B(2000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3CB7)
    OP_22(0xD7, 0x0, 0x64)
    Fade(1000)
    OP_72(0x401, 0x0)
    ExitThread()
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_0D()
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5600   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3BF0 end

    def Function_11_3D29(): pass

    label("Function_11_3D29")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 24070, 0, 51210, 180)
    SetChrPos(0x1, 24070, 0, 51210, 180)
    SetChrPos(0x2, 24070, 0, 51210, 180)
    SetChrPos(0x3, 24070, 0, 51210, 180)
    OP_69(0x0, 0x0)
    OP_6C(315000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 13)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_3D29 end

    def Function_12_3E10(): pass

    label("Function_12_3E10")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 6690, 0, -68020, 90)
    SetChrPos(0x1, 6690, 0, -68020, 90)
    SetChrPos(0x2, 6690, 0, -68020, 90)
    SetChrPos(0x3, 6690, 0, -68020, 90)
    OP_69(0x0, 0x0)
    OP_6C(315000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 13)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_3E10 end

    def Function_13_3EF7(): pass

    label("Function_13_3EF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F20")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F14():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F14)

    label("loc_3F20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F49")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F3D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3F3D)

    label("loc_3F49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F72")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F66():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3F66)

    label("loc_3F72")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F9B")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F8F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3F8F)

    label("loc_3F9B")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FC7")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3FC7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FDE")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3FDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FF5")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3FF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_400C")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_400C")

    Return()

    # Function_13_3EF7 end

    def Function_14_400D(): pass

    label("Function_14_400D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29D, 1)"), scpexpr(EXPR_END)), "loc_407F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        "\x07\x00得到了\x1F\x9D\x02\x07\x00。\x02",
    )

    Jump("loc_4064")

    label("loc_4064")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B9E)
    Jump("loc_40EB")

    label("loc_407F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #73
        (
            "宝箱里装有\x1F\x9D\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x9D\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_40CC")

    label("loc_40CC")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_40EB")

    Jump("loc_411F")

    label("loc_40EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #74
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_411F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_400D end

    SaveToFile()

Try(main)
