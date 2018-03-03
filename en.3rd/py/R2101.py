from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2101.x',
        MapIndex            = 100,
        MapDefaultBGM       = "ed60029",
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
        'Manoria Village',                      # 9
        'Varenne Lighthouse',                   # 10
        'Krone Trail',                          # 11
        'Polly',                                # 12
        'Target Camera',                        # 13
        'Clem',                                 # 14
        'Mary',                                 # 15
        'Daniel',                               # 16
        'Matron Theresa',                       # 17
        'Grant',                                # 18
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
        'ED6_DT07/CH02500 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH01260 ._CH',             # 05
        'ED6_DT26/CH20404 ._CH',             # 06
        'ED6_DT26/CH20707 ._CH',             # 07
        'ED6_DT26/CH20704 ._CH',             # 08
        'ED6_DT26/CH20703 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02500P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH01260P._CP',             # 05
        'ED6_DT26/CH20404P._CP',             # 06
        'ED6_DT26/CH20707P._CP',             # 07
        'ED6_DT26/CH20704P._CP',             # 08
        'ED6_DT26/CH20703P._CP',             # 09
    )

    DeclNpc(
        X                   = 13030,
        Z                   = -2070,
        Y                   = -137400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -72540,
        Z                   = -1880,
        Y                   = -134520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -18980,
        Z                   = -2000,
        Y                   = 6950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
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
        NpcIndex            = 0x80,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -22120,
        Y                   = -3060,
        Z                   = -30980,
        Range               = -12380,
        Unknown_10          = 0xBF4,
        Unknown_14          = 0xFFFF9098,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -20260,
        Y                   = -2980,
        Z                   = -48950,
        Range               = -29910,
        Unknown_10          = 0xBA4,
        Unknown_14          = 0xFFFF48AE,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -16190,
        Y                   = -3020,
        Z                   = -46690,
        Range               = 2410,
        Unknown_10          = 0xB9A,
        Unknown_14          = 0xFFFF41F6,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -67840,
        Y                   = -3000,
        Z                   = -116100,
        Range               = -78240,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFE30B8,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -16670,
        TriggerZ            = -1970,
        TriggerY            = -43720,
        TriggerRange        = 1500,
        ActorX              = -16670,
        ActorZ              = -300,
        ActorY              = -43720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20680,
        TriggerZ            = -2009,
        TriggerY            = -44860,
        TriggerRange        = 1500,
        ActorX              = -20680,
        ActorZ              = -350,
        ActorY              = -44860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_302",          # 00, 0
        "Function_1_329",          # 01, 1
        "Function_2_3A4",          # 02, 2
        "Function_3_8EE",          # 03, 3
        "Function_4_AC5",          # 04, 4
        "Function_5_CA6",          # 05, 5
        "Function_6_29FF",         # 06, 6
        "Function_7_2A63",         # 07, 7
        "Function_8_2ABA",         # 08, 8
    )


    def Function_0_302(): pass

    label("Function_0_302")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_328")
    OP_A2(0x1)
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_328")

    Return()

    # Function_0_302 end

    def Function_1_329(): pass

    label("Function_1_329")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFD0648, 0x23002C)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351")
    OP_22(0x1C4, 0x1, 0x64)

    label("loc_351")

    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_B2(0x0, 0x3, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_380")
    OP_B2(0x1, 0x0, 0x80)
    Jump("loc_385")

    label("loc_380")

    OP_B2(0x1, 0x3, 0x80)

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_3A3")
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A3")
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)

    label("loc_3A3")

    Return()

    # Function_1_329 end

    def Function_2_3A4(): pass

    label("Function_2_3A4")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x20000000)
    EventBegin(0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-17140, -1600, -30940, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -17140, -2000, -35940, 0)
    SetChrPos(0x14F, -17140, -2000, -37940, 0)

    def lambda_427():
        OP_8E(0xFE, 0xFFFFBD0C, 0xFFFFF830, 0xFFFFBDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_427)

    def lambda_442():
        OP_8E(0xFE, 0xFFFFBD0C, 0xFFFFF830, 0xFFFF96C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_442)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x8, 0x9, 0xC8, 0x5)
    Sleep(2000)
    OP_63(0x14E)
    Sleep(1000)

    def lambda_48F():
        OP_6D(-17140, -1600, -26940, 6000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_48F)

    def lambda_4A7():
        OP_6B(2520, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4A7)

    ChrTalk(    #0 op#A op#5
        0x14E,
        (
            "#1718F#50ASay, Polly? What do you think those happiness\x01",
            "stones are really like in person?\x05\x02\x03",

            "#55ADo you think Mr. O'Neil's right about them\x01",
            "glowing with a pretty golden light?\x05\x02\x03",

            "#1903F#40A*sigh* That'd be so wonderful... ㈱\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    WaitChrThread(0x14F, 0x1)
    WaitChrThread(0x14, 0x0)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14F, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14F)
    OP_8C(0x14F, 90, 400)
    Sleep(1000)

    ChrTalk(    #1
        0x14F,
        "#1733F...Huh?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14E, 0x1)
    FadeToDark(2000, 0, -1)

    def lambda_5F5():
        OP_6B(2420, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5F5)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x14E, -17380, -2000, -24340, 0)
    SetChrPos(0x14F, -14100, -2000, -23800, 0)
    OP_6D(-18980, -1600, -17900, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)

    def lambda_66A():
        OP_8E(0xFE, 0xFFFFB5DC, 0xFFFFF830, 0xFFFFBA14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_66A)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #2 op#A op#5
        0x14E,
        (
            "#1714F#45AI-I'm not saying that I believe him now or\x01",
            "anything! Far from it!\x05\x02\x03",

            "#1719F#42AI'm just saying if all he said IS true, it'd make\x01",
            "a perfect present for Matron Theresa... What\x01",
            "do you think?\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 180, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #3
        0x14E,
        "#1714FWait... Polly?!\x02",
    )

    CloseMessageWindow()

    def lambda_7B1():
        OP_6D(-18020, -1700, -26860, 2500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7B1)

    def lambda_7C9():
        OP_8E(0xFE, 0xFFFFB99C, 0xFFFFF830, 0xFFFF9714, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_7C9)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 140, 500)
    Sleep(800)
    OP_8C(0x14E, 260, 500)
    Sleep(1000)
    OP_8C(0x14E, 180, 500)
    Sleep(400)

    ChrTalk(    #4
        0x14E,
        "#1712FD-Don't tell me she's lost...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_8C(0x14E, 30, 500)
    Sleep(500)
    OP_8C(0x14E, 120, 500)
    Sleep(300)
    OP_8C(0x14E, 270, 500)
    Sleep(500)
    OP_8C(0x14E, 350, 500)
    Sleep(300)
    OP_63(0x14E)

    ChrTalk(    #5
        0x14E,
        "#1712F#3SPolly!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 500)
    Sleep(300)

    ChrTalk(    #6
        0x14E,
        "#1717F#3SPolly! Where are you?!#2S\x02",
    )

    CloseMessageWindow()
    RemoveParty(0x4E, 0x0)
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2F22)
    EventEnd(0x0)
    Return()

    # Function_2_3A4 end

    def Function_3_8EE(): pass

    label("Function_3_8EE")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-23280, -1910, -46940, 0)
    OP_67(0, 3580, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(82000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -24460, -1910, -47120, 228)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_8C(0x14E, 304, 400)
    Sleep(800)
    OP_8C(0x14E, 135, 400)
    Sleep(800)

    ChrTalk(    #7
        0x14E,
        "#1717F#3SPolly! Polly!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x14E, 228, 400)
    Sleep(500)

    ChrTalk(    #8
        0x14E,
        "#1715FI told her to stay close to me, too!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -12140, -2000, -44260, 308)

    def lambda_9FF():
        OP_8E(0xFE, 0xFFFFBB54, 0xFFFFF830, 0xFFFF7338, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9FF)

    def lambda_A1A():
        OP_6D(-23570, -1960, -45850, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_A1A)

    def lambda_A32():
        OP_67(0, 3580, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A32)

    def lambda_A4A():
        OP_6C(70000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_A4A)
    Sleep(4500)

    ChrTalk(    #9
        0x14E,
        (
            "#1713FWhere could she have gone...?\x02\x03",

            "#1716F*sigh* She's hopeless...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    SetChrFlags(0x13, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2F23)
    EventEnd(0x0)
    Return()

    # Function_3_8EE end

    def Function_4_AC5(): pass

    label("Function_4_AC5")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-11330, -2000, -46400, 0)
    OP_67(0, 4620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(277000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -10050, -2000, -46560, 135)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_8C(0x14E, 50, 400)
    Sleep(800)
    OP_8C(0x14E, 230, 400)
    Sleep(800)

    ChrTalk(    #10
        0x14E,
        "#1717F#3SPolly! Polly!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x14E, 135, 400)
    Sleep(500)

    ChrTalk(    #11
        0x14E,
        "#1715FOhh! I told her to stay close to me, too!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrPos(0x13, -19940, -2000, -43700, 0)

    def lambda_BE0():
        OP_8E(0xFE, 0xFFFFC824, 0xFFFFF830, 0xFFFF7400, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BE0)

    def lambda_BFB():
        OP_6D(-12720, -2000, -44240, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_BFB)

    def lambda_C13():
        OP_67(0, 4620, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C13)

    def lambda_C2B():
        OP_6C(280000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_C2B)
    Sleep(4500)

    ChrTalk(    #12
        0x14E,
        (
            "#1713FWhere could she have gone...?\x02\x03",

            "#1716F*sigh* She's hopeless...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    SetChrFlags(0x13, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2F23)
    EventEnd(0x0)
    Return()

    # Function_4_AC5 end

    def Function_5_CA6(): pass

    label("Function_5_CA6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_23(0x1C4)
    OP_6D(-12640, -1900, -34160, 0)
    OP_67(0, 4360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(43000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14E, -12640, -2300, -34160, 260)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x19, -13040, -2000, -35500, 346)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrPos(0x13, -14100, -2000, -34800, 100)
    SetChrChipByIndex(0x14E, 9)
    SetChrSubChip(0x14E, 0)
    SetChrFlags(0x14E, 0x2)
    SetChrFlags(0x14E, 0x4)
    SetChrFlags(0x14E, 0x800)
    LoadEffect(0x0, "map\\mp074_00.eff")
    LoadEffect(0x1, "map\\mp075_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    Sleep(3000)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #13
        "\x07\x00...Hey, are you okay?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #14
        "\x07\x00Wake up!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_59()
    OP_22(0x1C4, 0x1, 0x64)
    OP_1D(0x76)
    FadeToBright(2000, 0)

    def lambda_E0B():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_E0B)
    Sleep(1000)

    def lambda_E20():
        OP_9E(0xFE, 0x5, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14E, 3, lambda_E20)
    Sleep(1000)
    Fade(1000)
    SetChrChipByIndex(0x14E, 8)
    SetChrSubChip(0x14E, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_E74")

    ChrTalk(    #15
        0x19,
        "#821FOh, good. She woke up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E9D")

    label("loc_E74")


    NpcTalk(    #16
        0x19,
        "Man",
        "#821F#12POh, good. She woke up.\x02",
    )

    CloseMessageWindow()

    label("loc_E9D")


    ChrTalk(    #17
        0x13,
        "#1731F#6PYou okay, Mary?\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0xFFFFFF38, 1500, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)

    def lambda_EE0():
        OP_99(0xFE, 0x0, 0x4, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_EE0)
    WaitChrThread(0x14E, 0x2)

    def lambda_EF5():
        OP_99(0xFE, 0x4, 0x3, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_EF5)
    WaitChrThread(0x14E, 0x2)

    def lambda_F0A():
        OP_99(0xFE, 0x3, 0x4, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_F0A)
    WaitChrThread(0x14E, 0x2)

    def lambda_F1F():
        OP_99(0xFE, 0x4, 0x2, 0x320)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_F1F)
    WaitChrThread(0x14E, 0x2)
    Fade(500)
    SetChrSubChip(0x14E, 5)
    Sleep(900)
    SetChrSubChip(0x14E, 7)
    Sleep(800)
    SetChrSubChip(0x14E, 5)
    Sleep(150)
    SetChrSubChip(0x14E, 6)
    Sleep(800)

    ChrTalk(    #18
        0x14E,
        (
            "#1714F#5PH-Huh?\x02\x03",

            "...?\x02\x03",

            "What happened to that weird monster?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_FD2")

    ChrTalk(    #19
        0x19,
        "#822F#12PMonster?! Were you attacked?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1002")

    label("loc_FD2")


    NpcTalk(    #20
        0x19,
        "Man",
        "#822F#12PMonster?! Were you attacked?!\x02",
    )

    CloseMessageWindow()

    label("loc_1002")

    SetChrSubChip(0x14E, 5)

    ChrTalk(    #21
        0x14E,
        "#1714F#5PNo, but...\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x13, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(100)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x13)
    OP_63(0x19)

    ChrTalk(    #22
        0x13,
        "#1733F#6PThere wasn't any monsters... Just you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14E,
        (
            "#1900F#5PTh-That's weird...\x02\x03",

            "#1713FWas that all a dream, then...?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, -12740, -2009, -44900, 350)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x40)
    SetChrPos(0x17, -11980, -2009, -45880, 350)
    Sleep(500)

    ChrTalk(    #24
        0x15,
        "#774F#3S#1PMary!#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x17,
        "#1722F#1PMaryyy!\x02",
    )

    CloseMessageWindow()

    def lambda_1145():
        OP_6D(-12020, -2000, -36520, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1145)

    def lambda_115D():
        OP_6C(44000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_115D)
    WaitChrThread(0x14, 0x0)

    def lambda_1172():
        OP_8E(0xFE, 0xFFFFCD10, 0xFFFFF830, 0xFFFF7554, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1172)

    def lambda_118D():
        OP_8E(0xFE, 0xFFFFD058, 0xFFFFF830, 0xFFFF72D4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_118D)

    def lambda_11A8():

        label("loc_11A8")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_11A8")

    QueueWorkItem2(0x13, 3, lambda_11A8)

    def lambda_11B9():

        label("loc_11B9")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_11B9")

    QueueWorkItem2(0x19, 3, lambda_11B9)
    Sleep(500)
    SetChrSubChip(0x14E, 7)

    def lambda_11D4():
        OP_8F(0xFE, 0xFFFFC568, 0xFFFFF830, 0xFFFF7298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_11D4)

    def lambda_11EF():
        OP_8F(0xFE, 0xFFFFC658, 0xFFFFF830, 0xFFFF7748, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_11EF)
    Sleep(100)

    def lambda_120F():
        OP_6D(-12500, -2000, -34500, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_120F)

    def lambda_1227():
        OP_6B(2860, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1227)

    def lambda_1237():
        OP_6E(254, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1237)
    WaitChrThread(0x19, 0x1)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x17, 0x1)
    OP_44(0x19, 0x3)
    OP_44(0x13, 0x3)
    TurnDirection(0x19, 0x15, 400)
    TurnDirection(0x13, 0x14E, 400)
    Sleep(300)

    ChrTalk(    #26
        0x15,
        "#775F#12PA-Are you okay?!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x14E, 65535)
    SetChrSubChip(0x14E, 0)
    ClearChrFlags(0x14E, 0x2)
    ClearChrFlags(0x14E, 0x4)
    ClearChrFlags(0x14E, 0x800)
    TurnDirection(0x14E, 0x15, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0x14E,
        "#1714F#5PY-Yeah. I'm fine...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0x15,
        "#778F#12P#3SHow can you be fine?!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x15,
        (
            "#775F#12PI promised Kloe and Joshua that I'd protect\x01",
            "everyone! I promised!\x02\x03",

            "#773FIf anything happened to you, I...I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x14E,
        "#1714F#5PClem...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    OP_8C(0x15, 180, 500)
    Sleep(400)

    ChrTalk(    #31
        0x15,
        (
            "#773F#6PWh-Why do you always gotta try and do\x01",
            "crazy things alone, anyway?!\x02\x03",

            "#773FWe were all gonna look for the matron's\x01",
            "birthday present together...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 0, 500)
    Sleep(400)

    ChrTalk(    #32
        0x15,
        (
            "#778F#12P#3SDon't go off and start doin' dangerous\x01",
            "stuff all by yourself!#2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14E,
        "#1713F#5P..I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x17,
        (
            "#1722F#12PHe's right, Mary!\x02\x03",

            "We were real worried about you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x13,
        (
            "#1731F#6PWe were all looking for you together...\x02\x03",

            "...'cause you went and disappeared on us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x14E, 270, 400)
    Sleep(500)
    OP_8C(0x14E, 180, 400)
    Sleep(300)

    ChrTalk(    #36
        0x14E,
        (
            "#1713F#5PI...\x02\x03",

            "#1710FI'm sorry...\x02\x03",

            "#1719F...and thanks.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #37
        0x15,
        (
            "#774F#12P...H-Huh?!\x02\x03",

            "#773FWh-What're you thanking us for?!\x02\x03",

            "#773FI wasn't worried or nothin'. I just figured\x01",
            "we could look for you while looking for a\x01",
            "present...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x17,
        (
            "#1721F#12PUmm... You remember how Clem forgot to buy\x01",
            "those decorations when he was in Mr. O'Neil's\x01",
            "shop, right?\x02\x03",

            "That was why we went over to the bazaar to do\x01",
            "a bunch of shopping there, so we could get what\x01",
            "we needed for Matron's birthday.\x02\x03",

            "#1720FHe said we had to go do it 'cause it'd be a big\x01",
            "pain in the butt for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    TurnDirection(0x15, 0x17, 500)
    Sleep(400)

    ChrTalk(    #39
        0x15,
        "#776F#6PShhh! Don't tell her everything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x17,
        (
            "#1721F#12PAnyway, then we headed over to the\x01",
            "Krone trail aaand...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_187B():
        OP_8E(0xFE, 0xFFFFCF2C, 0xFFFFF830, 0xFFFF7428, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_187B)
    WaitChrThread(0x15, 0x1)
    OP_22(0x7D, 0x0, 0x64)

    def lambda_18A0():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_18A0)

    def lambda_18BA():
        OP_8F(0xFE, 0xFFFFCD10, 0xFFFFF830, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_18BA)
    WaitChrThread(0x15, 0x1)

    def lambda_18DA():
        OP_8E(0xFE, 0xFFFFCF2C, 0xFFFFF830, 0xFFFF7428, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_18DA)
    WaitChrThread(0x15, 0x1)
    OP_22(0x7D, 0x0, 0x64)

    def lambda_18FF():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_18FF)

    def lambda_1919():
        OP_8F(0xFE, 0xFFFFCD10, 0xFFFFF830, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1919)
    WaitChrThread(0x15, 0x1)
    Sleep(300)
    TurnDirection(0x17, 0x15, 500)

    ChrTalk(    #41
        0x17,
        "#1723F#12POwwwwww! Y-You're hurting me, Clem!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x14E,
        (
            "#1710F#5P...\x02\x03",

            "(Heehee... I feel so happy for some reason.)\x02\x03",

            "#1719F(...I feel like I just had a dream.)\x02\x03",

            "(A really, really nice dream...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1600)

    def lambda_1A1D():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1A1D)
    Sleep(150)
    OP_8C(0x17, 0, 500)
    Sleep(250)

    ChrTalk(    #43
        0x15,
        (
            "#775F#12PM-Mary?!\x02\x03",

            "Are you okay? You aren't feeling sick or\x01",
            "something, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x19, 0x3)

    def lambda_1A95():

        label("loc_1A95")

        TurnDirection(0xFE, 0x14E, 400)
        OP_48()
        Jump("loc_1A95")

    QueueWorkItem2(0x19, 3, lambda_1A95)

    def lambda_1AA6():
        OP_8F(0xFE, 0xFFFFCA68, 0xFFFFF830, 0xFFFF76E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1AA6)
    WaitChrThread(0x19, 0x1)

    def lambda_1AC6():
        OP_8F(0xFE, 0xFFFFCB6C, 0xFFFFF830, 0xFFFF7A40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1AC6)
    WaitChrThread(0x19, 0x1)
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0x19, 6)
    SetChrSubChip(0x19, 1)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(    #44
        0x19,
        "#822F#1PAre you all right? Feeling dizzy or nauseous?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B7E")

    label("loc_1B3F")


    NpcTalk(    #45
        0x19,
        "Man",
        "#822F#1PAre you all right? Feeling dizzy or nauseous?\x02",
    )

    CloseMessageWindow()

    label("loc_1B7E")

    OP_63(0x14E)
    OP_8C(0x14E, 260, 400)
    Sleep(500)

    ChrTalk(    #46
        0x14E,
        (
            "#1714F#2POh, I'm fine.\x02\x03",

            "#1710FHeehee. I was just spacing out a little.\x01",
            "A lot's happened, you see...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_1C1E")

    ChrTalk(    #47
        0x19,
        "#820F#1PHeh. Okay, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA3")

    label("loc_1C1E")


    NpcTalk(    #48
        0x19,
        "Man",
        "#820F#1PHeh. Okay, then.\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #49
        0x14E,
        (
            "#1714F#2P(...Oh! I remember now.)\x02\x03",

            "#1718F(His name's Grant, isn't it?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA3")

    Fade(500)
    SetChrChipByIndex(0x19, 5)
    SetChrSubChip(0x19, 0)
    Sleep(500)
    OP_44(0x19, 0x3)
    OP_8C(0x19, 180, 400)
    Sleep(500)

    ChrTalk(    #50
        0x19,
        "#821F#5P...Okay, troops! Let's start heading back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x15,
        "#775F#12PWhaaat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x17,
        "#1723F#12PB-But we still haven't found a present yet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x19,
        (
            "#820F#5PMaybe not, but you're all downright exhausted\x01",
            "from looking around for one.\x02\x03",

            "#821FThe young lady here looks like she could do\x01",
            "with some serious napping, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #54
        0x14E,
        "#1714F#2PI-I'm fine, honestly...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x14E, 500)
    Sleep(400)

    ChrTalk(    #55
        0x19,
        (
            "#823F#1PNope. Not hearing it.\x02\x03",

            "#820FI'll escort you all back home, so take it easy and\x01",
            "get some rest for today.\x02\x03",

            "If any of you were to get sick from overexerting \x01",
            "themselves, the matron would be really upset,\x01",
            "wouldn't she?\x02\x03",

            "#821FYou can always keep searching for a present\x01",
            "tomorrow. I'll give you a hand, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x17,
        "#1721F#12PWow! Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x13,
        "#1733F#6PYou're pretty cool for a guy who looks so boring!\x02",
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x19, 0x13, 400)
    Sleep(300)

    ChrTalk(    #58
        0x19,
        (
            "#823F#5POuch... Just kick me down while you're at it,\x01",
            "why don'cha?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_204D():
        OP_8E(0xFE, 0xFFFFC8EC, 0xFFFFF830, 0xFFFF7518, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_204D)
    WaitChrThread(0x19, 0x1)

    def lambda_206D():
        OP_6D(-12500, -2000, -36500, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_206D)

    def lambda_2085():
        OP_8E(0xFE, 0xFFFFC8EC, 0xFFFFF830, 0xFFFF65DC, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2085)
    Sleep(200)

    def lambda_20A5():
        OP_8E(0xFE, 0xFFFFC658, 0xFFFFF830, 0xFFFF6C6C, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_20A5)
    Sleep(50)

    def lambda_20C5():
        OP_8E(0xFE, 0xFFFFCD10, 0xFFFFF830, 0xFFFF6C94, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_20C5)
    Sleep(50)

    def lambda_20E5():
        OP_8E(0xFE, 0xFFFFCFF4, 0xFFFFF830, 0xFFFF69C4, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_20E5)
    Sleep(50)

    def lambda_2105():
        OP_8E(0xFE, 0xFFFFCE00, 0xFFFFF830, 0xFFFF7284, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2105)
    WaitChrThread(0x14E, 0x1)
    PlayEffect(0x0, 0x0, 0xFF, -12980, -1500, -36420, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    Fade(500)
    SetChrChipByIndex(0x14E, 7)
    SetChrSubChip(0x14E, 0)
    Sleep(500)

    ChrTalk(    #59
        0x14E,
        "#1714F#5PHuh? What's this...?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x1)

    def lambda_21B5():
        TurnDirection(0xFE, 0x14E, 400)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_21B5)
    Sleep(100)
    WaitChrThread(0x17, 0x1)

    def lambda_21CD():
        TurnDirection(0xFE, 0x14E, 400)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_21CD)
    Sleep(70)
    WaitChrThread(0x13, 0x1)

    def lambda_21E5():
        TurnDirection(0xFE, 0x14E, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_21E5)
    Sleep(120)
    WaitChrThread(0x19, 0x1)

    def lambda_21FD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_21FD)
    OP_82(0x0, 0x2)
    OP_22(0x80, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0xFF, -12980, -1400, -36420, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x96, 0x1)
    OP_62(0x17, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    OP_62(0x15, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    OP_62(0x13, 0x0, 1600, 0x2, 0x7, 0x96, 0x1)
    Sleep(1000)
    OP_63(0x19)
    OP_63(0x17)
    OP_63(0x15)
    OP_63(0x13)
    Sleep(300)

    ChrTalk(    #60
        0x19,
        "#825F#12PWow... That looks...\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #61
        0x17,
        "#1723F#12PYou don't think that could be...?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #62
        0x15,
        "#774F#3S#12PWhoa!!#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x13,
        "#1732F#6PIt's a happiness stone!\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(2000)
    OP_63(0x14E)
    Sleep(500)

    ChrTalk(    #64
        0x14E,
        (
            "#1710F#5P...Yeah.\x02\x03",

            "#1903FIt must be!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23AE():
        OP_6B(2760, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_23AE)
    FadeToDark(2000, 0, -1)
    OP_24(0x1C4, 0x5A)
    Sleep(300)
    OP_24(0x1C4, 0x50)
    Sleep(300)
    OP_24(0x1C4, 0x46)
    Sleep(300)
    OP_24(0x1C4, 0x3C)
    Sleep(300)
    OP_24(0x1C4, 0x32)
    Sleep(300)
    OP_24(0x1C4, 0x28)
    Sleep(300)
    OP_24(0x1C4, 0x1E)
    Sleep(300)
    OP_23(0x1C4)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_C4(0x0, 0x800)
    Sleep(500)

    AnonymousTalk(    #65
        (
            "\x18\x07\x0C#40WClem suddenly chimed that he had an idea as\x01",
            "he took an old pendant out of his pocket.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #66
        (
            "\x18\x07\x0C#40WHe'd grumbled that it was only something he\x01",
            "stumbled upon at the bazaar.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #67
        (
            "\x18\x07\x0C#40WWith everyone's encouragement, I decided to\x01",
            "try setting the happiness stone in the center\x01",
            "in hopes that it would fit.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #68
        (
            "\x18\x07\x0C#40W...It fit perfectly, too! It was as if they were\x01",
            "always meant to be together.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #69
        (
            "\x18\x07\x0C#40WPolly's golden chain turned out to be the perfect\x01",
            "length as well.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #70
        (
            "\x18\x07\x0C#40WFinally, we placed it in the small box that Daniel\x01",
            "had kept with him, wrapped it in wrapping paper,\x01",
            "and the perfect necklace was born.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS355._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS357._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS358._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(4000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(140, 320, -1, -1)
    SetChrName("Mary")

    AnonymousTalk(    #71
        (
            "\x07\x0C#40WHuh? This is the same smell that monster\x01",
            "gave off...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Mary")

    AnonymousTalk(    #72
        (
            "\x07\x0C#40WIs that because I gave her the happiness\x01",
            "stone?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(280, 240, -1, -1)
    SetChrName("Matron Theresa")

    AnonymousTalk(    #73
        "\x07\x0C#40W...Mary?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(2000)
    SetMessageWindowPos(130, 320, -1, -1)
    SetChrName("Mary")

    AnonymousTalk(    #74
        "\x07\x0C#40W...I understand now.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(130, 320, -1, -1)
    SetChrName("Mary")

    AnonymousTalk(    #75
        "\x07\x0C#40WIt's the warm smell of happiness.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x20000000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_F7(0xA, 0x5, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #76
        "\x07\x00Side Story [The Happiness Stone] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F2")
    Sleep(1000)
    OP_28(0x6, 0x4, 0x10)
    OP_28(0x6, 0x4, 0x20)
    OP_3E(0x12D, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05Received \x1F\x2D\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(12000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #78
        "\x07\x05Received \x07\x0212,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_29F2")

    OP_A2(0x2505)
    NewScene("ED6_DT21/U2600   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_5_CA6 end

    def Function_6_29FF(): pass

    label("Function_6_29FF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #79
        (
            "\x07\x05East: Ruan - 374 selge\x01",
            "Manoria Village - 63 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_29FF end

    def Function_7_2A63(): pass

    label("Function_7_2A63")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #80
        "\x07\x05South: Varenne Lighthouse - 70 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_2A63 end

    def Function_8_2ABA(): pass

    label("Function_8_2ABA")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B45")

    ChrTalk(    #81
        0x14E,
        (
            "#1714FThis way leads to the lighthouse,\x01",
            "doesn't it?\x02\x03",

            "#1900FHow did we get so turned around?\x01",
            "The bazaar's back in Manoria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC1")

    label("loc_2B45")


    ChrTalk(    #82
        0x14E,
        (
            "#1714FThis way leads to the lighthouse,\x01",
            "doesn't it?\x02\x03",

            "How did we get so turned around?\x01",
            "The bazaar's back in Manoria.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2BC1")

    OP_59()
    Fade(1000)
    SetChrPos(0x14E, -73000, -1950, -114600, 0)
    SetChrPos(0x14F, -73000, -1950, -114600, 0)
    OP_6D(-73000, -1950, -114000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_8_2ABA end

    SaveToFile()

Try(main)
