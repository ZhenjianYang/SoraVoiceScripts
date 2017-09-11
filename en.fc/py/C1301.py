from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1301   ._SN',
        MapName             = 'Bose',
        Location            = 'C1301.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60031",
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
        'Kyle',                                 # 9
        'Josette',                              # 10
        'Sky Bandit Aaron',                     # 11
        'Sky Bandit Lonnie',                    # 12
        'Sky Bandit Dino',                      # 13
        'Sky Bandit Lyall',                     # 14
        'Sky Bandit Rosco',                     # 15
        'Sky Bandit Ryan',                      # 16
        ' ',                                    # 17
        ' ',                                    # 18
        ' ',                                    # 19
        ' ',                                    # 20
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02120 ._CH',             # 00
        'ED6_DT07/CH02130 ._CH',             # 01
        'ED6_DT07/CH01380 ._CH',             # 02
        'ED6_DT07/CH00360 ._CH',             # 03
        'ED6_DT06/CH20074 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00101 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT07/CH00111 ._CH',             # 08
        'ED6_DT07/CH00120 ._CH',             # 09
        'ED6_DT07/CH00121 ._CH',             # 0A
        'ED6_DT07/CH00130 ._CH',             # 0B
        'ED6_DT07/CH00131 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02120P._CP',             # 00
        'ED6_DT07/CH02130P._CP',             # 01
        'ED6_DT07/CH01380P._CP',             # 02
        'ED6_DT07/CH00360P._CP',             # 03
        'ED6_DT06/CH20074P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00101P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT07/CH00111P._CP',             # 08
        'ED6_DT07/CH00120P._CP',             # 09
        'ED6_DT07/CH00121P._CP',             # 0A
        'ED6_DT07/CH00130P._CP',             # 0B
        'ED6_DT07/CH00131P._CP',             # 0C
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 500,
        Y                   = 500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 500,
        Y                   = -2800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -11400,
        TriggerZ            = 4000,
        TriggerY            = -2400,
        TriggerRange        = 1500,
        ActorX              = -8930,
        ActorZ              = 6520,
        ActorY              = -880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9150,
        TriggerZ            = 5540,
        TriggerY            = -590,
        TriggerRange        = 1000,
        ActorX              = -10940,
        ActorZ              = 5000,
        ActorY              = -1870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2DA",          # 00, 0
        "Function_1_338",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_34F",          # 03, 3
        "Function_4_138E",         # 04, 4
        "Function_5_1468",         # 05, 5
        "Function_6_1519",         # 06, 6
        "Function_7_15CA",         # 07, 7
        "Function_8_16AE",         # 08, 8
        "Function_9_1706",         # 09, 9
        "Function_10_1750",        # 0A, 10
        "Function_11_178C",        # 0B, 11
        "Function_12_17BA",        # 0C, 12
        "Function_13_189E",        # 0D, 13
        "Function_14_18F6",        # 0E, 14
        "Function_15_1940",        # 0F, 15
        "Function_16_197C",        # 10, 16
    )


    def Function_0_2DA(): pass

    label("Function_0_2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2E8")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_END)), "loc_337")
    SetChrPos(0xD, -11640, 4000, 6760, 55)
    SetChrPos(0xF, -13460, 4000, 7840, 312)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xF, 0x1)
    OP_44(0xD, 0xFF)
    OP_44(0xF, 0xFF)
    SetChrChipByIndex(0xD, 4)
    SetChrChipByIndex(0xF, 4)

    label("loc_337")

    Return()

    # Function_0_2DA end

    def Function_1_338(): pass

    label("Function_1_338")

    Return()

    # Function_1_338 end

    def Function_2_339(): pass

    label("Function_2_339")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_339")

    label("loc_34E")

    Return()

    # Function_2_339 end

    def Function_3_34F(): pass

    label("Function_3_34F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-13163, 5000, -2170, 0)
    SetChrPos(0x101, -4230, 4000, -2740, 0)
    SetChrPos(0x102, -4230, 4000, -2740, 0)
    SetChrPos(0x103, -4230, 4000, -2740, 0)
    SetChrPos(0x104, -4230, 4000, -2740, 0)
    SetChrPos(0xA, -4230, 4000, -2740, 0)
    SetChrPos(0xB, -4230, 4000, -2740, 0)
    SetChrPos(0xC, -4230, 4000, -2740, 0)
    SetChrPos(0xD, -4230, 4000, -2740, 0)
    SetChrPos(0xE, -4230, 4000, -2740, 0)
    SetChrPos(0xF, -4230, 4000, -2740, 0)
    SetChrPos(0x9, -4230, 4000, -2740, 0)
    SetChrPos(0x8, -4230, 4000, -2740, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    OP_6D(2350, 4000, -39840, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(5220, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_6D(-5000, 4000, -980, 6000)
    Fade(1000)
    OP_6D(-3670, 4000, 210, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_587():
        OP_6D(-10920, 4000, -1950, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_587)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    OP_43(0x8, 0x1, 0x0, 0x4)
    Sleep(600)
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(1200)
    OP_43(0xA, 0x1, 0x0, 0x4)
    Sleep(600)
    OP_43(0xB, 0x1, 0x0, 0x4)
    Sleep(600)
    OP_43(0xC, 0x1, 0x0, 0x4)
    Sleep(600)
    OP_43(0xE, 0x1, 0x0, 0x4)
    Sleep(1500)
    OP_43(0xD, 0x1, 0x0, 0x5)
    Sleep(1000)
    OP_43(0xF, 0x1, 0x0, 0x6)
    Sleep(1500)

    def lambda_610():
        OP_6D(-12340, 4000, -15850, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_610)
    WaitChrThread(0xD, 0x1)

    def lambda_62D():

        label("loc_62D")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_62D")

    QueueWorkItem2(0xD, 2, lambda_62D)
    WaitChrThread(0xF, 0x1)

    def lambda_643():

        label("loc_643")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_643")

    QueueWorkItem2(0xF, 2, lambda_643)

    ChrTalk(    #0
        0xD,
        (
            "#2P*yaaaawn*\x01",
            "Boy, am I tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xD,
        (
            "#2PEver since we came here my night and\x01",
            "day have been completely reversed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        (
            "#1PWe've just got to tough things out\x01",
            "a little longer and then we can say\x01",
            "goodbye to this horrible life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xF,
        (
            "#1PWith Don as our leader,\x01",
            "we can't go wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xD,
        (
            "#2PBut...don't you think Don's been\x01",
            "acting a little strange lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xD,
        (
            "#2PI mean, he's kind of scary to\x01",
            "talk to these days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xF,
        "#1PHow about you knock that crap off?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xF,
        (
            "#1PIf Kyle or Josette heard you talking\x01",
            "like that, they'd beat you upside the\x01",
            "head!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        "#2PB-But it's just that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xF,
        (
            "#1PI'm sure you're just tired from\x01",
            "lack of sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xF,
        (
            "#1PLet's hurry and finish up here\x01",
            "and get some rest.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 7)
    SetChrChipByIndex(0x103, 9)
    SetChrChipByIndex(0x104, 11)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x104, 0x80)
    SetChrPos(0x101, -12840, 4000, -6330, 180)
    SetChrPos(0x102, -12790, 4000, -4890, 180)
    SetChrPos(0x103, -11570, 4000, -5960, 180)
    SetChrPos(0x104, -11540, 4000, -4420, 180)

    NpcTalk(    #11
        0x101,
        "Girl's Voice",
        (
            "#2PYou're welcome to take a rest\x01",
            "now if you'd like.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_9E7():

        label("loc_9E7")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_9E7")

    QueueWorkItem2(0xF, 2, lambda_9E7)

    def lambda_9F8():

        label("loc_9F8")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_9F8")

    QueueWorkItem2(0xD, 2, lambda_9F8)

    def lambda_A09():
        OP_6D(-12270, 4000, -10410, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A09)
    Sleep(1200)

    ChrTalk(    #12
        0xF,
        "Ah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xD,
        "You... You're those...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#006FYou're too late!\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_A8A():
        OP_6D(-12970, 4000, -14070, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A8A)

    def lambda_AA2():
        OP_8E(0x101, 0xFFFFCC98, 0xFA0, 0xFFFFCCAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA2)
    Sleep(100)
    SetChrChipByIndex(0xF, 3)

    def lambda_AC7():
        OP_8E(0x103, 0xFFFFD1A2, 0xFA0, 0xFFFFCDD8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC7)
    Sleep(100)
    SetChrChipByIndex(0xD, 3)

    def lambda_AEC():
        OP_8E(0x102, 0xFFFFC856, 0xFA0, 0xFFFFD274, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEC)
    Sleep(100)

    def lambda_B0C():
        OP_8E(0x104, 0xFFFFCD88, 0xFA0, 0xFFFFD530, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B0C)
    Sleep(300)
    Battle(0x388, 0x0, 0x2, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_B3F"),
        (SWITCH_DEFAULT, "loc_B44"),
    )


    label("loc_B3F")

    OP_B4(0x0)
    Jump("loc_B44")

    label("loc_B44")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xF, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrPos(0x101, -13670, 4000, 2920, 141)
    SetChrPos(0x102, -12270, 4000, 2580, 171)
    SetChrPos(0x103, -13420, 4000, 800, 90)
    SetChrPos(0x104, -12130, 4000, 800, 325)
    SetChrPos(0xD, -11640, 4000, 6760, 55)
    SetChrPos(0xF, -13460, 4000, 7840, 312)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xF, 0x1)
    OP_44(0xD, 0xFF)
    OP_44(0xF, 0xFF)
    SetChrChipByIndex(0xD, 4)
    SetChrChipByIndex(0xF, 4)
    OP_6D(-11980, 4000, 1620, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(1000)

    ChrTalk(    #15
        0x104,
        (
            "#030F#6PWhew... It looks like we were able\x01",
            "to get in here without any trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        (
            "#027FI'm amazed that this little plan\x01",
            "actually worked.\x02\x03",

            "I guess we all have you to\x01",
            "thank this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#009F#5PBut seriously, I was getting\x01",
            "pretty nervous.\x02\x03",

            "I wasn't sure what we were going to\x01",
            "do if we got caught stowing away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#010FWell, even if we were discovered, we'd just have\x01",
            "to take control of the airship.\x02\x03",

            "And we would've had an advantage fighting against\x01",
            "this lot in those tight quarters. Superior numbers\x01",
            "mean nothing without space to maneuver in.\x02\x03",

            "Olivier... So you thought that far ahead,\x01",
            "taking all of these factors into account,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x104,
        (
            "#031F#6PNot in a million years.\x01",
            "Are you kidding?\x02\x03",

            "I simply thought it would be fun\x01",
            "to infiltrate an enemy base.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x101,
        (
            "#007F#5PI think we would have been better\x01",
            "off if you said nothing at all...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #21
        0x103,
        (
            "#021FGive the poor guy a break. At least\x01",
            "we were able to get in here without\x01",
            "incident.\x02\x03",

            "#020FAnyway...this looks like somewhere\x01",
            "in the Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 200)

    ChrTalk(    #22
        0x101,
        (
            "#501F#1PThe Nebel Valley? Like the one on\x01",
            "the border of Bose and Rolent?\x02\x03",

            "Well, that explains why it's so\x01",
            "misty outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#010FAnd this is definitely terrain covered with\x01",
            "extreme differences in height which prevent\x01",
            "the landing of any large aircraft...\x02\x03",

            "It looks like your guess was right, Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        (
            "#026FYeah, well, it didn't seem to help\x01",
            "us much in getting in here.\x02\x03",

            "#020FBut anyhow...we don't have time\x01",
            "to be hanging around here.\x02\x03",

            "We'll need to subdue the sky bandits\x01",
            "and ensure the safety of the hostages\x01",
            "being held captive.\x02\x03",

            "And of course, your father,\x01",
            "Cassius, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#006F#1PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#012FUnderstood!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x104, 0x40)
    Sleep(100)
    Fade(1000)
    OP_6D(-12990, 4000, 980, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -12990, 4000, 980, 141)
    SetChrPos(0x102, -12990, 4000, 980, 141)
    SetChrPos(0x103, -12990, 4000, 980, 141)
    SetChrPos(0x104, -12990, 4000, 980, 141)
    OP_0D()
    OP_A2(0x353)
    OP_28(0x39, 0x1, 0x1)
    OP_28(0x39, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_3_34F end

    def Function_4_138E(): pass

    label("Function_4_138E")

    SetChrPos(0xFE, -3290, 5600, -1690, 262)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFEEC6, 0x15E0, 0xFFFFF8DA, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFECB4, 0x17F2, 0xFFFFFFEC, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDC1A, 0x15A4, 0xFFFFFDF8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 400)
    OP_96(0xFE, 0xFFFFD4AE, 0xFA0, 0xFFFFFEB6, 0x258, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFCD06, 0xFA0, 0xFFFFFCA4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFCCB6, 0xFA0, 0xFFFFBED8, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFBD98, 0xFA0, 0xFFFFBDD4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFBD66, 0x0, 0xFFFFDEA4, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_138E end

    def Function_5_1468(): pass

    label("Function_5_1468")

    SetChrPos(0xFE, -3290, 5600, -1690, 262)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFEEC6, 0x15E0, 0xFFFFF8DA, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFECB4, 0x17F2, 0xFFFFFFEC, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDC1A, 0x15A4, 0xFFFFFDF8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 400)
    OP_96(0xFE, 0xFFFFD4AE, 0xFA0, 0xFFFFFEB6, 0x258, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFCA54, 0xFA0, 0xFFFFFCA4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFCA54, 0xFA0, 0xFFFFC4AA, 0xFA0, 0x0)
    OP_4A(0xFE, 255)
    Return()

    # Function_5_1468 end

    def Function_6_1519(): pass

    label("Function_6_1519")

    SetChrPos(0xFE, -3290, 5600, -1690, 262)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFEEC6, 0x15E0, 0xFFFFF8DA, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFECB4, 0x17F2, 0xFFFFFFEC, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDC1A, 0x15A4, 0xFFFFFDF8, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 400)
    OP_96(0xFE, 0xFFFFD4AE, 0xFA0, 0xFFFFFEB6, 0x258, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFD058, 0xFA0, 0xFFFFFCA4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFD058, 0xFA0, 0xFFFFC77A, 0xFA0, 0x0)
    OP_4A(0xFE, 255)
    Return()

    # Function_6_1519 end

    def Function_7_15CA(): pass

    label("Function_7_15CA")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0xB)
    OP_43(0x1, 0x1, 0x0, 0xA)
    OP_43(0x2, 0x1, 0x0, 0x9)
    OP_43(0x3, 0x1, 0x0, 0x8)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_7_15CA end

    def Function_8_16AE(): pass

    label("Function_8_16AE")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_16AE end

    def Function_9_1706(): pass

    label("Function_9_1706")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_1706 end

    def Function_10_1750(): pass

    label("Function_10_1750")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_1750 end

    def Function_11_178C(): pass

    label("Function_11_178C")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 90, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFDD3C, 0x1586, 0xFFFFFD80, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_178C end

    def Function_12_17BA(): pass

    label("Function_12_17BA")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x10)
    OP_43(0x1, 0x1, 0x0, 0xF)
    OP_43(0x2, 0x1, 0x0, 0xE)
    OP_43(0x3, 0x1, 0x0, 0xD)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_12_17BA end

    def Function_13_189E(): pass

    label("Function_13_189E")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_189E end

    def Function_14_18F6(): pass

    label("Function_14_18F6")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_14_18F6 end

    def Function_15_1940(): pass

    label("Function_15_1940")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_15_1940 end

    def Function_16_197C(): pass

    label("Function_16_197C")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFD508, 0xFA0, 0xFFFFF83A, 0x1F4, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_197C end

    SaveToFile()

Try(main)
