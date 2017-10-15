from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3108   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3108.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Cassius',                              # 9
        'Patrol Ship',                          # 10
        'Patrol Ship',                          # 11
        'Patrol Ship',                          # 12
        'Patrol Ship',                          # 13
        'Lt. Colonel Cid',                      # 14
        'Maintenance Chief Gustav',             # 15
        'Faye',                                 # 16
        'Mechanic',                             # 17
        'Mechanic',                             # 18
        'Mechanic',                             # 19
        'Mechanic',                             # 20
        'Factory Ship',                         # 21
        '工房船影',                             # 22
        'アルセイユの影',                       # 23
        '警備艇影',                             # 24
        '警備艇影',                             # 25
        '警備艇影',                             # 26
        '警備艇影',                             # 27
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT07/CH02440 ._CH',             # 02
        'ED6_DT07/CH01550 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT07/CH02440P._CP',             # 02
        'ED6_DT07/CH01550P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_332",          # 00, 0
        "Function_1_375",          # 01, 1
        "Function_2_376",          # 02, 2
        "Function_3_E18",          # 03, 3
        "Function_4_E61",          # 04, 4
        "Function_5_EAA",          # 05, 5
        "Function_6_EF3",          # 06, 6
        "Function_7_F3C",          # 07, 7
        "Function_8_F85",          # 08, 8
        "Function_9_FCE",          # 09, 9
        "Function_10_135E",        # 0A, 10
        "Function_11_1394",        # 0B, 11
        "Function_12_1651",        # 0C, 12
        "Function_13_1990",        # 0D, 13
        "Function_14_1C48",        # 0E, 14
        "Function_15_1F8E",        # 0F, 15
    )


    def Function_0_332(): pass

    label("Function_0_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_35A")
    OP_B1("C3108_1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_374")

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374")
    SetMapFlags(0x10000000)
    OP_B1("C3108_2")
    Event(0, 2)

    label("loc_374")

    Return()

    # Function_0_332 end

    def Function_1_375(): pass

    label("Function_1_375")

    Return()

    # Function_1_375 end

    def Function_2_376(): pass

    label("Function_2_376")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearMapFlags(0x10)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x40)
    SetChrPos(0x14, 570, 30000, 22920, 360)
    SetChrPos(0x15, 570, 15000, 22920, 360)
    SetChrPos(0x16, 10000, -10000, 54840, 270)
    OP_A1(0x14, 0x0)
    OP_A1(0x15, 0x1)
    OP_A1(0x16, 0x2)
    OP_6D(5630, 0, 36820, 0)
    OP_67(0, 22750, -10000, 0)
    OP_6B(11040, 0)
    OP_EA(0x64, 0x1, 0x0, 0x0)
    OP_6C(45000, 0)
    OP_6E(150, 0)
    OP_22(0x79, 0x0, 0x64)

    def lambda_434():
        OP_6D(2240, 0, 31860, 10000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_434)

    def lambda_44C():
        OP_67(0, 20330, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_44C)
    OP_6B(9000, 10000)
    OP_EA(0x64, 0x2, 0x0, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    OP_6F(0x0, 60)

    def lambda_497():
        OP_91(0xFE, 0x0, 0xFFFFC568, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_497)

    def lambda_4B2():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4B2)
    Sleep(2500)

    def lambda_4D2():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4D2)
    Sleep(1500)

    def lambda_4F2():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0xE10, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4F2)
    Sleep(900)

    def lambda_512():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0xC80, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_512)
    Sleep(800)

    def lambda_532():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0xAF0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_532)
    Sleep(700)

    def lambda_552():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_552)
    FadeToDark(1000, 0, -1)
    Sleep(600)

    def lambda_57C():
        OP_91(0xFE, 0x0, 0xFFFFA628, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_57C)
    Sleep(500)
    OP_0D()
    Sleep(500)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x14, 0x1)
    OP_44(0xE, 0x0)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x0)
    OP_44(0xF, 0x1)
    SetChrPos(0x14, 570, 100, 22920, 360)
    SetChrPos(0x15, 570, 100, 22920, 360)
    OP_6D(-15480, 15220, 18720, 0)
    OP_67(0, 9940, -10000, 0)
    OP_6B(2980, 0)
    OP_EA(0x64, 0x3, 0x0, 0x0)
    OP_6C(31000, 0)
    OP_6E(367, 0)
    SetChrBattleFlags(0xE, 0x20)
    SetChrBattleFlags(0xF, 0x20)
    SetChrBattleFlags(0x10, 0x20)
    SetChrBattleFlags(0x11, 0x20)
    SetChrBattleFlags(0x12, 0x20)
    SetChrBattleFlags(0x13, 0x20)
    OP_48()
    OP_89(0xE, -800, 2300, 23440, 270)
    OP_89(0xF, -1170, 2300, 23910, 270)
    OP_89(0x11, -740, 2300, 23530, 270)
    OP_89(0x10, -1600, 2300, 22200, 270)
    OP_89(0x13, -740, 2300, 23530, 270)
    OP_89(0x12, -740, 2300, 23530, 270)
    OP_E5(0xF, 0x0, 0x0)
    OP_E5(0x10, 0x0, 0x0)
    OP_E5(0x11, 0x0, 0x0)
    OP_E5(0x12, 0x0, 0x0)
    OP_E5(0x13, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x1)
    OP_73(0x0)
    OP_43(0xF, 0x0, 0x0, 0x7)
    Sleep(700)
    OP_43(0x11, 0x1, 0x0, 0x4)
    Sleep(600)
    OP_43(0x10, 0x1, 0x0, 0x3)
    Sleep(600)
    OP_43(0x12, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0x13, 0x1, 0x0, 0x6)
    Sleep(1000)
    OP_43(0xE, 0x0, 0x0, 0x8)
    Sleep(3000)

    def lambda_728():
        OP_6D(1040, 0, 47760, 5000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_728)
    OP_EA(0x64, 0x4, 0x0, 0x0)

    def lambda_745():
        OP_67(0, 9770, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_745)
    OP_6B(3510, 5000)
    OP_EA(0x64, 0x5, 0x0, 0x0)

    def lambda_76B():
        OP_6C(66000, 5000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_76B)

    def lambda_77B():
        OP_6E(349, 5000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_77B)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0xF, 0x2)
    Sleep(500)

    ChrTalk(    #0
        0xE,
        (
            "#691F#5PSo the Arseille's arrived, eh?\x02\x03",

            "#693FAhhh, damn. Every time I see this\x01",
            "ship, my heart skips a beat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xF,
        (
            "#2PI hear ya, boss... Who needs a guy,\x01",
            "OR a girl, when you can fall in love\x01",
            "with something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        (
            "#2PDon't think there's an engineer alive who'd\x01",
            "deserve to work on her every day, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xE,
        "#691F#5PHeh, that's my line.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -10930, 0, 35080, 72)

    NpcTalk(    #4
        0xD,
        "Man's Voice",
        (
            "#1PMaintenance Chief Gustav, thank you\x01",
            "for coming. I know you've been busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_994():
        TurnDirection(0xF, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_994)
    TurnDirection(0xE, 0xD, 400)

    def lambda_9A9():
        OP_8E(0xFE, 0xFFFFEA52, 0x0, 0x9E3E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9A9)
    Fade(1000)
    OP_6D(-4280, 0, 41130, 0)
    OP_67(0, 10220, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(192000, 0)
    OP_6E(262, 0)

    def lambda_A06():

        label("loc_A06")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_A06")

    QueueWorkItem2(0xE, 1, lambda_A06)

    def lambda_A17():

        label("loc_A17")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_A17")

    QueueWorkItem2(0xF, 1, lambda_A17)
    OP_0D()
    WaitChrThread(0xD, 0x1)
    TurnDirection(0xD, 0xE, 400)
    WaitChrThread(0xD, 0x2)

    ChrTalk(    #5
        0xE,
        (
            "#691F#5PHey, Cid. Wasn't expecting you to come meet us.\x02\x03",

            "I thought you'd moved up in the world and\x01",
            "left behind your job as garrison commander\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        (
            "#701F#4PHaha. Well, I have.\x02\x03",

            "I'm intending to leave aboard a patrol\x01",
            "ship with my men later on.\x02\x03",

            "Until then, however, I'm free, so I thought\x01",
            "I may as well come and greet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xE,
        (
            "#693F#5PHah! Well, good luck with\x01",
            "the patrol, at least.\x02\x03",

            "#692FOh, yeah, wasn't there an earthquake\x01",
            "around here a bit ago?\x02\x03",

            "You didn't let anything happen\x01",
            "to the Arseille, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "#703F#4PNo, the Arseille was in the\x01",
            "air during the earthquake.\x02\x03",

            "The earthquake caused little damage\x01",
            "in general, in fact. We were prepared\x01",
            "in advance for it.\x02\x03",

            "#701FOur facilities should still be\x01",
            "perfect for your needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xE,
        (
            "#691F#5PGood to hear!\x02\x03",

            "Anyhow, we'd love to get down\x01",
            "to work, but I'm wondering...\x02\x03",

            "Where are all the Royal Guard folks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xD,
        (
            "#701F#4PAh. Here, let me show you.\x02\x03",

            "We should be just in time\x01",
            "for a bit of a show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xE,
        "#692F#5PHuh?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_376 end

    def Function_3_E18(): pass

    label("Function_3_E18")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD896, 0x0, 0x5C1C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD8C, 0x0, 0x98E4, 0xFA0, 0x0)
    OP_8E(0xFE, 0x500, 0x0, 0xB6F8, 0xFA0, 0x0)
    OP_8C(0xFE, 325, 400)
    Return()

    # Function_3_E18 end

    def Function_4_E61(): pass

    label("Function_4_E61")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD74C, 0x0, 0x5CDA, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD1E, 0x0, 0x94B6, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0xB716, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_E61 end

    def Function_5_EAA(): pass

    label("Function_5_EAA")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD80A, 0x0, 0x5A5A, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD1E, 0x0, 0x8CE6, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFF6C8, 0x0, 0xB96E, 0xFA0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_5_EAA end

    def Function_6_EF3(): pass

    label("Function_6_EF3")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD670, 0x0, 0x5D66, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD1E, 0x0, 0x8CE6, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFF24A, 0x0, 0xB9C8, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 45)
    Return()

    # Function_6_EF3 end

    def Function_7_F3C(): pass

    label("Function_7_F3C")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD80A, 0x0, 0x5A5A, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFDD1E, 0x0, 0x90CE, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xA56E, 0xFA0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_7_F3C end

    def Function_8_F85(): pass

    label("Function_8_F85")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFD670, 0x0, 0x5D66, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFE408, 0x0, 0x9934, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFF4AC, 0x0, 0xA5C8, 0xFA0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_8_F85 end

    def Function_9_FCE(): pass

    label("Function_9_FCE")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x101, 0x80)
    OP_6D(1860, 0, 29300, 0)
    OP_67(0, 15020, -10000, 0)
    OP_6C(15000, 0)
    OP_6B(8600, 0)
    OP_6E(255, 0)
    OP_A1(0x9, 0x3)
    OP_A1(0xA, 0x1)
    OP_A1(0xB, 0x2)
    OP_A1(0xC, 0x0)
    SetChrPos(0x9, 1620, 0, 23850, 0)
    SetChrPos(0xA, 10180, -10450, 61010, 0)
    SetChrPos(0xB, 28590, -10450, 60800, 0)
    SetChrPos(0xC, -8380, -10450, 60710, 0)
    OP_A1(0x17, 0x7)
    OP_A1(0x18, 0x5)
    OP_A1(0x19, 0x6)
    OP_A1(0x1A, 0x4)
    SetChrPos(0x17, 1620, 100, 23850, 0)
    SetChrPos(0x18, 10180, -10450, 61010, 0)
    SetChrPos(0x19, 28590, -10450, 60800, 0)
    SetChrPos(0x1A, -8380, -10450, 60710, 0)
    ClearMapFlags(0x10)
    SetChrPos(0x8, 10750, 0, 30020, 270)
    ClearChrFlags(0x8, 0x80)

    def lambda_10E4():

        label("loc_10E4")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_10E4")

    QueueWorkItem2(0x8, 1, lambda_10E4)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    OP_43(0x9, 0x0, 0x0, 0xA)

    def lambda_1110():
        OP_6D(9110, 0, 26810, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1110)

    def lambda_1128():
        OP_67(0, 18670, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1128)

    def lambda_1140():
        OP_6B(6000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1140)

    def lambda_1150():
        OP_6C(56000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1150)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(11060, 0, 30510, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(2000)
    OP_DC()

    ChrTalk(    #12
        0x8,
        (
            "#1125F#6PTo think HE would actually fall into\x01",
            "their hands.\x02\x03",

            "#1122FPerhaps I need to settle this myself...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #13
        0x8,
        (
            "#1128F#6P...No.\x02\x03",

            "If I act, it will simply be the same thing\x01",
            "all over again.\x02\x03",

            "#1120FHah... He and I are in the same position,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 90, 400)
    Sleep(500)

    ChrTalk(    #14
        0x8,
        (
            "#1125F#6PGreat Aidios, who art in the sky.\x02\x03",

            "#1122FPlease...guide us who stand upon this\x01",
            "chaotic earth.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_9_FCE end

    def Function_10_135E(): pass

    label("Function_10_135E")

    OP_22(0x75, 0x0, 0x64)
    OP_43(0x9, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0xC)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0xE)
    Sleep(8500)
    Return()

    # Function_10_135E end

    def Function_11_1394(): pass

    label("Function_11_1394")

    OP_22(0x77, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 1620, 0, 23850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_6F(0x0, 360)
    OP_70(0x0, 0x1F4)
    Sleep(500)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
    OP_82(0x1, 0x2)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
    OP_B0(0x0, 0x2D)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x208)
    Sleep(500)

    def lambda_1483():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1483)

    def lambda_149E():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_149E)
    Sleep(300)

    def lambda_14BE():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14BE)

    def lambda_14D9():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_14D9)
    Sleep(300)

    def lambda_14F9():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14F9)

    def lambda_1514():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1514)
    Sleep(300)

    def lambda_1534():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1534)

    def lambda_154F():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_154F)
    Sleep(300)

    def lambda_156F():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_156F)

    def lambda_158A():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_158A)
    Sleep(300)

    def lambda_15AA():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15AA)

    def lambda_15C5():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_15C5)
    Sleep(300)

    def lambda_15E5():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15E5)

    def lambda_1600():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1600)
    Sleep(300)

    def lambda_1620():
        OP_8F(0xFE, 0x654, 0x4E20, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1620)

    def lambda_163B():
        OP_8F(0xFE, 0x654, 0x64, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_163B)
    Return()

    # Function_11_1394 end

    def Function_12_1651(): pass

    label("Function_12_1651")

    PlayEffect(0x1, 0x2, 0xFF, 10180, -10450, 61010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1F4)
    Sleep(500)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)

    def lambda_16B8():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_16B8)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)

    def lambda_16E7():
        OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_16E7)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
    OP_82(0x2, 0x2)

    def lambda_1719():
        OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1719)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)

    def lambda_1748():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1748)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)

    def lambda_1777():
        OP_91(0xFE, 0x0, 0x1C2, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1777)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
    OP_B0(0x1, 0x2D)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x208)
    Sleep(500)

    def lambda_17C2():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17C2)

    def lambda_17DD():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_17DD)
    Sleep(300)

    def lambda_17FD():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17FD)

    def lambda_1818():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1818)
    Sleep(300)

    def lambda_1838():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1838)

    def lambda_1853():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1853)
    Sleep(300)

    def lambda_1873():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1873)

    def lambda_188E():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_188E)
    Sleep(300)

    def lambda_18AE():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18AE)

    def lambda_18C9():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_18C9)
    Sleep(300)

    def lambda_18E9():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18E9)

    def lambda_1904():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1904)
    Sleep(300)

    def lambda_1924():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1924)

    def lambda_193F():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_193F)
    Sleep(300)

    def lambda_195F():
        OP_8F(0xFE, 0x27C4, 0x4E20, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_195F)

    def lambda_197A():
        OP_8F(0xFE, 0x27C4, 0x0, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_197A)
    Return()

    # Function_12_1651 end

    def Function_13_1990(): pass

    label("Function_13_1990")

    PlayEffect(0x1, 0x3, 0xFF, 28590, -10450, 60800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_6F(0x2, 360)
    OP_70(0x2, 0x1F4)
    Sleep(500)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
    OP_82(0x3, 0x2)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
    OP_B0(0x2, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x208)
    Sleep(500)

    def lambda_1A7A():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A7A)

    def lambda_1A95():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1A95)
    Sleep(300)

    def lambda_1AB5():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1AB5)

    def lambda_1AD0():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1AD0)
    Sleep(300)

    def lambda_1AF0():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1AF0)

    def lambda_1B0B():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1B0B)
    Sleep(300)

    def lambda_1B2B():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B2B)

    def lambda_1B46():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1B46)
    Sleep(300)

    def lambda_1B66():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B66)

    def lambda_1B81():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1B81)
    Sleep(300)

    def lambda_1BA1():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BA1)

    def lambda_1BBC():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1BBC)
    Sleep(300)

    def lambda_1BDC():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BDC)

    def lambda_1BF7():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1BF7)
    Sleep(300)

    def lambda_1C17():
        OP_8F(0xFE, 0x6FAE, 0x4E20, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C17)

    def lambda_1C32():
        OP_8F(0xFE, 0x6FAE, 0xFFFFD72E, 0xFFFF7CC0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1C32)
    Return()

    # Function_13_1990 end

    def Function_14_1C48(): pass

    label("Function_14_1C48")

    PlayEffect(0x1, 0x4, 0xFF, -8380, -10450, 60710, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1F4)
    Sleep(500)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)

    def lambda_1CAF():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1CAF)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)

    def lambda_1CDE():
        OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1CDE)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xBB8, 0x0)
    OP_82(0x4, 0x2)

    def lambda_1D10():
        OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1D10)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0xFA0, 0x0)

    def lambda_1D3F():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1D3F)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)

    def lambda_1D6E():
        OP_91(0xFE, 0x0, 0x1C2, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1D6E)
    OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
    OP_B0(0x3, 0x2D)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 500)
    OP_70(0x3, 0x208)
    Sleep(500)

    def lambda_1DB9():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1DB9)

    def lambda_1DD4():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1DD4)
    Sleep(300)

    def lambda_1DF4():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1DF4)

    def lambda_1E0F():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1E0F)
    Sleep(300)

    def lambda_1E2F():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E2F)

    def lambda_1E4A():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1E4A)
    Sleep(300)

    def lambda_1E6A():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E6A)

    def lambda_1E85():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1E85)
    Sleep(300)

    def lambda_1EA5():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EA5)

    def lambda_1EC0():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1EC0)
    Sleep(300)

    def lambda_1EE0():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EE0)

    def lambda_1EFB():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1EFB)
    Sleep(300)

    def lambda_1F1B():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F1B)

    def lambda_1F36():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1F36)
    Sleep(300)

    def lambda_1F56():
        OP_8F(0xFE, 0xFFFFDF58, 0x4E20, 0xFFFF079A, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F56)

    def lambda_1F71():
        OP_8F(0xFE, 0xFFFFDF58, 0x0, 0xFFFF079A, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1F71)
    OP_43(0x9, 0x1, 0x0, 0xF)
    Return()

    # Function_14_1C48 end

    def Function_15_1F8E(): pass

    label("Function_15_1F8E")

    OP_24(0x75, 0x5A)
    OP_24(0x77, 0x5A)
    Sleep(200)
    OP_24(0x75, 0x50)
    OP_24(0x77, 0x50)
    Sleep(200)
    OP_24(0x75, 0x46)
    OP_24(0x77, 0x46)
    Sleep(200)
    OP_24(0x75, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(200)
    OP_24(0x75, 0x32)
    OP_24(0x77, 0x32)
    Sleep(200)
    OP_24(0x75, 0x28)
    OP_24(0x77, 0x28)
    Sleep(200)
    OP_24(0x75, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(200)
    OP_23(0x75)
    OP_23(0x77)
    OP_23(0xCF)
    Return()

    # Function_15_1F8E end

    SaveToFile()

Try(main)
