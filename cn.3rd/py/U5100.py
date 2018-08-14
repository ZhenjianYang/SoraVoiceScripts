from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U5100   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U5100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        '鼠人',                                 # 9
        '鼠人',                                 # 10
        '鼠人',                                 # 11
        '鼠人',                                 # 12
        '狼人',                                 # 13
        '狼人',                                 # 14
        '狼人',                                 # 15
        '女性的灵魂',                           # 16
        '卢·洛克尔地图',                       # 17
        '',                                     # 18
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
        'ED6_DT29/CH14540 ._CH',             # 00
        'ED6_DT29/CH14541 ._CH',             # 01
        'ED6_DT29/CH14740 ._CH',             # 02
        'ED6_DT29/CH14741 ._CH',             # 03
        'ED6_DT29/CH14742 ._CH',             # 04
        'ED6_DT26/CH20622 ._CH',             # 05
        'ED6_DT07/CH02890 ._CH',             # 06
        'ED6_DT26/CH20653 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH14540P._CP',             # 00
        'ED6_DT29/CH14541P._CP',             # 01
        'ED6_DT29/CH14740P._CP',             # 02
        'ED6_DT29/CH14741P._CP',             # 03
        'ED6_DT29/CH14742P._CP',             # 04
        'ED6_DT26/CH20622P._CP',             # 05
        'ED6_DT07/CH02890P._CP',             # 06
        'ED6_DT26/CH20653P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -3550,
        TriggerZ            = 0,
        TriggerY            = -3000,
        TriggerRange        = 800,
        ActorX              = -4250,
        ActorZ              = 1000,
        ActorY              = -3000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_261",          # 01, 1
        "Function_2_281",          # 02, 2
        "Function_3_28A",          # 03, 3
        "Function_4_23F6",         # 04, 4
        "Function_5_2428",         # 05, 5
        "Function_6_2455",         # 06, 6
        "Function_7_2482",         # 07, 7
        "Function_8_24B4",         # 08, 8
        "Function_9_2522",         # 09, 9
        "Function_10_258B",        # 0A, 10
        "Function_11_25F9",        # 0B, 11
        "Function_12_2643",        # 0C, 12
        "Function_13_268D",        # 0D, 13
        "Function_14_26D7",        # 0E, 14
        "Function_15_2721",        # 0F, 15
        "Function_16_2758",        # 10, 16
        "Function_17_278F",        # 11, 17
        "Function_18_27C6",        # 12, 18
        "Function_19_27E2",        # 13, 19
        "Function_20_2803",        # 14, 20
        "Function_21_281F",        # 15, 21
        "Function_22_2840",        # 16, 22
        "Function_23_3C54",        # 17, 23
        "Function_24_3CB0",        # 18, 24
        "Function_25_3D11",        # 19, 25
        "Function_26_3DB8",        # 1A, 26
        "Function_27_3EEB",        # 1B, 27
        "Function_28_44AF",        # 1C, 28
        "Function_29_459E",        # 1D, 29
        "Function_30_465A",        # 1E, 30
        "Function_31_4770",        # 1F, 31
        "Function_32_47BE",        # 20, 32
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_246"),
        (SWITCH_DEFAULT, "loc_24D"),
    )


    label("loc_246")

    Event(0, 28)
    Jump("loc_24D")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_260")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_260")

    Return()

    # Function_0_22E end

    def Function_1_261(): pass

    label("Function_1_261")

    OP_16(0x2, 0xFA0, 0xFFFE13D0, 0xFFFDE4F0, 0x23006F)
    OP_1B(0x4, 0x0, 0x1D)
    OP_1B(0x0, 0x0, 0x1B)
    OP_82(0x81, 0x0)
    Return()

    # Function_1_261 end

    def Function_2_281(): pass

    label("Function_2_281")

    Call(0, 3)
    Call(0, 22)
    Return()

    # Function_2_281 end

    def Function_3_28A(): pass

    label("Function_3_28A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp204_02.eff")
    OP_E0(265, 0x48, 0x2)
    OP_E0(258, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(241, 0x4B, 0x2)
    SetChrPos(0x109, 7450, 0, 5430, 180)
    SetChrPos(0x102, 6540, 0, 6210, 180)
    SetChrPos(0xF0, 8230, 0, 6140, 180)
    SetChrPos(0xF1, 7310, 0, 7160, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(20430, 2600, -5010, 0)
    OP_67(0, 9920, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(237, 0)

    def lambda_370():
        OP_6D(9200, 2600, 4600, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_370)

    def lambda_388():
        OP_67(0, 9490, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_388)

    def lambda_3A0():
        OP_6B(3800, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3A0)

    def lambda_3B0():
        OP_6E(237, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3B0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)

    def lambda_3CF():
        OP_6D(9200, 2600, 4600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3CF)

    def lambda_3E7():
        OP_67(0, 7580, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3E7)

    def lambda_3FF():
        OP_6B(2440, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3FF)

    def lambda_40F():
        OP_6E(285, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_40F)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(300)

    def lambda_468():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_468)

    def lambda_47A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_47A)

    def lambda_48C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_48C)

    def lambda_49E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_49E)
    WaitChrThread(0x109, 0x0)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_53C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_564")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_564")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_57B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A8")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60F")

    label("loc_5A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60F")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_60F")

    label("loc_5F8")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_60F")

    Sleep(1000)

    ChrTalk(    #0
        0x102,
        "#1504F#5P这里是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1067F#6P哎……\x01",
            "我好像没见过这个地方。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AA")

    label("loc_692")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AA")

    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x108, 0, 400)
    Sleep(300)

    ChrTalk(    #2
        0x108,
        "#073F#6P哦，这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B7")

    label("loc_6F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_783")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_737")

    label("loc_71F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_737")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_737")

    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10D, 0, 400)
    Sleep(300)

    ChrTalk(    #3
        0x10D,
        "#273F#6P哦，那是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B7")

    label("loc_783")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_810")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C4")

    label("loc_7AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C4")

    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10E, 0, 400)
    Sleep(300)

    ChrTalk(    #4
        0x10E,
        "#173F#6P哦，那是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B7")

    label("loc_810")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_839")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_851")

    label("loc_839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_851")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_851")

    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x105, 0, 400)
    Sleep(300)

    ChrTalk(    #5
        0x105,
        "#1164F#6P那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B7")

    label("loc_89C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8DD")

    label("loc_8C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DD")

    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10B, 0, 400)
    Sleep(300)

    ChrTalk(    #6
        0x10B,
        "#213F#6P哇……看那个！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B7")

    label("loc_92B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_954")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96C")

    label("loc_954")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96C")

    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 0, 400)
    Sleep(300)

    ChrTalk(    #7
        0x107,
        "#560F#6P哇……看那个！\x02",
    )

    CloseMessageWindow()

    label("loc_9B7")

    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15")
    OP_62(0xF1, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_A6D")

    label("loc_A15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A38")
    OP_62(0xF1, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_A6D")

    label("loc_A38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5B")
    OP_62(0xF1, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_A6D")

    label("loc_A5B")

    OP_62(0xF1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_A6D")

    Jump("loc_AF8")

    label("loc_A70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA0")
    OP_62(0xF0, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_AF8")

    label("loc_AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC3")
    OP_62(0xF0, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_AF8")

    label("loc_AC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE6")
    OP_62(0xF0, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_AF8")

    label("loc_AE6")

    OP_62(0xF0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_AF8")

    Sleep(1000)

    def lambda_B03():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B03)
    Sleep(100)

    def lambda_B16():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B16)
    Sleep(100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3A")
    OP_8C(0xF1, 0, 400)
    Jump("loc_B4E")

    label("loc_B3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4E")
    OP_8C(0xF0, 0, 400)

    label("loc_B4E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0xDD)
    Fade(1000)
    OP_6D(3630, 0, 46640, 0)
    OP_67(0, 11020, -10000, 0)
    OP_6B(4030, 0)
    OP_6C(315000, 0)
    OP_6E(312, 0)
    OP_0D()
    Sleep(500)

    def lambda_BA8():
        OP_6D(9200, 2600, 5600, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BA8)

    def lambda_BC0():
        OP_67(0, 9180, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BC0)

    def lambda_BD8():
        OP_6B(4930, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BD8)

    def lambda_BE8():
        OP_6E(332, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BE8)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(7130, 0, 7000, 0)
    OP_67(0, 8180, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7D")

    ChrTalk(    #8
        0x104,
        "#1541F#6P呵……真是绝景啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D9E")

    label("loc_C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB1")

    ChrTalk(    #9
        0x107,
        "#560F#6P哇……好漂亮！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D9E")

    label("loc_CB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CEA")

    ChrTalk(    #10
        0x10B,
        (
            "#210F#6P呼。\x01",
            "这景色还不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9E")

    label("loc_CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D23")

    ChrTalk(    #11
        0x105,
        "#1382F#6P真是美丽的景色……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D9E")

    label("loc_D23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D62")

    ChrTalk(    #12
        0x10E,
        (
            "#171F#6P这……\x01",
            "还真是不错的景象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9E")

    label("loc_D62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9E")

    ChrTalk(    #13
        0x10D,
        (
            "#277F#6P嗯……\x01",
            "还真是不错的景象。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9E")


    ChrTalk(    #14
        0x109,
        (
            "#1078F#6P嘿……\x01",
            "没想到来到了这样的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#1500F#5P难道也和王都一样\x01",
            "是『影之国』中\x01",
            "再现出来的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1065F#6P啊，这种可能性很高。\x02\x03",

            "#1067F可是……\x01",
            "这里是利贝尔的某个地方吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF2")

    ChrTalk(    #17
        0x102,
        (
            "#1505F#5P不……\x01",
            "我也没有见过这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        (
            "#1163F#6P古罗尼连峰？\x01",
            "不对，而且这里的空气……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCF")

    label("loc_EF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6C")

    ChrTalk(    #19
        0x102,
        (
            "#1505F#5P不……\x01",
            "我也没有见过这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10E,
        (
            "#178F#6P古罗尼连峰？\x01",
            "不对，而且这里的空气……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCF")

    label("loc_F6C")


    ChrTalk(    #21
        0x102,
        (
            "#1505F#5P不……\x01",
            "我也没有见过这里。\x02\x03",

            "#1503F古罗尼连峰？\x01",
            "不对，而且这里的空气……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCF")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #22
        0x102,
        "#1504F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_1019():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1019)
    Sleep(100)

    def lambda_102C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_102C)
    Sleep(100)
    OP_8C(0xF0, 270, 400)

    ChrTalk(    #23
        0x109,
        "#1079F#6P怎么……？\x02",
    )

    CloseMessageWindow()

    def lambda_1066():
        OP_6D(-860, 9050, 5560, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1066)

    def lambda_107E():
        OP_67(0, 5810, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_107E)

    def lambda_1096():
        OP_6B(3280, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1096)

    def lambda_10A6():
        OP_6C(291000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10A6)

    def lambda_10B6():
        OP_6E(253, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10B6)
    Sleep(500)

    def lambda_10CB():
        OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0x1676, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_10CB)
    Sleep(200)

    def lambda_10EB():
        OP_8E(0xFE, 0xF0, 0x0, 0x113A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_10EB)
    Sleep(200)

    def lambda_110B():
        OP_8E(0xFE, 0x26C, 0x0, 0x19AA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_110B)
    Sleep(200)

    def lambda_112B():
        OP_8E(0xFE, 0x776, 0x0, 0x1450, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_112B)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x3)
    WaitChrThread(0x109, 0x3)
    WaitChrThread(0xF1, 0x3)
    WaitChrThread(0xF0, 0x3)

    ChrTalk(    #24
        0x109,
        (
            "#1064F#5P哎……\x01",
            "游击士协会的纹章……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1505F#5P也许……\x01",
            "这里是利贝尔之外吧。\x02\x03",

            "#1502F据我所知，\x01",
            "这样的协会设施\x01",
            "在国内是不存在的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_126F")

    ChrTalk(    #26
        0x108,
        (
            "#074F#11P嗯……\x01",
            "的确，我也没见过呢。\x02\x03",

            "#072F就算是共和国，\x01",
            "也应该没有这样的设施。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1405")

    label("loc_126F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C2")

    ChrTalk(    #27
        0x10D,
        (
            "#270F#11P唔，\x01",
            "那就是说利贝尔以外的场所\x01",
            "也被再现了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1405")

    label("loc_12C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1310")

    ChrTalk(    #28
        0x10B,
        (
            "#212F#11P这么说，\x01",
            "利贝尔以外的场所也被复制了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1405")

    label("loc_1310")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1364")

    ChrTalk(    #29
        0x104,
        (
            "#1545F#11P呼，\x01",
            "那就是说利贝尔以外的场所\x01",
            "也被再现了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1405")

    label("loc_1364")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(    #30
        0x107,
        (
            "#065F#11P那、那就是说\x01",
            "利贝尔以外的场所\x01",
            "也被再现了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1405")

    label("loc_13B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1405")

    ChrTalk(    #31
        0x10E,
        (
            "#178F#11P这么说……\x01",
            "利贝尔以外的场所\x01",
            "也被再现了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1405")

    Sleep(300)
    Fade(500)
    OP_6D(-1200, 0, 7120, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(315000, 0)
    OP_6E(269, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #32
        0x109,
        (
            "#1078F#5P什么啊……\x01",
            "这里不就有答案吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14AE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14AE)
    Sleep(100)

    def lambda_14C1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_14C1)
    Sleep(100)
    OP_8C(0xF0, 180, 400)

    ChrTalk(    #33
        0x102,
        "#1504F#11P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4650, 0, -980, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(315000, 0)
    OP_6E(265, 0)
    OP_43(0x109, 0x0, 0x0, 0x12)
    OP_43(0x102, 0x0, 0x0, 0x13)
    OP_43(0xF0, 0x0, 0x0, 0x14)
    OP_43(0xF1, 0x0, 0x0, 0x15)

    def lambda_155B():
        OP_6D(-3590, 0, -2410, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_155B)

    def lambda_1573():
        OP_67(0, 7400, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1573)

    def lambda_158B():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_158B)

    def lambda_159B():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_159B)

    def lambda_15AB():
        OP_6E(248, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_15AB)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x102, 0x0)
    Sleep(500)

    ChrTalk(    #34
        0x102,
        (
            "#1504F#12P『游击士协会\x01",
            "  卢·洛克尔训练场』……\x02\x03",

            "难不成这里是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1060F#6P我记得这不是\x01",
            "艾丝蒂尔到国外训练的地方吗？\x02\x03",

            "和亚妮拉丝一起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1505F#12P嗯……是位于列曼自治州的\x01",
            "游击士协会训练场。\x02\x03",

            "#1503F我只是听她提起过，\x01",
            "并没有亲自来过这里……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1776")

    ChrTalk(    #37
        0x108,
        (
            "#070F#6P嗯……\x01",
            "这就是那个卢·洛克尔吗。\x02\x03",

            "我虽然没有在这里训练过，\x01",
            "不过在协会内部可是非常有名的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1776")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17DD")

    ChrTalk(    #38
        0x104,
        (
            "#1542F#6P……不过真奇怪。\x02\x03",

            "列曼自治州离利贝尔\x01",
            "应该有相当远的距离。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_17DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1844")

    ChrTalk(    #39
        0x105,
        (
            "#1163F#6P真不可思议……\x02\x03",

            "列曼自治州离利贝尔\x01",
            "明明有那么远的距离……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_1844")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B1")

    ChrTalk(    #40
        0x10D,
        (
            "#272F#6P可是真弄不明白……\x02\x03",

            "#270F列曼自治州离利贝尔\x01",
            "应该有相当远的距离。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_18B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1910")
    OP_A2(0x0)

    ChrTalk(    #41
        0x10B,
        (
            "#212F#6P啊……可是……\x02\x03",

            "列曼自治州离利贝尔\x01",
            "不是很远吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_1910")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1979")

    ChrTalk(    #42
        0x10E,
        (
            "#176F#6P嗯……真奇怪。\x02\x03",

            "#178F说起列曼自治州，\x01",
            "离利贝尔可是相当远的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_1979")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19FA")
    OP_A2(0x3)

    ChrTalk(    #43
        0x107,
        (
            "#064F#6P列曼自治州\x01",
            "不就是爷爷曾经\x01",
            "旅行到过的地方吗……\x02\x03",

            "#065F咦，可是，\x01",
            "应该是很远的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A95")

    ChrTalk(    #44
        0x109,
        (
            "#1063F#5P没错，\x01",
            "比起埃雷波尼亚和卡尔瓦德，\x01",
            "这里距离利贝尔要远得多。\x02\x03",

            "#1065F为什么这样的地方\x01",
            "会被再现呢？\x01",
            "真是无法理解……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B20")

    label("loc_1A95")


    ChrTalk(    #45
        0x109,
        (
            "#1063F#5P嗯，\x01",
            "比起埃雷波尼亚和卡尔瓦德，\x01",
            "这里距离利贝尔要远得多。\x02\x03",

            "#1065F为什么这样的地方\x01",
            "会被再现呢？\x01",
            "真是无法理解……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B20")

    OP_A3(0x0)
    OP_A3(0x3)
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #46
        0x102,
        (
            "#1505F#11P如果是敌人的安排，\x01",
            "那一定有特殊的用意才对……\x02\x03",

            "#1500F你是这个意思吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #47
        0x109,
        "#1060F#6P呵，你理解得这么快就好办了。\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x194, 0x0, 0x64)
    Sleep(150)
    OP_22(0x194, 0x0, 0x64)
    Sleep(500)
    OP_22(0x193, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C56")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CBD")

    label("loc_1C56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CBD")

    label("loc_1C7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA6")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CBD")

    label("loc_1CA6")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1CBD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEA")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D51")

    label("loc_1CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D12")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D51")

    label("loc_1D12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D51")

    label("loc_1D3A")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1D51")

    Sleep(1000)

    def lambda_1D5C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D5C)
    Sleep(50)

    def lambda_1D6F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D6F)
    Sleep(50)

    def lambda_1D82():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1D82)
    Sleep(50)
    OP_8C(0xF0, 180, 400)
    OP_1D(0x97)
    Sleep(500)

    ChrTalk(    #48
        0x102,
        "#1502F#11P刚才的是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1063F#5P啊啊……\x01",
            "这么快就出来迎接了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    ClearMapFlags(0x10)
    OP_6D(1130, 1300, -8000, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(8150, 0)
    OP_6C(212000, 0)
    OP_6E(138, 0)

    def lambda_1E47():
        OP_6D(-330, 0, -11660, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1E47)
    SetChrPos(0x109, -1520, 0, -4240, 180)
    SetChrPos(0x102, -1320, 0, -2650, 180)
    SetChrPos(0xF0, -80, 0, -4390, 180)
    SetChrPos(0xF1, 190, 0, -2460, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -2780, 0, -27580, 0)
    SetChrPos(0x11, -1780, 0, -26660, 0)
    SetChrPos(0x12, 450, 0, -27500, 0)
    OP_43(0x10, 0x0, 0x0, 0xB)
    OP_43(0x12, 0x0, 0x0, 0xD)
    OP_43(0x11, 0x0, 0x0, 0xC)
    Sleep(500)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 7060, 4250, -18070, 315)
    SetChrPos(0x15, 7770, 4250, -16870, 315)
    SetChrPos(0x16, 8900, 4250, -17550, 315)
    OP_43(0x14, 0x0, 0x0, 0xF)
    Sleep(100)
    OP_43(0x15, 0x0, 0x0, 0x10)
    Sleep(100)
    OP_43(0x16, 0x0, 0x0, 0x11)
    WaitChrThread(0x109, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FBF")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2026")

    label("loc_1FBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE7")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2026")

    label("loc_1FE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200F")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2026")

    label("loc_200F")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2026")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2053")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20BA")

    label("loc_2053")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_207B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20BA")

    label("loc_207B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A3")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20BA")

    label("loc_20A3")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_20BA")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20F3")

    ChrTalk(    #50
        0x107,
        "#065F#5P哇、哇啊啊！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_218A")

    label("loc_20F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2126")

    ChrTalk(    #51
        0x105,
        "#1164F#5P这、这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_218A")

    label("loc_2126")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_215E")

    ChrTalk(    #52
        0x10B,
        "#216F#5P什、什、什么啊！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_218A")

    label("loc_215E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218A")

    ChrTalk(    #53
        0x104,
        "#1540F#5P哎呀……\x02",
    )

    CloseMessageWindow()

    label("loc_218A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C0")

    ChrTalk(    #54
        0x10D,
        "#277F#5P哼……出现了吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2221")

    label("loc_21C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21F2")

    ChrTalk(    #55
        0x10E,
        "#178F#5P……来了吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2221")

    label("loc_21F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2221")

    ChrTalk(    #56
        0x108,
        "#072F#5P出来了吗……\x02",
    )

    CloseMessageWindow()

    label("loc_2221")

    Sleep(150)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 8)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x102, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 10)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x102,
        (
            "#1502F#5P带武装的野兽──\x01",
            "不，该说是『兽人』……\x02\x03",

            "『接下来是兽之道』，\x01",
            "指的就是这个吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x109,
        (
            "#1065F#5P啊，看起来没错。\x02\x03",

            "#1069F这么一大群强壮的家伙……\x01",
            "我们努力把它们赶走吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x10, 0x0, 0x0, 0x4)
    OP_43(0x11, 0x0, 0x0, 0x5)
    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_43(0x14, 0x0, 0x0, 0x8)
    OP_43(0x15, 0x0, 0x0, 0x9)
    OP_43(0x16, 0x0, 0x0, 0xA)

    def lambda_2389():
        OP_6D(-370, 0, -6510, 600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2389)

    def lambda_23A1():
        OP_67(0, 7770, -10000, 600)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_23A1)

    def lambda_23B9():
        OP_6B(4200, 600)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_23B9)

    def lambda_23C9():
        OP_6C(213000, 600)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_23C9)

    def lambda_23D9():
        OP_6E(169, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23D9)
    WaitChrThread(0x109, 0x0)
    Battle(0x1A2, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_28A end

    def Function_4_23F6(): pass

    label("Function_4_23F6")

    Sleep(10)

    def lambda_2401():

        label("loc_2401")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_2401")

    QueueWorkItem2(0xFE, 3, lambda_2401)
    SetChrChipByIndex(0xFE, 1)
    OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1B58, 0x0)
    Return()

    # Function_4_23F6 end

    def Function_5_2428(): pass

    label("Function_5_2428")


    def lambda_242E():

        label("loc_242E")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_242E")

    QueueWorkItem2(0xFE, 3, lambda_242E)
    SetChrChipByIndex(0xFE, 1)
    OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1B58, 0x0)
    Return()

    # Function_5_2428 end

    def Function_6_2455(): pass

    label("Function_6_2455")


    def lambda_245B():

        label("loc_245B")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_245B")

    QueueWorkItem2(0xFE, 3, lambda_245B)
    SetChrChipByIndex(0xFE, 1)
    OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1B58, 0x0)
    Return()

    # Function_6_2455 end

    def Function_7_2482(): pass

    label("Function_7_2482")

    Sleep(5)

    def lambda_248D():

        label("loc_248D")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_248D")

    QueueWorkItem2(0xFE, 3, lambda_248D)
    SetChrChipByIndex(0xFE, 1)
    OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1B58, 0x0)
    Return()

    # Function_7_2482 end

    def Function_8_24B4(): pass

    label("Function_8_24B4")

    Sleep(10)

    def lambda_24BF():

        label("loc_24BF")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_24BF")

    QueueWorkItem2(0xFE, 3, lambda_24BF)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x12FC, 0xF64, 0xFFFFD274, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 4)

    def lambda_24F4():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_24F4)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_2509():
        OP_96(0xFE, 0xC8, 0x0, 0xFFFFEA2A, 0x708, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2509)
    Return()

    # Function_8_24B4 end

    def Function_9_2522(): pass

    label("Function_9_2522")


    def lambda_2528():

        label("loc_2528")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_2528")

    QueueWorkItem2(0xFE, 3, lambda_2528)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x168A, 0xF64, 0xFFFFD670, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 4)

    def lambda_255D():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_255D)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_2572():
        OP_96(0xFE, 0x21C, 0x0, 0xFFFFEC1E, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2572)
    Return()

    # Function_9_2522 end

    def Function_10_258B(): pass

    label("Function_10_258B")

    Sleep(15)

    def lambda_2596():

        label("loc_2596")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_2596")

    QueueWorkItem2(0xFE, 3, lambda_2596)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x1982, 0xF64, 0xFFFFD42C, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 4)

    def lambda_25CB():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_25CB)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_25E0():
        OP_96(0xFE, 0x3FC, 0x0, 0xFFFFF3EE, 0x898, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25E0)
    Return()

    # Function_10_258B end

    def Function_11_25F9(): pass

    label("Function_11_25F9")

    Sleep(20)

    def lambda_2604():

        label("loc_2604")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_2604")

    QueueWorkItem2(0xFE, 3, lambda_2604)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0xFFFFF95C, 0x0, 0xFFFFD49A, 0x1770, 0x0)

    def lambda_2630():

        label("loc_2630")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2630")

    QueueWorkItem2(0xFE, 3, lambda_2630)
    SetChrChipByIndex(0xFE, 0)
    Return()

    # Function_11_25F9 end

    def Function_12_2643(): pass

    label("Function_12_2643")

    Sleep(35)

    def lambda_264E():

        label("loc_264E")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_264E")

    QueueWorkItem2(0xFE, 3, lambda_264E)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0xFFFFFF2E, 0x0, 0xFFFFD81E, 0x1770, 0x0)

    def lambda_267A():

        label("loc_267A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_267A")

    QueueWorkItem2(0xFE, 3, lambda_267A)
    SetChrChipByIndex(0xFE, 0)
    Return()

    # Function_12_2643 end

    def Function_13_268D(): pass

    label("Function_13_268D")

    Sleep(45)

    def lambda_2698():

        label("loc_2698")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_2698")

    QueueWorkItem2(0xFE, 3, lambda_2698)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0x424, 0x0, 0xFFFFD63E, 0x1770, 0x0)

    def lambda_26C4():

        label("loc_26C4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_26C4")

    QueueWorkItem2(0xFE, 3, lambda_26C4)
    SetChrChipByIndex(0xFE, 0)
    Return()

    # Function_13_268D end

    def Function_14_26D7(): pass

    label("Function_14_26D7")

    Sleep(15)

    def lambda_26E2():

        label("loc_26E2")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_26E2")

    QueueWorkItem2(0xFE, 3, lambda_26E2)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0x5BE, 0x0, 0xFFFFD238, 0x1770, 0x0)

    def lambda_270E():

        label("loc_270E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_270E")

    QueueWorkItem2(0xFE, 3, lambda_270E)
    SetChrChipByIndex(0xFE, 0)
    Return()

    # Function_14_26D7 end

    def Function_15_2721(): pass

    label("Function_15_2721")

    Sleep(300)

    def lambda_272C():

        label("loc_272C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_272C")

    QueueWorkItem2(0xFE, 3, lambda_272C)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x14AA, 0x109A, 0xFFFFCDF6, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_15_2721 end

    def Function_16_2758(): pass

    label("Function_16_2758")

    Sleep(200)

    def lambda_2763():

        label("loc_2763")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2763")

    QueueWorkItem2(0xFE, 3, lambda_2763)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x1978, 0x109A, 0xFFFFD45E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_16_2758 end

    def Function_17_278F(): pass

    label("Function_17_278F")

    Sleep(400)

    def lambda_279A():

        label("loc_279A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_279A")

    QueueWorkItem2(0xFE, 3, lambda_279A)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0x1D60, 0x109A, 0xFFFFCEFA, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_17_278F end

    def Function_18_27C6(): pass

    label("Function_18_27C6")

    OP_8E(0xFE, 0xFFFFF790, 0x0, 0xFFFFEEA8, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_18_27C6 end

    def Function_19_27E2(): pass

    label("Function_19_27E2")

    Sleep(200)
    OP_8E(0xFE, 0xFFFFF704, 0x0, 0xFFFFF48E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_19_27E2 end

    def Function_20_2803(): pass

    label("Function_20_2803")

    OP_8E(0xFE, 0xFFFFFE5C, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_2803 end

    def Function_21_281F(): pass

    label("Function_21_281F")

    Sleep(200)
    OP_8E(0xFE, 0xFFFFFDDA, 0x0, 0xFFFFF4E8, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_21_281F end

    def Function_22_2840(): pass

    label("Function_22_2840")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x1)
    OP_E0(265, 0x48, 0x2)
    OP_E0(258, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(241, 0x4B, 0x2)
    SetChrPos(0x109, -1760, 0, -4430, 180)
    SetChrPos(0x102, -2070, 0, -2700, 180)
    SetChrPos(0xF0, -400, 0, -4370, 135)
    SetChrPos(0xF1, -530, 0, -2720, 135)
    SetChrChipByIndex(0x109, 8)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF0, 10)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -2040, 0, -8580, 0)
    SetChrPos(0x11, -460, 0, -8420, 0)
    SetChrChipByIndex(0x10, 0)
    SetChrChipByIndex(0x11, 0)

    def lambda_2944():

        label("loc_2944")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2944")

    QueueWorkItem2(0x10, 3, lambda_2944)

    def lambda_2957():

        label("loc_2957")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2957")

    QueueWorkItem2(0x11, 3, lambda_2957)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 2670, 0, -7050, 315)
    SetChrChipByIndex(0x14, 2)

    def lambda_298F():

        label("loc_298F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_298F")

    QueueWorkItem2(0x14, 3, lambda_298F)
    OP_6D(-160, 0, -7560, 0)
    OP_67(0, 6830, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(189000, 0)
    OP_6E(298, 0)
    OP_43(0x10, 0x0, 0x0, 0x17)
    OP_43(0x11, 0x0, 0x0, 0x18)
    OP_43(0x14, 0x0, 0x0, 0x19)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x194, 0x0, 0x64)
    Sleep(150)
    OP_22(0x194, 0x0, 0x64)
    Sleep(500)
    OP_22(0x193, 0x0, 0x64)
    Sleep(1000)

    def lambda_2A1C():
        OP_6D(1120, 1600, -7240, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A1C)

    def lambda_2A34():
        OP_67(0, 6830, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A34)

    def lambda_2A4C():
        OP_6B(3080, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2A4C)

    def lambda_2A5C():
        OP_6E(310, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2A5C)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(-2310, 0, -2720, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(314000, 0)
    OP_6E(279, 0)
    OP_0D()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #59
        0x109,
        (
            "#1075F#5P……哼，撤退了吗。\x02\x03",

            "#1840F还真是机灵的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#1505F#5P嗯，和普通的魔兽不一样，\x01",
            "好像拥有较高的智能。\x02\x03",

            "#1502F果然还是和之前一样，\x01",
            "是『不可能存在的魔物』吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x109,
        (
            "#1063F#5P嗯，\x01",
            "虽然不了解列曼自治州的魔兽生态，\x01",
            "但这样的肯定不正常。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C85")

    ChrTalk(    #62
        0x10B,
        (
            "#413F#5P唉……这『第四星层』\x01",
            "也得让我们费一番功夫呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2C85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CD6")

    ChrTalk(    #63
        0x107,
        (
            "#062F#5P这、这『第四星层』\x01",
            "也不是简单就能通过呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D2B")

    ChrTalk(    #64
        0x10E,
        (
            "#178F#5P……看来这『第四星层』\x01",
            "也没办法一鼓作气通过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2D2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D76")

    ChrTalk(    #65
        0x10D,
        (
            "#277F#5P……这『第四星层』\x01",
            "也有一番折腾的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2D76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DCC")

    ChrTalk(    #66
        0x105,
        (
            "#1162F#5P……看来这『第四星层』\x01",
            "也没办法一鼓作气通过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E15")

    label("loc_2DCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E15")

    ChrTalk(    #67
        0x104,
        (
            "#1545F#5P呵，这『第四星层』\x01",
            "也真是值得期待呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E15")

    Sleep(300)
    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E84")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2EEB")

    label("loc_2E84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EAC")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2EEB")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2EEB")

    label("loc_2ED4")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2EEB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F18")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F7F")

    label("loc_2F18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F40")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F7F")

    label("loc_2F40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F68")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F7F")

    label("loc_2F68")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2F7F")

    Sleep(1000)

    def lambda_2F8A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2F8A)
    Sleep(100)
    OP_8C(0xF0, 270, 400)
    Sleep(300)

    ChrTalk(    #68
        0x109,
        "#1069F#5P出来了吗……！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x109, 0x20)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -1660, 500, 1000, 180)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_301E():

        label("loc_301E")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_301E")

    QueueWorkItem2(0x17, 2, lambda_301E)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x96, 0x5DC)

    def lambda_3041():
        OP_6D(-2510, 200, -1000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3041)

    def lambda_3059():
        OP_67(0, 6540, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3059)

    def lambda_3071():
        OP_6B(2720, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3071)

    def lambda_3081():
        OP_6E(279, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3081)

    def lambda_3091():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3091)
    Sleep(100)

    def lambda_30A4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_30A4)
    Sleep(100)
    OP_8C(0xF0, 0, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #69
        (
            "\x07\x0C\x18#2S#80W……终于……\x01",
            "………来到这里了………\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #70
        (
            "\x07\x0C\x18#2S#80W这个『第四星层』……\x01",
            "一共有三座『修炼场』……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #71
        (
            "\x07\x0C\x18#2S#80W全部通过之后……\x01",
            "……就可以打开前进的道路……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #72
        "\x07\x0C\x18#2S#80W……请……把这个……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x20)
    SetChrPos(0x18, -1830, 500, -3500, 180)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x99, 0x0, 0x64)

    def lambda_3210():
        OP_8F(0xFE, 0xFFFFF8DA, 0xFFFFFED4, 0xFFFFF254, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3210)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    WaitChrThread(0x18, 0x1)
    Sleep(500)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #73
        "\x07\x00得到了\x1F\x2C\x03\x07\x00。\x02",
    )

    Jump("loc_3276")

    label("loc_3276")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x32C, 1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #74
        (
            "\x07\x0C\x18#2S#80W……可是……\x01",
            "请……千万小心……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #75
        (
            "\x07\x0C\x18#2S#80W『影之王』的目标是……\x01",
            "………你……的……………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_82(0x1, 0x2)
    SetChrFlags(0x17, 0x80)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339F")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_33F7")

    label("loc_339F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C2")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_33F7")

    label("loc_33C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E5")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_33F7")

    label("loc_33E5")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_33F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_341A")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3472")

    label("loc_341A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343D")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3472")

    label("loc_343D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3460")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3472")

    label("loc_3460")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3472")

    Sleep(500)
    OP_6D(-2310, 0, -2500, 1500)
    OP_63(0x109)
    OP_63(0x102)
    OP_63(0xF0)
    OP_63(0xF1)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #76
        0x109,
        (
            "#1841F#6P……消失了吗。\x02\x03",

            "#1063F是不是因为被夺走了『力量』，\x01",
            "而无法让我们看到她的全部面貌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#1505F#5P嗯……\x01",
            "她说不定也很焦急呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3555():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3555)
    Sleep(100)

    def lambda_3568():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3568)
    Sleep(100)
    OP_8C(0xF0, 270, 400)
    Sleep(300)

    ChrTalk(    #78
        0x102,
        (
            "#1500F#11P不过，\x01",
            "她给了我们非常贵重的线索呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        "#1060F#6P是啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #80
        "\x07\x05凯文摊开了卢·洛克尔的地图。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x12, 0x0, 0x64)
    OP_AD(0x2400C9, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    FadeToBright(0, 0)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #81
        (
            "\x07\x00#1063F……唔，\x01",
            "我们现在应该在右上角的这个地方。\x02\x03",

            "左边相邻的是\x01",
            "『巴斯塔尔水道』……\x02\x03",

            "这大概就是她所说的\x01",
            "『修炼场』吧。\x02",
        )
    )

    Jump("loc_36DD")

    label("loc_36DD")

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_375B")
    OP_A2(0x7)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #82
        (
            "\x07\x00#074F可是，她所说的修炼场\x01",
            "应该有三个吧。\x02\x03",

            "#072F剩下的两个在哪里？\x02",
        )
    )

    Jump("loc_3755")

    label("loc_3755")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3A0C")

    label("loc_375B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37ED")
    OP_A2(0x6)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #83
        (
            "\x07\x00#1545F嗯，可是她所说的修炼场\x01",
            "应该有三个才对。\x02\x03",

            "#1540F剩下的两个在哪里呢？\x02",
        )
    )

    Jump("loc_37E7")

    label("loc_37E7")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3A0C")

    label("loc_37ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3870")
    OP_A2(0x5)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("科洛丝")

    AnonymousTalk(    #84
        (
            "\x07\x00#1163F……可是她刚才说\x01",
            "修炼场一共有三个。\x02\x03",

            "剩下的两个在哪里呢？\x02",
        )
    )

    Jump("loc_386A")

    label("loc_386A")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3A0C")

    label("loc_3870")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F6")
    OP_A2(0x2)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("穆拉")

    AnonymousTalk(    #85
        (
            "\x07\x00#272F可是她刚才应该是说\x01",
            "一共有三个修炼场……\x02\x03",

            "#270F剩下的两个在哪里呢？\x02",
        )
    )

    Jump("loc_38F0")

    label("loc_38F0")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3A0C")

    label("loc_38F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_398A")
    OP_A2(0x1)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("尤莉亚　　　　　　　")

    AnonymousTalk(    #86
        (
            "\x07\x00#176F可是她刚才应该是说\x01",
            "一共有三个修炼场……\x02\x03",

            "#178F剩下的两个在哪儿呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3A0C")

    label("loc_398A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A0C")
    OP_A2(0x0)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #87
        (
            "\x07\x00#063F可、可是那位姐姐……\x01",
            "好像说修炼场有三个呢。\x02\x03",

            "剩下的两个在哪儿呢？\x02",
        )
    )

    Jump("loc_3A09")

    label("loc_3A09")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ACF")
    SetMessageWindowPos(80, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #88
        (
            "\x07\x00#1505F大概……\x01",
            "是在这条断得\x01",
            "很不自然的路前面吧。\x02\x03",

            "#1502F不过，也许这也是\x01",
            "所谓的『规则』之一。\x02\x03",

            "现在往那边走\x01",
            "也许什么都看不到。\x02",
        )
    )

    Jump("loc_3AC9")

    label("loc_3AC9")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3B84")

    label("loc_3ACF")

    SetMessageWindowPos(80, 80, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #89
        (
            "\x07\x00#1505F大概……\x01",
            "是在这条断得\x01",
            "很不自然的路前面吧。\x02\x03",

            "#1502F不过，也许这也是\x01",
            "所谓的『规则』之一。\x02\x03",

            "现在往那边走\x01",
            "也许什么都看不到。\x02",
        )
    )

    Jump("loc_3B81")

    label("loc_3B81")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3B84")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #90
        (
            "\x07\x00#1067F在这被重组的空间内，\x01",
            "也不是不可能发生的事情……\x02\x03",

            "#1060F……没办法，我们先去这个\x01",
            "『巴斯塔尔水道』看看吧。\x02",
        )
    )

    Jump("loc_3C1A")

    label("loc_3C1A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_A2(0x2902)
    OP_28(0x32, 0x1, 0x8)
    OP_28(0x32, 0x1, 0x10)
    OP_28(0x32, 0x1, 0x20)
    OP_28(0x32, 0x1, 0x40)
    OP_28(0x32, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_22_2840 end

    def Function_23_3C54(): pass

    label("Function_23_3C54")

    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0xFFFFF7EA, 0x0, 0xFFFFDA9E, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(2500)
    OP_8C(0xFE, 180, 600)
    SetChrChipByIndex(0xFE, 1)

    def lambda_3C89():

        label("loc_3C89")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_3C89")

    QueueWorkItem2(0xFE, 3, lambda_3C89)
    OP_8F(0xFE, 0xFFFFF952, 0x0, 0xFFFFA2E0, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_3C54 end

    def Function_24_3CB0(): pass

    label("Function_24_3CB0")

    Sleep(150)
    SetChrChipByIndex(0xFE, 1)
    OP_8F(0xFE, 0xFFFFFE84, 0x0, 0xFFFFDC4C, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(2700)
    OP_8C(0xFE, 180, 600)
    SetChrChipByIndex(0xFE, 1)

    def lambda_3CEA():

        label("loc_3CEA")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_3CEA")

    QueueWorkItem2(0xFE, 3, lambda_3CEA)
    OP_8F(0xFE, 0xFFFFFFA6, 0x0, 0xFFFFA416, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_3CB0 end

    def Function_25_3D11(): pass

    label("Function_25_3D11")

    Sleep(55)
    SetChrChipByIndex(0xFE, 3)
    OP_8F(0xFE, 0xC12, 0x0, 0xFFFFE1C4, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Sleep(2800)
    OP_8C(0xFE, 135, 600)
    SetChrChipByIndex(0xFE, 3)
    OP_8F(0xFE, 0xFD2, 0x0, 0xFFFFDD96, 0x1B58, 0x0)
    OP_22(0xCB, 0x0, 0x64)
    SetChrSubChip(0x0, 2)

    def lambda_3D69():
        OP_96(0xFE, 0x1590, 0xFA0, 0xFFFFD24C, 0x1194, 0x1F40)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D69)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3D91():

        label("loc_3D91")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_3D91")

    QueueWorkItem2(0xFE, 3, lambda_3D91)
    OP_8F(0xFE, 0x22B0, 0x1054, 0xFFFFBAF0, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_3D11 end

    def Function_26_3DB8(): pass

    label("Function_26_3DB8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-450, 3500, 3820, 0)
    OP_67(0, 7420, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(315000, 0)
    OP_6E(385, 0)

    def lambda_3E07():
        OP_6D(1530, -5000, 47780, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E07)

    def lambda_3E1F():
        OP_67(0, 9860, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3E1F)

    def lambda_3E37():
        OP_6B(3820, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3E37)

    def lambda_3E47():
        OP_6E(385, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3E47)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(2000)
    OP_22(0x1DA, 0x0, 0x64)
    OP_22(0x345, 0x1, 0x64)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A2(0x2504)
    OP_A2(0x2509)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_3DB8 end

    def Function_27_3EEB(): pass

    label("Function_27_3EEB")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_3F0E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F1F")

    label("loc_3F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_3F1F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F1F")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3F44"),
        (1, "loc_3F73"),
        (2, "loc_3FA2"),
        (SWITCH_DEFAULT, "loc_3FD1"),
    )


    label("loc_3F44")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_3FD1")

    label("loc_3F73")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_3FD1")

    label("loc_3FA2")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_3FD1")

    label("loc_3FD1")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4006")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4373")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4031"),
        (1, "loc_405D"),
        (2, "loc_409A"),
        (SWITCH_DEFAULT, "loc_40EC"),
    )


    label("loc_4031")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_40EC")

    label("loc_405D")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_40EC")

    label("loc_409A")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_40EC")

    label("loc_40EC")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4116"),
        (1, "loc_41AA"),
        (2, "loc_4240"),
        (3, "loc_42D6"),
        (SWITCH_DEFAULT, "loc_4370"),
    )


    label("loc_4116")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #91
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_4175")

    label("loc_4175")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4197"),
        (1, "loc_41A4"),
        (SWITCH_DEFAULT, "loc_41A7"),
    )


    label("loc_4197")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41A7")

    label("loc_41A4")

    Jump("loc_41A7")

    label("loc_41A7")

    Jump("loc_4370")

    label("loc_41AA")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #92
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_420B")

    label("loc_420B")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_422D"),
        (1, "loc_423A"),
        (SWITCH_DEFAULT, "loc_423D"),
    )


    label("loc_422D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_423D")

    label("loc_423A")

    Jump("loc_423D")

    label("loc_423D")

    Jump("loc_4370")

    label("loc_4240")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #93
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_42A1")

    label("loc_42A1")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_42C3"),
        (1, "loc_42D0"),
        (SWITCH_DEFAULT, "loc_42D3"),
    )


    label("loc_42C3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_42D3")

    label("loc_42D0")

    Jump("loc_42D3")

    label("loc_42D3")

    Jump("loc_4370")

    label("loc_42D6")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #94
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_433B")

    label("loc_433B")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_435D"),
        (1, "loc_436A"),
        (SWITCH_DEFAULT, "loc_436D"),
    )


    label("loc_435D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_436D")

    label("loc_436A")

    Jump("loc_436D")

    label("loc_436D")

    Jump("loc_4370")

    label("loc_4370")

    Jump("loc_4006")

    label("loc_4373")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_438C"),
        (1, "loc_43C0"),
        (2, "loc_43F4"),
        (3, "loc_4428"),
        (SWITCH_DEFAULT, "loc_445C"),
    )


    label("loc_438C")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_445C")

    label("loc_43C0")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_445C")

    label("loc_43F4")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_445C")

    label("loc_4428")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_445C")

    label("loc_445C")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_447E"),
        (1, "loc_448A"),
        (2, "loc_4496"),
        (3, "loc_44A2"),
        (SWITCH_DEFAULT, "loc_44AE"),
    )


    label("loc_447E")

    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_44AE")

    label("loc_448A")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_44AE")

    label("loc_4496")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_44AE")

    label("loc_44A2")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_44AE")

    label("loc_44AE")

    Return()

    # Function_27_3EEB end

    def Function_28_44AF(): pass

    label("Function_28_44AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44C0")
    Call(0, 2)
    Return()

    label("loc_44C0")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 7450, 0, 5550, 180)
    SetChrPos(0x1, 6540, 0, 6210, 180)
    SetChrPos(0x2, 8230, 0, 6140, 180)
    SetChrPos(0x3, 7310, 0, 7160, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 30)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x104), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_28_44AF end

    def Function_29_459E(): pass

    label("Function_29_459E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 7450, 0, 5430, 0)
    SetChrPos(0x2, 6540, 0, 6210, 0)
    SetChrPos(0x1, 8230, 0, 6140, 0)
    SetChrPos(0x0, 7310, 0, 7160, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 31)
    NewScene("ED6_DT21/M7107   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_29_459E end

    def Function_30_465A(): pass

    label("Function_30_465A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4683")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4677():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4677)

    label("loc_4683")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46AC")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_46A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_46A0)

    label("loc_46AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D5")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_46C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_46C9)

    label("loc_46D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46FE")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_46F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_46F2)

    label("loc_46FE")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_472A")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_472A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4741")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4741")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4758")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4758")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_476F")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_476F")

    Return()

    # Function_30_465A end

    def Function_31_4770(): pass

    label("Function_31_4770")


    def lambda_4776():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4776)

    def lambda_4788():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4788)

    def lambda_479A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_479A)

    def lambda_47AC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_47AC)
    Sleep(1000)
    Return()

    # Function_31_4770 end

    def Function_32_47BE(): pass

    label("Function_32_47BE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #95
        (
            "\x07\x05　　　游击士协会\x01",
            "【卢·洛克尔训练场】\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_32_47BE end

    SaveToFile()

Try(main)
