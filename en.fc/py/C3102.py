from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3102.x',
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
        'Major Cid',                            # 9
        'Maintenance Chief Gustav',             # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Antoine',                              # 15
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
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH02440 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
        'ED6_DT07/CH01650 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH02440P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
        'ED6_DT07/CH01650P._CP',             # 04
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1B2",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_218",          # 02, 2
        "Function_3_22E",          # 03, 3
        "Function_4_1410",         # 04, 4
        "Function_5_1544",         # 05, 5
    )


    def Function_0_1B2(): pass

    label("Function_0_1B2")

    OP_A3(0x3FA)
    Event(0, 3)
    Return()

    # Function_0_1B2 end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE")
    OP_28(0x2A, 0x1, 0x4000)

    label("loc_1CE")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_1BA end

    def Function_2_218(): pass

    label("Function_2_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_218")

    label("loc_22D")

    Return()

    # Function_2_218 end

    def Function_3_22E(): pass

    label("Function_3_22E")

    OP_A2(0x564)
    OP_28(0x44, 0x1, 0x2)
    EventBegin(0x0)
    SetChrPos(0x8, -15700, 0, 24380, 90)
    SetChrPos(0xA, -14780, 0, 25510, 90)
    SetChrPos(0xB, -16670, 0, 25510, 90)
    SetChrPos(0xC, -14880, 0, 26880, 90)
    SetChrPos(0xD, -16680, 0, 27080, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    StopSound(0xAFC8, 0x3D090, 0x0)
    SetPlaceName(0x8C)
    OP_6D(-950, 0, 52320, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4460, 0)
    OP_6C(80000, 0)
    OP_6E(262, 0)

    def lambda_2FA():
        OP_6C(50000, 8000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2FA)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6D(-6420, 0, 24580, 6000)
    Fade(1000)
    OP_6D(-4770, 0, 24600, 0)
    OP_6B(3250, 0)
    OP_6C(54000, 0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x106, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x107, 0, 0, 0, 0)
    SetChrPos(0x106, 0, 0, 0, 0)
    SetChrBattleFlags(0x9, 0x20)
    OP_89(0x9, -2180, 2300, 22900, 270)
    OP_4A(0x8, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)

    def lambda_3CF():

        label("loc_3CF")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3CF")

    QueueWorkItem2(0x8, 1, lambda_3CF)

    def lambda_3E0():

        label("loc_3E0")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3E0")

    QueueWorkItem2(0xA, 1, lambda_3E0)

    def lambda_3F1():

        label("loc_3F1")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3F1")

    QueueWorkItem2(0xB, 1, lambda_3F1)

    def lambda_402():

        label("loc_402")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_402")

    QueueWorkItem2(0xC, 1, lambda_402)

    def lambda_413():

        label("loc_413")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_413")

    QueueWorkItem2(0xD, 1, lambda_413)
    StopSound(0xAFC8, 0x1FBD0, 0x0)
    Sleep(500)

    def lambda_436():
        OP_6D(-15630, 0, 24380, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_436)
    OP_8E(0x9, 0xFFFFC59A, 0x0, 0x59F6, 0xBB8, 0x0)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #0
        0x9,
        (
            "#691FMajor Cid? I'm here, as\x01",
            "per your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#701FHello, Chief Gustav. I'm sorry\x01",
            "to make you come all this way.\x02\x03",

            "That said, however, I'm impressed.\x01",
            "I wasn't expecting you to get here\x01",
            "so soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#691FThe Royal Military is one of my\x01",
            "best customers. You folks are\x01",
            "always a priority.\x02\x03",

            "Not to mention, the order\x01",
            "sounded pretty urgent.\x02\x03",

            "I already finished maintenance on\x01",
            "the patrol ship. Did something\x01",
            "happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#702FO-Oh, nothing significant... Just\x01",
            "your usual military matters.\x02\x03",

            "Ah, yes. I've heard about the\x01",
            "attack on the central labs.\x02\x03",

            "I've recently come into possession of\x01",
            "a clue which may help us wrap up this\x01",
            "matter within as little as a few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#690FOh...?\x01",
            "That's excellent news.\x02\x03",

            "Professor Russell is one of\x01",
            "my greatest inspirations and\x01",
            "benefactors.\x02\x03",

            "I hope he hasn't been injured...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#701FN-No...\x01",
            "You can relax on that score.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        "#692FOh? How can you be so sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#703FIt seems that the abductors\x01",
            "are demanding a ransom for\x01",
            "the professor's safe return.\x02\x03",

            "That would suggest that\x01",
            "he's unharmed, so I don't\x01",
            "think that's a concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "#691FI see...\x02\x03",

            "Well, it looks like the Royal\x01",
            "Armed Forces have this well\x01",
            "under control.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_8C(0x9, 45, 400)

    ChrTalk(    #9
        0x9,
        (
            "#691FSo are you planning to do another\x01",
            "container check today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#701FI trust you, but regulations\x01",
            "must be adhered to.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    ChrTalk(    #11
        0x8,
        (
            "#702FAll right, grunts!\x01",
            "Get to work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xD,
        "#3PRoger that, sir!\x02",
    )

    CloseMessageWindow()

    def lambda_9D3():
        OP_8E(0xFE, 0xFFFFCA04, 0x0, 0x7846, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9D3)

    ChrTalk(    #13
        0xC,
        "#3PRoger!\x02",
    )

    CloseMessageWindow()

    def lambda_9FD():

        label("loc_9FD")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_9FD")

    QueueWorkItem2(0x8, 1, lambda_9FD)

    def lambda_A0E():

        label("loc_A0E")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_A0E")

    QueueWorkItem2(0xA, 1, lambda_A0E)

    def lambda_A1F():

        label("loc_A1F")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_A1F")

    QueueWorkItem2(0xB, 1, lambda_A1F)

    def lambda_A30():

        label("loc_A30")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_A30")

    QueueWorkItem2(0x9, 1, lambda_A30)

    def lambda_A41():
        OP_6D(-9060, 0, 23330, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A41)

    def lambda_A59():
        OP_6B(4710, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A59)

    def lambda_A69():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A69)
    OP_8E(0xC, 0xFFFFC91E, 0x0, 0x64DC, 0xFA0, 0x0)

    def lambda_A8D():
        OP_8E(0xFE, 0xFFFFCB62, 0x0, 0x40D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A8D)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xD, 90, 0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)

    ChrTalk(    #14
        0xD,
        (
            "#1PNothing unusual here.\x01",
            "Next one...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x0, 0x4)
    OP_8C(0xC, 90, 0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)

    ChrTalk(    #15
        0xC,
        "#2PThis one's clear.\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x1, 0x0, 0x5)
    WaitChrThread(0xD, 0x1)
    OP_22(0xAB, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    def lambda_B47():
        OP_6D(-12400, 0, 26810, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B47)

    def lambda_B5F():
        OP_6B(3250, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5F)

    def lambda_B6F():
        OP_6C(62000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B6F)

    ChrTalk(    #16
        0xD,
        (
            "I'm picking up an anomaly\x01",
            "on the sensors!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xD,
        (
            "Looks like it's alive,\x01",
            "whatever it is!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)

    ChrTalk(    #18
        0x8,
        (
            "#702FWhat...?!\x02\x03",

            "What is this, Maintenance Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#692FH-Hey now. I have no idea.\x02\x03",

            "You sure your equipment's\x01",
            "in working order?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#703FOf course it is.\x02\x03",

            "It's a central lab-made biosensor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "#691FWell, if you say so. It's probably\x01",
            "just a mouse or some such.\x02\x03",

            "Hardly worth making such\x01",
            "a fuss over, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#703FRegulations are regulations.\x02\x03",

            "#704FSurround that container, men!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, -9980, 0, 18170, 0)
    SetChrPos(0xE, -12260, 0, 26290, 180)

    def lambda_D9C():

        label("loc_D9C")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_D9C")

    QueueWorkItem2(0xA, 1, lambda_D9C)

    def lambda_DAD():

        label("loc_DAD")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DAD")

    QueueWorkItem2(0xB, 1, lambda_DAD)

    def lambda_DBE():

        label("loc_DBE")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DBE")

    QueueWorkItem2(0xC, 1, lambda_DBE)

    def lambda_DCF():

        label("loc_DCF")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DCF")

    QueueWorkItem2(0xD, 1, lambda_DCF)

    def lambda_DE0():

        label("loc_DE0")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DE0")

    QueueWorkItem2(0x8, 1, lambda_DE0)

    def lambda_DF1():

        label("loc_DF1")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_DF1")

    QueueWorkItem2(0x9, 1, lambda_DF1)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0xB, 4)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 4)

    def lambda_E16():
        OP_8E(0xC, 0xFFFFD71A, 0x0, 0x5F64, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_E16)

    def lambda_E31():
        OP_8E(0xA, 0xFFFFD1FC, 0x0, 0x5924, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E31)

    def lambda_E4C():
        OP_8E(0xB, 0xFFFFC748, 0x0, 0x5D7A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E4C)

    def lambda_E67():
        OP_8E(0x8, 0xFFFFCD42, 0x0, 0x56EA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E67)

    def lambda_E82():
        OP_8F(0x9, 0xFFFFC270, 0x0, 0x56D6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E82)
    OP_8E(0xD, 0xFFFFC928, 0x0, 0x721A, 0xFA0, 0x0)
    OP_8E(0xD, 0xFFFFC810, 0x0, 0x6126, 0xFA0, 0x0)
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #23
        0x8,
        "#700FAll right... Open it up.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x80)
    OP_72(0x2, 0x10)
    OP_22(0xA8, 0x0, 0x64)
    OP_B0(0x2, 0x78)
    OP_70(0x2, 0x78)
    OP_6D(-12850, 0, 23990, 1000)
    OP_73(0x2)
    Sleep(1000)

    ChrTalk(    #24
        0x8,
        "#702FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_8E(0xE, 0xFFFFCF40, 0x0, 0x5ED8, 0x3E8, 0x0)
    TurnDirection(0xE, 0xD, 600)
    TurnDirection(0xE, 0xC, 600)
    TurnDirection(0xE, 0x8, 600)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    Sleep(500)
    OP_8E(0x9, 0xFFFFCA2C, 0x0, 0x5A1E, 0x7D0, 0x0)

    ChrTalk(    #25
        0x9,
        (
            "#692FOh, it's just Antoine.\x02\x03",

            "When did you sneak off, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #26
        0xE,
        "Nya-o...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "#702FOkay, so what's with the cat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#691FHis name's Antoine. He lives\x01",
            "at the central labs.\x02\x03",

            "I'd guess he sneaked onto\x01",
            "the Leibnitz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#703FHe certainly gave ME quite\x01",
            "a shock.\x02\x03",

            "#701FFalse alarm, I guess.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 400)

    ChrTalk(    #30
        0xE,
        "Nyaon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#701FWell, I suppose that one can't\x01",
            "blame a cat for being a cat.\x02\x03",

            "Hey, you. If you like it here,\x01",
            "you're welcome to stay for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#692FHey, now.\x01",
            "Don't try to tempt him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xE,
        "*Fumyaaa...*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xE,
        "...Nyaon.\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0xE, 0x20)
    OP_8E(0xE, 0xFFFFDD28, 0x0, 0x59F6, 0x1388, 0x0)
    OP_8E(0xE, 0xFFFFF77C, 0x8FC, 0x5974, 0x1388, 0x0)
    SetChrFlags(0xE, 0x80)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x9, 0xFF)

    ChrTalk(    #35
        0x8,
        (
            "#703FI think I'm getting the\x01",
            "cold shoulder.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 2)
    SetChrChipByIndex(0xC, 2)
    SetChrChipByIndex(0xD, 2)

    def lambda_1295():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1295)

    def lambda_12A3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12A3)

    def lambda_12B1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12B1)

    def lambda_12BF():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12BF)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #36
        0x9,
        (
            "#693FHa ha... Too bad.\x02\x03",

            "#691FStill, that bio-sensor is a\x01",
            "pretty impressive piece of\x01",
            "work.\x02\x03",

            "If not for it, Antoine would have\x01",
            "been packed away in storage.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #37
        0x8,
        "#701FWell, it IS of central lab make.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 400)

    ChrTalk(    #38
        0x8,
        (
            "#700FAll right, men. Check the\x01",
            "other containers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        "#3PYes, sir!\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x3FA)
    SetMapFlags(0x40000000)
    NewScene("ED6_DT01/C3106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_22E end

    def Function_4_1410(): pass

    label("Function_4_1410")

    OP_8E(0xD, 0xFFFFC914, 0x0, 0x7350, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFD076, 0x0, 0x731E, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFD08A, 0x0, 0x744A, 0xBB8, 0x0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(500)
    OP_8F(0xD, 0xFFFFD076, 0x0, 0x731E, 0x7D0, 0x0)
    OP_8E(0xD, 0xFFFFD940, 0x0, 0x736E, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFD940, 0x0, 0x744A, 0xBB8, 0x0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(500)
    OP_8F(0xD, 0xFFFFD940, 0x0, 0x736E, 0x7D0, 0x0)
    OP_8E(0xD, 0xFFFFDFF8, 0x0, 0x736E, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFDFF8, 0x0, 0x8368, 0xBB8, 0x0)
    OP_8C(0xD, 270, 400)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(500)
    OP_8E(0xD, 0xFFFFDFF8, 0x0, 0x733C, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFCF04, 0x0, 0x733C, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFCF04, 0x0, 0x71CA, 0xBB8, 0x0)
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_4_1410 end

    def Function_5_1544(): pass

    label("Function_5_1544")

    OP_8E(0xC, 0xFFFFCB76, 0x0, 0x4150, 0xBB8, 0x0)
    OP_8C(0xC, 90, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFCB76, 0x0, 0x37DC, 0xBB8, 0x0)
    OP_8C(0xC, 90, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFCB76, 0x0, 0x2ECC, 0xBB8, 0x0)
    OP_8C(0xC, 90, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFCB76, 0x0, 0x26FC, 0xFA0, 0x0)
    OP_8E(0xC, 0xFFFFD530, 0x0, 0x1D38, 0x1770, 0x0)
    OP_8E(0xC, 0xFFFFDDDC, 0x0, 0x1D38, 0x1770, 0x0)
    OP_8E(0xC, 0xFFFFE570, 0x0, 0x25C6, 0x1770, 0x0)
    OP_8E(0xC, 0xFFFFE570, 0x0, 0x2E68, 0xFA0, 0x0)
    OP_8C(0xC, 270, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFE570, 0x0, 0x3ACA, 0xFA0, 0x0)
    OP_8C(0xC, 270, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    OP_8E(0xC, 0xFFFFE570, 0x0, 0x46A0, 0xFA0, 0x0)
    OP_8C(0xC, 270, 400)
    Sleep(400)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(400)
    Return()

    # Function_5_1544 end

    SaveToFile()

Try(main)
