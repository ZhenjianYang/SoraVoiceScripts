from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7107   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7107.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60222",
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
        'Schwarzritter',                        # 9
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
        'ED6_DT27/CH03440 ._CH',             # 00
        'ED6_DT27/CH04455 ._CH',             # 01
        'ED6_DT27/CH04080 ._CH',             # 02
        'ED6_DT27/CH04082 ._CH',             # 03
        'ED6_DT26/CH20724 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03440P._CP',             # 00
        'ED6_DT27/CH04455P._CP',             # 01
        'ED6_DT27/CH04080P._CP',             # 02
        'ED6_DT27/CH04082P._CP',             # 03
        'ED6_DT26/CH20724P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4450,
        Y                   = -1000,
        Z                   = 15020,
        Range               = 4070,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x4858,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = 7800,
        TriggerZ            = 0,
        TriggerY            = -80,
        TriggerRange        = 1000,
        ActorX              = 7800,
        ActorZ              = 2000,
        ActorY              = -80,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 1500,
        TriggerY            = 33300,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 2500,
        ActorY              = 33300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15A",          # 00, 0
        "Function_1_1A4",          # 01, 1
        "Function_2_234",          # 02, 2
        "Function_3_40B",          # 03, 3
        "Function_4_465",          # 04, 4
        "Function_5_802",          # 05, 5
        "Function_6_82E",          # 06, 6
        "Function_7_85F",          # 07, 7
        "Function_8_890",          # 08, 8
        "Function_9_8C1",          # 09, 9
        "Function_10_CC9",         # 0A, 10
        "Function_11_CF5",         # 0B, 11
        "Function_12_D26",         # 0C, 12
        "Function_13_D57",         # 0D, 13
        "Function_14_D88",         # 0E, 14
        "Function_15_3FAC",        # 0F, 15
        "Function_16_4662",        # 10, 16
        "Function_17_47AD",        # 11, 17
        "Function_18_4950",        # 12, 18
        "Function_19_4A2E",        # 13, 19
        "Function_20_4B0F",        # 14, 20
        "Function_21_4C25",        # 15, 21
    )


    def Function_0_15A(): pass

    label("Function_0_15A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_172"),
        (SWITCH_DEFAULT, "loc_179"),
    )


    label("loc_172")

    Event(0, 18)
    Jump("loc_179")

    label("loc_179")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A3")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1A3")

    Return()

    # Function_0_15A end

    def Function_1_1A4(): pass

    label("Function_1_1A4")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x23008A)
    OP_1B(0x2, 0x0, 0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5")
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x85, 0x0)

    label("loc_1E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F4")
    Jump("loc_21A")

    label("loc_1F4")

    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x0, 120)
    OP_6F(0x1, 120)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C")
    OP_6F(0x3, 0)
    Jump("loc_233")

    label("loc_22C")

    OP_6F(0x3, 60)

    label("loc_233")

    Return()

    # Function_1_1A4 end

    def Function_2_234(): pass

    label("Function_2_234")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x33F, 1)"), scpexpr(EXPR_END)), "loc_2A2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x3F\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AF)
    Jump("loc_30A")

    label("loc_2A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x3F\x03\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x3F\x03\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_30A")

    Jump("loc_3FD")

    label("loc_30D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05[22/36] 'And for thirty-three of those years, I hated that damn place,'\x01",
            "he snapped between chewing cuts of lamb. After swallowing, he added,\x01",
            "'Who's going to run it? I sure ain't, and you're no carpenter.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xCA, 0x0)

    label("loc_3FD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_234 end

    def Function_3_40B(): pass

    label("Function_3_40B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 3)), scpexpr(EXPR_END)), "loc_43E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 2)), scpexpr(EXPR_END)), "loc_42C")
    Call(0, 9)
    Jump("loc_43B")

    label("loc_42C")

    OP_DC(0x0, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_43B")

    Jump("loc_462")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 4)), scpexpr(EXPR_END)), "loc_462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 7)), scpexpr(EXPR_END)), "loc_453")
    Call(0, 4)
    Jump("loc_462")

    label("loc_453")

    OP_DC(0x0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_462")

    EventEnd(0x0)
    Return()

    # Function_3_40B end

    def Function_4_465(): pass

    label("Function_4_465")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DF(0x0, 0x1, 0x1)
    Sleep(300)
    SetChrPos(0xEE, 14890, 4000, -29830, 0)
    SetChrPos(0xEF, 15300, 4000, -30380, 0)
    SetChrPos(0xF0, 14260, 4000, -30350, 0)
    SetChrPos(0xF1, 14970, 4000, -31300, 0)
    OP_9F(0xEE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x4, 0x80)
    ClearChrFlags(0x5, 0x80)
    ClearChrFlags(0x6, 0x80)
    ClearChrFlags(0x7, 0x80)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrPos(0xF2, 1960, 0, -2570, 135)
    SetChrPos(0xF3, 0, 0, -1870, 135)
    SetChrPos(0xF4, 2410, 0, -740, 135)
    SetChrPos(0xF5, 850, 0, 0, 135)
    OP_6D(13690, 9000, -26230, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)

    def lambda_5C5():
        OP_6D(13690, 4500, -26230, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5C5)

    def lambda_5DD():
        OP_67(0, 6200, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5DD)
    FadeToBright(2000, 0)
    OP_22(0x6C, 0x0, 0x64)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    OP_43(0xEE, 0x0, 0x0, 0x5)
    OP_43(0xEF, 0x0, 0x0, 0x6)
    OP_43(0xF0, 0x0, 0x0, 0x7)
    OP_43(0xF1, 0x0, 0x0, 0x8)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)

    ChrTalk(    #3
        0x10F,
        "#1442F#1PKevin!\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_687():
        OP_6D(-270, 0, -1370, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_687)

    def lambda_69F():
        OP_67(0, 6970, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_69F)

    def lambda_6B7():
        OP_6B(3670, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6B7)

    def lambda_6C7():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6C7)

    def lambda_6D7():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6D7)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(14160, 4000, -25750, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(3440, 0)
    OP_6C(224000, 0)
    OP_6E(253, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #4
        0x109,
        "#1840F#5PHaha... Looks like they're okay.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_76D():
        OP_8E(0xFE, 0x3930, 0x0, 0xFFFFCAA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_76D)
    Sleep(150)

    def lambda_78D():
        OP_8E(0xFE, 0x3CFA, 0x0, 0xFFFFC928, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_78D)
    Sleep(200)

    def lambda_7AD():
        OP_8E(0xFE, 0x35E8, 0x0, 0xFFFFC93C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_7AD)
    Sleep(250)

    def lambda_7CD():
        OP_8E(0xFE, 0x38FE, 0x0, 0xFFFFC680, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_7CD)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    Call(0, 14)
    Return()

    # Function_4_465 end

    def Function_5_802(): pass

    label("Function_5_802")


    def lambda_808():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_808)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x39F8, 0xFA0, 0xFFFFA128, 0x7D0, 0x0)
    Return()

    # Function_5_802 end

    def Function_6_82E(): pass

    label("Function_6_82E")

    Sleep(300)

    def lambda_839():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_839)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x3D36, 0xFA0, 0xFFFF9D7C, 0x7D0, 0x0)
    Return()

    # Function_6_82E end

    def Function_7_85F(): pass

    label("Function_7_85F")

    Sleep(600)

    def lambda_86A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86A)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x367E, 0xFA0, 0xFFFF9BD8, 0x7D0, 0x0)
    Return()

    # Function_7_85F end

    def Function_8_890(): pass

    label("Function_8_890")

    Sleep(1000)

    def lambda_89B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_89B)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x394E, 0xFA0, 0xFFFF9750, 0x7D0, 0x0)
    Return()

    # Function_8_890 end

    def Function_9_8C1(): pass

    label("Function_9_8C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DC(0x0, 0x0)
    OP_DF(0x0, 0x1, 0x1)
    Sleep(300)
    OP_E0(242, 0x45, 0x1)
    OP_E0(243, 0x46, 0x1)
    OP_E0(244, 0x47, 0x1)
    OP_E0(245, 0x48, 0x1)
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x4, 0x80)
    ClearChrFlags(0x5, 0x80)
    ClearChrFlags(0x6, 0x80)
    ClearChrFlags(0x7, 0x80)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrPos(0xF2, -14750, 4000, -29670, 0)
    SetChrPos(0xF3, -14120, 4000, -30480, 0)
    SetChrPos(0xF4, -15430, 4000, -30480, 0)
    SetChrPos(0xF5, -14720, 4000, -31090, 0)
    OP_9F(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x6, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, -2060, 0, -1910, 225)
    SetChrPos(0x1, -2270, 0, -560, 225)
    SetChrPos(0x2, 250, 0, -2310, 225)
    SetChrPos(0x3, 220, 0, -500, 225)
    OP_6D(-13410, 9000, -26560, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)

    def lambda_A8C():
        OP_6D(-13410, 4500, -26560, 5000)
        ExitThread()

    QueueWorkItem(0xF2, 2, lambda_A8C)

    def lambda_AA4():
        OP_67(0, 6200, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xF2, 3, lambda_AA4)
    FadeToBright(2000, 0)
    OP_22(0x6C, 0x0, 0x64)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    OP_43(0xF2, 0x0, 0x0, 0xA)
    OP_43(0xF3, 0x0, 0x0, 0xB)
    OP_43(0xF4, 0x0, 0x0, 0xC)
    OP_43(0xF5, 0x0, 0x0, 0xD)
    WaitChrThread(0xF2, 0x0)
    WaitChrThread(0xF3, 0x0)
    WaitChrThread(0xF4, 0x0)
    WaitChrThread(0xF5, 0x0)

    ChrTalk(    #5
        0x109,
        "#1078F#2PRies!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_B4D():
        OP_6D(110, 0, -1560, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B4D)

    def lambda_B65():
        OP_67(0, 6080, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B65)

    def lambda_B7D():
        OP_6B(3800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B7D)

    def lambda_B8D():
        OP_6C(89000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B8D)

    def lambda_B9D():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B9D)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-13620, 4000, -26570, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(3440, 0)
    OP_6C(135000, 0)
    OP_6E(256, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x10F,
        "#1442F#11PThank goodness...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xF2, 5)

    def lambda_C25():
        OP_8E(0xFE, 0xFFFFC662, 0x0, 0xFFFFC7B6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF2, 0, lambda_C25)
    Sleep(150)
    SetChrChipByIndex(0xF3, 6)

    def lambda_C4A():
        OP_8E(0xFE, 0xFFFFCA5E, 0x0, 0xFFFFC400, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF3, 0, lambda_C4A)
    Sleep(200)
    SetChrChipByIndex(0xF4, 7)

    def lambda_C6F():
        OP_8E(0xFE, 0xFFFFC2FC, 0x0, 0xFFFFC48C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_C6F)
    Sleep(250)
    SetChrChipByIndex(0xF5, 8)

    def lambda_C94():
        OP_8E(0xFE, 0xFFFFC69E, 0x0, 0xFFFFC22A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_C94)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xF2, 0x0)
    OP_44(0xF3, 0x0)
    OP_44(0xF4, 0x0)
    OP_44(0xF5, 0x0)
    Call(0, 14)
    Return()

    # Function_9_8C1 end

    def Function_10_CC9(): pass

    label("Function_10_CC9")


    def lambda_CCF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CCF)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFC680, 0xFA0, 0xFFFFA088, 0x7D0, 0x0)
    Return()

    # Function_10_CC9 end

    def Function_11_CF5(): pass

    label("Function_11_CF5")

    Sleep(300)

    def lambda_D00():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D00)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFCB58, 0xFA0, 0xFFFF9CAA, 0x7D0, 0x0)
    Return()

    # Function_11_CF5 end

    def Function_12_D26(): pass

    label("Function_12_D26")

    Sleep(600)

    def lambda_D31():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D31)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFC2FC, 0xFA0, 0xFFFF9D22, 0x7D0, 0x0)
    Return()

    # Function_12_D26 end

    def Function_13_D57(): pass

    label("Function_13_D57")

    Sleep(1000)

    def lambda_D62():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D62)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFC752, 0xFA0, 0xFFFF98C2, 0x7D0, 0x0)
    Return()

    # Function_13_D57 end

    def Function_14_D88(): pass

    label("Function_14_D88")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_DC(0x0, 0x0)
    OP_DF(0x0, 0x1, 0x1)
    Sleep(300)
    SetChrPos(0xEE, 870, 0, 660, 270)
    SetChrPos(0xEF, 2330, 0, 740, 270)
    SetChrPos(0xF0, 600, 0, -1530, 315)
    SetChrPos(0xF1, 2210, 0, -1110, 270)
    OP_51(0xF2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF2, 0x8)
    ClearChrFlags(0xF3, 0x8)
    ClearChrFlags(0xF4, 0x8)
    ClearChrFlags(0xF5, 0x8)
    SetChrPos(0xF2, -910, 0, 410, 90)
    SetChrPos(0xF3, -2540, 0, 610, 90)
    SetChrPos(0xF4, -1400, 0, -1890, 45)
    SetChrPos(0xF5, -2780, 0, -1310, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 10000, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(1080, 0, 1010, 0)
    OP_67(0, 6370, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    Sleep(1500)

    def lambda_F0D():
        OP_6B(2770, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F0D)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #7
        0x109,
        (
            "#1068F#5PWhew... Yep. You're the real deal, all right.\x02\x03",

            "#1840FThank Aidios... I was worried as hell about\x01",
            "you, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        (
            "#1447F#6PI could say the same to you.\x02\x03",

            "#1445FStill, it looks like those really must have been\x01",
            "grimoires, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        "#1063F#5PSure does.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10E,
        "#173FGrimoires?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10D,
        "#270FIs that the name of those fiends we encountered?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1065F#5PYou got it. It's a type of fiend mentioned in\x01",
            "the Testaments.\x02\x03",

            "#1063FAlthough, maybe 'fiend' isn't the best word...\x01",
            "They're said to be what souls eventually turn\x01",
            "into after being thrown into Gehenna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10B,
        "#216FPeople's souls turn into...those?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#1503FThat's not a very pleasant thought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        (
            "#1446F#6PAs I'm sure you know, the church teaches\x01",
            "that the souls of sinners end up in the fiery\x01",
            "depths of Gehenna.\x02\x03",

            "#1445FThere, they are tormented by the ceaseless\x01",
            "flames, slowly losing their own sense of self\x01",
            "over time...\x02\x03",

            "#1443F...till finally, they're said to end up as nothing\x01",
            "more than a chaotic lump of spirit known as a\x01",
            "grimoire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x107,
        "#065FI-I'm getting goosebumps just picturing it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#1163FAnd that's what those shapeshifting\x01",
            "creatures we encountered were?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1446F#6PYes.\x02\x03",

            "The mirrors and cannons that appear with\x01",
            "them are all cursed items that have the\x01",
            "same origin.\x02\x03",

            "#1443FHow they did it, I don't know...but it seems\x01",
            "our enemies have quite literally opened the\x01",
            "gates of Gehenna.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #19
        0x10,
        "Man's Voice",
        "\x07\x05#4P...Haha. That's quite a fitting metaphor.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E2")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1549")

    label("loc_14E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150A")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1549")

    label("loc_150A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1532")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1549")

    label("loc_1532")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1549")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1571")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15D8")

    label("loc_1571")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1599")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15D8")

    label("loc_1599")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C1")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15D8")

    label("loc_15C1")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_15D8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1605")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_166C")

    label("loc_1605")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_166C")

    label("loc_162D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1655")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_166C")

    label("loc_1655")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_166C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1694")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16FB")

    label("loc_1694")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BC")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16FB")

    label("loc_16BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16FB")

    label("loc_16E4")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16FB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1728")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_178F")

    label("loc_1728")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1750")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_178F")

    label("loc_1750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1778")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_178F")

    label("loc_1778")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_178F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B7")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_181E")

    label("loc_17B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DF")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_181E")

    label("loc_17DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1807")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_181E")

    label("loc_1807")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_181E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184B")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18B2")

    label("loc_184B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1873")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18B2")

    label("loc_1873")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189B")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18B2")

    label("loc_189B")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_18B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18DA")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1941")

    label("loc_18DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1902")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1941")

    label("loc_1902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192A")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1941")

    label("loc_192A")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1941")

    Sleep(1000)

    def lambda_194C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_194C)
    Sleep(50)

    def lambda_195F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF2, 1, lambda_195F)

    def lambda_196D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_196D)
    Sleep(50)

    def lambda_1980():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1980)

    def lambda_198E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_198E)
    Sleep(50)

    def lambda_19A1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_19A1)

    def lambda_19AF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_19AF)
    Sleep(50)

    def lambda_19C2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_19C2)
    Sleep(300)

    ChrTalk(    #20
        0x10F,
        "#1441F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x109,
        "#1069F#12PThat sounds like...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0xB0)

    def lambda_1A13():
        OP_6D(530, 0, 10740, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A13)

    def lambda_1A2B():
        OP_67(0, 5770, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A2B)

    def lambda_1A43():
        OP_6B(2970, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A43)

    def lambda_1A53():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1A53)

    def lambda_1A63():
        OP_6E(291, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1A63)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 10000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x1, 0xFF, -350, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1AF1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AF1)
    OP_22(0x59, 0x0, 0x64)
    OP_8C(0xEE, 0, 0)
    OP_8C(0xEF, 0, 0)
    OP_8C(0xF0, 0, 0)
    OP_8C(0xF1, 0, 0)
    OP_8C(0xF2, 0, 0)
    OP_8C(0xF3, 0, 0)
    OP_8C(0xF4, 0, 0)
    OP_8C(0xF5, 0, 0)
    Fade(500)
    OP_6D(-480, 0, 4120, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(157000, 0)
    OP_6E(473, 0)
    OP_6D(-200, 0, 4510, 0)
    OP_67(0, 3890, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(152000, 0)
    OP_6E(473, 0)
    OP_6D(-200, 0, 4510, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(152000, 0)
    OP_6E(473, 0)
    OP_6D(350, 0, 3060, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(152000, 0)
    OP_6E(473, 0)
    OP_0D()
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6A")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CD1")

    label("loc_1C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C92")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CD1")

    label("loc_1C92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CBA")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CD1")

    label("loc_1CBA")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1CD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF9")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D60")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D21")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D60")

    label("loc_1D21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D49")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D60")

    label("loc_1D49")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1D60")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D8D")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1DF4")

    label("loc_1D8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB5")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1DF4")

    label("loc_1DB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DDD")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1DF4")

    label("loc_1DDD")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1C")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E83")

    label("loc_1E1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E44")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E83")

    label("loc_1E44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E83")

    label("loc_1E6C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1E83")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB0")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F17")

    label("loc_1EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F17")

    label("loc_1ED8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F00")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F17")

    label("loc_1F00")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1F17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3F")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FA6")

    label("loc_1F3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F67")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FA6")

    label("loc_1F67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8F")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FA6")

    label("loc_1F8F")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1FA6")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD3")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_203A")

    label("loc_1FD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FFB")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_203A")

    label("loc_1FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2023")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_203A")

    label("loc_2023")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_203A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2062")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20C9")

    label("loc_2062")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_208A")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20C9")

    label("loc_208A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B2")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20C9")

    label("loc_20B2")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_20C9")

    Sleep(1000)

    ChrTalk(    #22
        0x102,
        "#1504F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10E,
        "#172F#5PYou again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1075F#5PWell, look who decided to show their ugly mug.\x02\x03",

            "#1060FDid that lord of yours send you to come check\x01",
            "up on us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "\x07\x05#1591F#6PThat is one of the roles I have been assigned,\x01",
            "albeit not the only one.\x02\x03",

            "I am impressed by how quickly you've progressed,\x01",
            "even if it was with a significant amount of the\x01",
            "hermit's guidance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1063F#5PThe hermit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        (
            "#1163F#5PWho's that? The ghost we keep running into?\x02\x03",

            "I can't think of anyone else. She's been helping us\x01",
            "in various ways since we arrived here, and yet we\x01",
            "still have no idea who she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "\x07\x05#1590F#6PIndeed, I speak of her. She is a spirit that was\x01",
            "left behind in Phantasma, as well as the master\x01",
            "of the hollow garden.\x02\x03",

            "#1591FHah. Of course, thanks to my lord taking most\x01",
            "of her power, she can do little other than struggle\x01",
            "as your guide.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        (
            "#1075F#5PHmph. As usual, your cryptic nonsense just\x01",
            "goes right over my head.\x02\x03",

            "#1060FBut hey. If she's your enemy, that makes her\x01",
            "our ally, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "\x07\x05#1591F#6PI'll leave that for you to find out.\x02\x03",

            "Her position is hardly your concern at this time.\x01",
            "I have a message for you from my lord.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #31
        0x10,
        (
            "\x07\x05#1590F#6P'Your next destination is the path of beasts.'\x01\x02\x03",

            "'Devour the new offering presented to you, and\x01",
            "display your seal once more.'\x02\x03",

            "'Then shall the flames of Gehenna burn ever fiercer,\x01",
            "and my kingdom draw closer to its true completion.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x10F,
        "#1444F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        "#1079F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10E,
        "#178F#5PWhat is that supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "\x07\x05#1591F#6PMy lord says that you may choose to interpret\x01",
            "the message however you see fit.\x02\x03",

            "My task was simply to relay it to you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 4)
    SetChrSubChip(0x109, 1)
    OP_0D()
    Sleep(500)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(500)

    ChrTalk(    #36
        0x109,
        "#1846F#5P#50W...Hah...hahaha...\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #37
        0x109,
        "#1061F#5P#4SHahahaha!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #38
        0x10F,
        "#1802F#12PK-Kevin...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x109,
        (
            "#1840F#5PAhaha... Sorry. I couldn't help but laugh.\x02\x03",

            "Tell me: what sad classes did you and that joke of\x01",
            "a boss you got take to get your certifications in how\x01",
            "to be a big bad?\x02\x03",

            "#1075FNice touch trying to confuse us by spewing that\x01",
            "cryptic bullshit, too. Bet you thought we'd keep\x01",
            "ourselves up all night trying to figure that gem out.\x02\x03",

            "#1073FI mean, the overblown theatrics make it a bit TOO\x01",
            "obvious that it's fake, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        "\x07\x05#1590F#6P...\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(1200, 0, 5900, 0)
    OP_67(0, 4450, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(33000, 0)
    OP_6E(334, 0)
    OP_0D()
    Sleep(300)
    Fade(500)

    def lambda_2A45():
        OP_6D(1430, 0, 6040, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A45)

    def lambda_2A5D():
        OP_6B(3350, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A5D)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)

    def lambda_2A8C():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A8C)
    Sleep(300)
    OP_22(0xD8, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #41
        0x109,
        (
            "#1072F#6P...Well? You about done with us? If you are,\x01",
            "how about you get lost?\x02\x03",

            "We've got better things to do with our time\x01",
            "than listen to nonsensical riddles from a guy\x01",
            "who can't even bother to show his face.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x555, 0x2)"), scpexpr(EXPR_END)), "loc_2C4C")

    ChrTalk(    #42
        0x10,
        (
            "\x07\x05#1591F#5PHaha...\x02\x03",

            "I see you're quite fond of the gift granted\x01",
            "to you by my lord.\x02\x03",

            "Does it bring back memories?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x109,
        "#1074F#6PGift?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10F,
        "#1802F#6PKevin...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E3B")

    label("loc_2C4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x555, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D55")

    ChrTalk(    #45
        0x10,
        (
            "\x07\x05#1590F#5PHmm...\x02\x03",

            "I see you weren't all that fond of the gift \x01",
            "granted to you by my lord.\x02\x03",

            "#1591FHow disappointing... Was the thought of\x01",
            "using it that painful to you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x109,
        "#1074F#6PGift?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10F,
        "#1802F#6PKevin...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E3B")

    label("loc_2D55")


    ChrTalk(    #48
        0x10,
        (
            "\x07\x05#1590F#5PHmm... I see you didn't even notice the gift my\x01",
            "lord so graciously tried to grant you, either.\x02\x03",

            "#1591FWhat a shame... Perhaps you instinctively avoided\x01",
            "it out of fear?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        "#1074F#6PGift?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        "#1802F#6PKevin...?\x02",
    )

    CloseMessageWindow()

    label("loc_2E3B")

    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x2, 0x1, 0xFF, 0, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x10F, 0, 400)
    Sleep(500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 10000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0xBA, 0x1, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F00")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F67")

    label("loc_2F00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F28")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F67")

    label("loc_2F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F50")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F67")

    label("loc_2F50")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2F67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8F")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2FF6")

    label("loc_2F8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB7")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2FF6")

    label("loc_2FB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FDF")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2FF6")

    label("loc_2FDF")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2FF6")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3023")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_308A")

    label("loc_3023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_304B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_308A")

    label("loc_304B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3073")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_308A")

    label("loc_3073")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_308A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30B2")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3119")

    label("loc_30B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30DA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3119")

    label("loc_30DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3102")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3119")

    label("loc_3102")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3119")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3146")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_31AD")

    label("loc_3146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_31AD")

    label("loc_316E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3196")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_31AD")

    label("loc_3196")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_31AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D5")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_323C")

    label("loc_31D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31FD")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_323C")

    label("loc_31FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3225")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_323C")

    label("loc_3225")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_323C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3269")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_32D0")

    label("loc_3269")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3291")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_32D0")

    label("loc_3291")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B9")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_32D0")

    label("loc_32B9")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_32D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F8")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_335F")

    label("loc_32F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3320")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_335F")

    label("loc_3320")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3348")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_335F")

    label("loc_3348")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_335F")

    Sleep(1000)

    ChrTalk(    #51
        0x102,
        "#1502F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10B,
        "#214F#6PY-You think you can get away?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "\x07\x05#1591F#5PFear not. We will encounter one another again\x01",
            "before long.\x02\x03",

            "I am, after all, Phantasma's foremost guardian.\x02\x03",

            "Haha... And with that, I bid you farewell.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3488():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3488)
    OP_22(0x59, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    OP_20(0x7D0)
    Sleep(2000)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 65535)
    SetChrSubChip(0xEE, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E9")
    OP_62(0xEE, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3541")

    label("loc_34E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350C")
    OP_62(0xEE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3541")

    label("loc_350C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352F")
    OP_62(0xEE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3541")

    label("loc_352F")

    OP_62(0xEE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3541")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3564")
    OP_62(0xF5, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_35BC")

    label("loc_3564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3587")
    OP_62(0xF5, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_35BC")

    label("loc_3587")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35AA")
    OP_62(0xF5, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_35BC")

    label("loc_35AA")

    OP_62(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_35BC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E4")
    OP_62(0xF4, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_363C")

    label("loc_35E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3607")
    OP_62(0xF4, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_363C")

    label("loc_3607")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362A")
    OP_62(0xF4, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_363C")

    label("loc_362A")

    OP_62(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_363C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365F")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_36B7")

    label("loc_365F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3682")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_36B7")

    label("loc_3682")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A5")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_36B7")

    label("loc_36A5")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_36B7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36DF")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3737")

    label("loc_36DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3702")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3737")

    label("loc_3702")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3725")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3737")

    label("loc_3725")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3737")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375A")
    OP_62(0xF3, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_37B2")

    label("loc_375A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377D")
    OP_62(0xF3, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_37B2")

    label("loc_377D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A0")
    OP_62(0xF3, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_37B2")

    label("loc_37A0")

    OP_62(0xF3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_37B2")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37DA")
    OP_62(0xEF, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3832")

    label("loc_37DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37FD")
    OP_62(0xEF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3832")

    label("loc_37FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3820")
    OP_62(0xEF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3832")

    label("loc_3820")

    OP_62(0xEF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_3832")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3855")
    OP_62(0xF2, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_38AD")

    label("loc_3855")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3878")
    OP_62(0xF2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_38AD")

    label("loc_3878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_389B")
    OP_62(0xF2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_38AD")

    label("loc_389B")

    OP_62(0xF2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_38AD")

    Fade(1000)
    OP_6D(1800, 0, 0, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(134000, 0)
    OP_6E(245, 0)
    SetChrPos(0xEE, 730, 0, -740, 0)
    SetChrPos(0xEF, 2320, 0, 10, 0)
    SetChrPos(0xF0, 2910, 0, -1790, 0)
    SetChrPos(0xF1, 1750, 0, -2940, 0)
    SetChrPos(0xF2, -1110, 0, -790, 0)
    SetChrPos(0xF3, -2970, 0, -20, 0)
    SetChrPos(0xF4, -3250, 0, -1640, 0)
    SetChrPos(0xF5, -1530, 0, -2530, 0)

    def lambda_397D():
        OP_6D(1800, 0, -3000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_397D)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    OP_63(0xEE)
    OP_63(0xEF)
    OP_63(0xF0)
    OP_63(0xF1)
    OP_63(0xF2)
    OP_63(0xF3)
    OP_63(0xF4)
    OP_63(0xF5)
    Sleep(500)

    ChrTalk(    #54
        0x102,
        "#1503F#5PSo that's the Schwarzritter you mentioned?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x109,
        (
            "#1075F#5PHeh. He's the picture of his lord, right down\x01",
            "to taunting us as he leaves.\x02\x03",

            "#1840FToo bad for him that it doesn't take a genius\x01",
            "to work out they're both bluffing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10F,
        "#1802F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10E,
        (
            "#176F#5P'Your next destination is the path of beasts.'\x01\x02\x03",

            "'Devour the new offering presented to you, and\x01",
            "display your seal once more.'\x02\x03",

            "#178F'Then shall the flames of Gehenna burn ever\x01",
            "fiercer, and my kingdom draw closer to its\x01",
            "true completion.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10D,
        (
            "#272F#5PHis words sound as though they have some\x01",
            "specific meaning to me, but they could be\x01",
            "taken in a number of ways at face value.\x02\x03",

            "#270FWe could try to unravel said meaning, but that\x01",
            "may hinder our progress more than help in the\x01",
            "long run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x109,
        "#1075F#5PMy thoughts exactly.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #60
        0x109,
        (
            "#1078F#5PAnyway...what's definitely NOT going to hinder us\x01",
            "is going back to base and seeing who's in the two\x01",
            "sealing stones we picked up.\x02\x03",

            "If we activate that monument over there, we'll be\x01",
            "able to come right back here to continue exploring\x01",
            "later, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DD4():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3DD4)
    Sleep(50)

    def lambda_3DE7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3DE7)
    Sleep(50)

    def lambda_3DFA():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3DFA)
    Sleep(50)

    def lambda_3E0D():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_3E0D)
    Sleep(50)

    def lambda_3E20():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_3E20)
    Sleep(50)

    def lambda_3E33():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_3E33)
    Sleep(50)
    OP_8C(0xF2, 90, 400)
    Sleep(200)

    ChrTalk(    #61
        0x107,
        "#560F#5PThank goodness it's right there, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        "#1382F#5PI wonder who's going to be inside these.\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_3EC1():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3EC1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    Sleep(2000)
    OP_A2(0x280B)
    OP_A2(0x258D)
    OP_AA(2560)
    OP_AA(65281)
    OP_AD(0x2400EF, 0x0, 0x0, 0x64)
    OP_F7(0x3, 0x0, 0x0)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x158), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F60")
    ShowSaveMenu()

    label("loc_3F60")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2504)
    OP_A2(0x2506)
    NewScene("ED6_DT21/U7000   ._SN", 104, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_14_D88 end

    def Function_15_3FAC(): pass

    label("Function_15_3FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 1)), scpexpr(EXPR_END)), "loc_3FB4")
    Return()

    label("loc_3FB4")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-120, 1530, 28620, 0)
    OP_67(0, 12070, -10000, 0)
    OP_6B(3930, 0)
    OP_6C(47000, 0)
    OP_6E(287, 0)
    SetChrPos(0x109, -990, 0, 14080, 0)
    SetChrPos(0x102, 670, 0, 13980, 0)
    SetChrPos(0xF0, -990, 0, 14080, 0)
    SetChrPos(0xF1, 670, 0, 13980, 0)
    Sleep(1000)

    def lambda_4047():
        OP_6D(110, 1530, 26410, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4047)

    def lambda_405F():
        OP_67(0, 7090, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_405F)

    def lambda_4077():
        OP_6B(3350, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4077)

    def lambda_4087():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4087)

    def lambda_4097():
        OP_6E(245, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4097)

    def lambda_40A7():
        OP_8E(0xFE, 0xFFFFFC68, 0x5FA, 0x5F28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_40A7)
    Sleep(200)

    def lambda_40C7():
        OP_8E(0xFE, 0x1D6, 0x5FA, 0x5E92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_40C7)
    Sleep(500)

    def lambda_40E7():
        OP_8E(0xFE, 0xFFFFFBDC, 0x5FA, 0x592E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_40E7)
    Sleep(300)

    def lambda_4107():
        OP_8E(0xFE, 0xDC, 0x5FA, 0x5884, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_4107)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(    #63
        0x102,
        "#1502F#12PAnd here's the entrance to the next plane.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1065F#6PI doubt the pattern'll change up now, so yeah.\x02\x03",

            "#1063FWe won't know what kind of place that's going\x01",
            "to be until we step inside, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_428F")

    ChrTalk(    #65
        0x104,
        (
            "#1545FHeh. Or what utterly bizarre fiends will be \x01",
            "waiting for us there.\x02\x03",

            "#1540FI'm tingling with excitement.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448E")

    label("loc_428F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42DB")

    ChrTalk(    #66
        0x107,
        "#065FO-Or what kinds of scary fiends will be there...\x02",
    )

    CloseMessageWindow()
    Jump("loc_448E")

    label("loc_42DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4346")

    ChrTalk(    #67
        0x10B,
        (
            "#413F*sigh* Wherever it is, there's probably gonna\x01",
            "be a bunch of weird fiends there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448E")

    label("loc_4346")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43B5")

    ChrTalk(    #68
        0x105,
        (
            "#1162FWherever we end up, I imagine there'll be\x01",
            "plenty of strange fiends waiting for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448E")

    label("loc_43B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4423")

    ChrTalk(    #69
        0x10E,
        (
            "#178FWherever we end up, I imagine there'll be\x01",
            "plenty of strange fiends waiting for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448E")

    label("loc_4423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_448E")

    ChrTalk(    #70
        0x10D,
        (
            "#270FWherever we end up, I imagine there'll be\x01",
            "plenty of strange fiends waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44E0")

    ChrTalk(    #71
        0x108,
        (
            "#072FLet's make sure we're good to go before\x01",
            "we keep going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4657")

    label("loc_44E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_452F")

    ChrTalk(    #72
        0x10D,
        (
            "#270FWe'll have to be sure we're ready before\x01",
            "moving on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4657")

    label("loc_452F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_457E")

    ChrTalk(    #73
        0x10E,
        (
            "#178FWe'll have to be sure we're ready before\x01",
            "moving on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4657")

    label("loc_457E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45CE")

    ChrTalk(    #74
        0x105,
        (
            "#1162FWe'll have to be sure we're ready before\x01",
            "moving on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4657")

    label("loc_45CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4620")

    ChrTalk(    #75
        0x10B,
        (
            "#212FLet's make sure we're good to go before\x01",
            "we keep going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4657")

    label("loc_4620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4657")

    ChrTalk(    #76
        0x107,
        "#062FI hope we're ready for them...\x02",
    )

    CloseMessageWindow()

    label("loc_4657")

    OP_A2(0x2901)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_15_3FAC end

    def Function_16_4662(): pass

    label("Function_16_4662")

    EventBegin(0x0)
    Fade(500)
    OP_6D(530, 1530, 28420, 0)
    OP_67(0, 7380, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(253, 0)
    SetChrPos(0x109, -140, 1530, 28780, 0)
    SetChrPos(0x102, 680, 1530, 27980, 0)
    SetChrPos(0xF0, -1030, 1530, 27780, 0)
    SetChrPos(0xF1, -110, 1530, 27110, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -90, 1530, 27950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_4770():
        OP_6D(12870, 1430, 40450, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4770)
    Call(0, 21)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    NewScene("ED6_DT21/U5100   ._SN", 104, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_16_4662 end

    def Function_17_47AD(): pass

    label("Function_17_47AD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #77
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_47EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_492F")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4848"),
        (1, "loc_48C3"),
        (2, "loc_48F1"),
        (SWITCH_DEFAULT, "loc_491F"),
    )


    label("loc_4848")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDE)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_492C")

    label("loc_48C3")

    OP_A9(0x1A)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_492C")

    label("loc_48F1")

    OP_A9(0x5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #79
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_492C")

    label("loc_491F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_492C")

    label("loc_492C")

    Jump("loc_47EC")

    label("loc_492F")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_17_47AD end

    def Function_18_4950(): pass

    label("Function_18_4950")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -110, 1530, 27110, 180)
    SetChrPos(0x1, -1030, 1530, 27780, 180)
    SetChrPos(0x2, 680, 1530, 27980, 180)
    SetChrPos(0x3, -140, 1530, 28780, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -90, 1530, 27950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_18_4950 end

    def Function_19_4A2E(): pass

    label("Function_19_4A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A3F")
    Call(0, 16)
    Return()

    label("loc_4A3F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -110, 1530, 27110, 0)
    SetChrPos(0x2, -1030, 1530, 27780, 0)
    SetChrPos(0x1, 680, 1530, 27980, 0)
    SetChrPos(0x0, -140, 1530, 28780, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -90, 1530, 27950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B05")
    NewScene("ED6_DT21/U5100   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_4B0E")

    label("loc_4B05")

    NewScene("ED6_DT21/U5102   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_4B0E")

    Return()

    # Function_19_4A2E end

    def Function_20_4B0F(): pass

    label("Function_20_4B0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B38")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4B2C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4B2C)

    label("loc_4B38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B61")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4B55():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4B55)

    label("loc_4B61")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B8A")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4B7E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4B7E)

    label("loc_4B8A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BB3")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4BA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4BA7)

    label("loc_4BB3")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BDF")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4BDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BF6")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4BF6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C0D")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4C0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C24")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4C24")

    Return()

    # Function_20_4B0F end

    def Function_21_4C25(): pass

    label("Function_21_4C25")


    def lambda_4C2B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4C2B)

    def lambda_4C3D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4C3D)

    def lambda_4C4F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4C4F)

    def lambda_4C61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4C61)
    Sleep(1000)
    Return()

    # Function_21_4C25 end

    SaveToFile()

Try(main)
