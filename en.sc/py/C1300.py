from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1300   ._SN',
        MapName             = 'Bose',
        Location            = 'C1300.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60089",
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
        'Major Vander',                         # 9
        'Dorothy',                              # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Empty Bobcat',                         # 18
        'Empty Bobcat (Shadow)',                # 19
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
        'ED6_DT27/CH03570 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT06/CH20063 ._CH',             # 03
        'ED6_DT06/CH20064 ._CH',             # 04
        'ED6_DT27/CH04010 ._CH',             # 05
        'ED6_DT27/CH04011 ._CH',             # 06
        'ED6_DT07/CH00310 ._CH',             # 07
        'ED6_DT07/CH00311 ._CH',             # 08
        'ED6_DT07/CH00290 ._CH',             # 09
        'ED6_DT07/CH00291 ._CH',             # 0A
        'ED6_DT07/CH00300 ._CH',             # 0B
        'ED6_DT07/CH00301 ._CH',             # 0C
        'ED6_DT27/CH04570 ._CH',             # 0D
        'ED6_DT27/CH04571 ._CH',             # 0E
        'ED6_DT27/CH04572 ._CH',             # 0F
        'ED6_DT07/CH00321 ._CH',             # 10
        'ED6_DT06/CH20043 ._CH',             # 11
        'ED6_DT07/CH00326 ._CH',             # 12
        'ED6_DT07/CH00320 ._CH',             # 13
        'ED6_DT27/CH03010 ._CH',             # 14
        'ED6_DT27/CH03011 ._CH',             # 15
        'ED6_DT27/CH03101 ._CH',             # 16
        'ED6_DT27/CH03014 ._CH',             # 17
        'ED6_DT27/CH03761 ._CH',             # 18
        'ED6_DT27/CH03771 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT27/CH03570P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT06/CH20063P._CP',             # 03
        'ED6_DT06/CH20064P._CP',             # 04
        'ED6_DT27/CH04010P._CP',             # 05
        'ED6_DT27/CH04011P._CP',             # 06
        'ED6_DT07/CH00310P._CP',             # 07
        'ED6_DT07/CH00311P._CP',             # 08
        'ED6_DT07/CH00290P._CP',             # 09
        'ED6_DT07/CH00291P._CP',             # 0A
        'ED6_DT07/CH00300P._CP',             # 0B
        'ED6_DT07/CH00301P._CP',             # 0C
        'ED6_DT27/CH04570P._CP',             # 0D
        'ED6_DT27/CH04571P._CP',             # 0E
        'ED6_DT27/CH04572P._CP',             # 0F
        'ED6_DT07/CH00321P._CP',             # 10
        'ED6_DT06/CH20043P._CP',             # 11
        'ED6_DT07/CH00326P._CP',             # 12
        'ED6_DT07/CH00320P._CP',             # 13
        'ED6_DT27/CH03010P._CP',             # 14
        'ED6_DT27/CH03011P._CP',             # 15
        'ED6_DT27/CH03101P._CP',             # 16
        'ED6_DT27/CH03014P._CP',             # 17
        'ED6_DT27/CH03761P._CP',             # 18
        'ED6_DT27/CH03771P._CP',             # 19
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -9880,
        TriggerZ            = 4000,
        TriggerY            = -550,
        TriggerRange        = 1500,
        ActorX              = -8980,
        ActorZ              = 5200,
        ActorY              = -340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FE",          # 00, 0
        "Function_1_30B",          # 01, 1
        "Function_2_350",          # 02, 2
        "Function_3_6A1",          # 03, 3
        "Function_4_6CC",          # 04, 4
        "Function_5_6F7",          # 05, 5
        "Function_6_722",          # 06, 6
        "Function_7_74D",          # 07, 7
        "Function_8_77D",          # 08, 8
        "Function_9_7C1",          # 09, 9
        "Function_10_805",         # 0A, 10
        "Function_11_849",         # 0B, 11
        "Function_12_875",         # 0C, 12
        "Function_13_8C3",         # 0D, 13
        "Function_14_911",         # 0E, 14
        "Function_15_95F",         # 0F, 15
        "Function_16_9AD",         # 10, 16
        "Function_17_9BA",         # 11, 17
        "Function_18_EB3",         # 12, 18
        "Function_19_1A11",        # 13, 19
        "Function_20_272D",        # 14, 20
        "Function_21_27FC",        # 15, 21
        "Function_22_28DB",        # 16, 22
        "Function_23_293E",        # 17, 23
        "Function_24_2977",        # 18, 24
        "Function_25_29DF",        # 19, 25
        "Function_26_2A47",        # 1A, 26
        "Function_27_2A75",        # 1B, 27
        "Function_28_2ADD",        # 1C, 28
        "Function_29_2B10",        # 1D, 29
        "Function_30_2B75",        # 1E, 30
        "Function_31_2E64",        # 1F, 31
        "Function_32_3174",        # 20, 32
        "Function_33_31B6",        # 21, 33
    )


    def Function_0_2FE(): pass

    label("Function_0_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A")
    Event(0, 2)

    label("loc_30A")

    Return()

    # Function_0_2FE end

    def Function_1_30B(): pass

    label("Function_1_30B")

    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0x11, 0x0)
    OP_A1(0x12, 0x1)
    SetChrPos(0x11, -2160, 0, -1510, 0)
    SetChrPos(0x12, -2160, 100, -1510, 0)
    OP_8C(0x11, 350, 0)
    OP_8C(0x12, 350, 0)
    Return()

    # Function_1_30B end

    def Function_2_350(): pass

    label("Function_2_350")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_43(0x129, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x12A, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0x146, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x6)
    WaitChrThread(0x129, 0x1)
    OP_8C(0x129, 0, 400)

    ChrTalk(    #0
        0x129,
        "#192F#4PAhhhhh...!\x02",
    )

    CloseMessageWindow()

    def lambda_3F8():
        OP_6D(-7610, 4000, -1690, 7000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F8)

    def lambda_410():
        OP_67(0, 5790, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_410)

    def lambda_428():
        OP_6E(255, 7000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_428)

    def lambda_438():
        OP_6B(4660, 7000)
        ExitThread()

    QueueWorkItem(0x129, 3, lambda_438)
    OP_43(0x129, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x12A, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0x146, 0x1, 0x0, 0x9)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0xA)
    WaitChrThread(0x146, 0x1)

    ChrTalk(    #1
        0x129,
        (
            "#191F#5PMy beautiful, perfect Bobcat!\x01",
            "How I've missed you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x146,
        (
            "#211FLooks like they kept it fixed up,\x01",
            "at least!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12A,
        (
            "#202F#5PJust what you'd expect from the Liberlian\x01",
            "Royal Army. They know how to treat an\x01",
            "airship, if nothing else.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 400)
    Sleep(500)

    ChrTalk(    #4
        0x102,
        (
            "#1035F#2PI know this is a happy reunion,\x01",
            "but we're very short on time.\x02\x03",

            "#1030FWe have the ignition key.\x01",
            "Let's get in the air.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12A, 180, 400)

    ChrTalk(    #5
        0x12A,
        (
            "#200F#5PRight, right.\x01",
            "Give me just a second here...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x129, 180, 400)
    OP_8C(0x146, 180, 400)

    ChrTalk(    #6
        0x129,
        (
            "#198F#5PHmph. Let us enjoy the moment\x01",
            "a LITTLE.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x146,
        "#210F#5PAll righty! All aboard!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1804)
    EventEnd(0x0)
    Return()

    # Function_2_350 end

    def Function_3_6A1(): pass

    label("Function_3_6A1")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0xBB8, 0x0)
    Return()

    # Function_3_6A1 end

    def Function_4_6CC(): pass

    label("Function_4_6CC")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE55C, 0xBB8, 0x0)
    Return()

    # Function_4_6CC end

    def Function_5_6F7(): pass

    label("Function_5_6F7")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE944, 0xBB8, 0x0)
    Return()

    # Function_5_6F7 end

    def Function_6_722(): pass

    label("Function_6_722")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFED2C, 0xBB8, 0x0)
    Return()

    # Function_6_722 end

    def Function_7_74D(): pass

    label("Function_7_74D")

    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0x2DA, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_74D end

    def Function_8_77D(): pass

    label("Function_8_77D")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD5EE, 0xFA0, 0xFFFFFE20, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_77D end

    def Function_9_7C1(): pass

    label("Function_9_7C1")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD0E4, 0xFA0, 0x2D0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_7C1 end

    def Function_10_805(): pass

    label("Function_10_805")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD210, 0xFA0, 0xFFFFF9B6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_10_805 end

    def Function_11_849(): pass

    label("Function_11_849")

    OP_43(0xA, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0xB, 0x0, 0x0, 0xD)
    Sleep(400)
    OP_43(0xC, 0x0, 0x0, 0xE)
    Sleep(300)
    OP_43(0xD, 0x0, 0x0, 0xF)
    Return()

    # Function_11_849 end

    def Function_12_875(): pass

    label("Function_12_875")

    OP_8E(0xFE, 0xFFFFBF78, 0x7D0, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCD38, 0x7D0, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD274, 0xFA0, 0xFFFFE00C, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_875 end

    def Function_13_8C3(): pass

    label("Function_13_8C3")

    OP_8E(0xFE, 0xFFFFBBAE, 0x7D0, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC950, 0x7D0, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCD56, 0xFA0, 0xFFFFE0D4, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_13_8C3 end

    def Function_14_911(): pass

    label("Function_14_911")

    OP_8E(0xFE, 0xFFFFBF78, 0x3E8, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCD38, 0x3E8, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD35A, 0xFA0, 0xFFFFD990, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_14_911 end

    def Function_15_95F(): pass

    label("Function_15_95F")

    OP_8E(0xFE, 0xFFFFBBA4, 0x3E8, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC950, 0x3E8, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCD56, 0xFA0, 0xFFFFDA76, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_15_95F end

    def Function_16_9AD(): pass

    label("Function_16_9AD")

    Call(0, 17)
    Call(0, 18)
    Call(0, 19)
    Return()

    # Function_16_9AD end

    def Function_17_9BA(): pass

    label("Function_17_9BA")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-10510, 4000, 30, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(3930, 0)
    OP_6C(145000, 0)
    OP_6E(255, 0)
    SetChrPos(0xA, -15480, 4000, -12010, 0)
    SetChrPos(0x102, -11480, 4000, -1700, 90)
    SetChrPos(0x146, -12030, 4000, 580, 90)
    SetChrPos(0x129, -10510, 4000, 720, 90)
    SetChrPos(0x12A, -10510, 4000, -1000, 90)
    OP_0D()

    NpcTalk(    #8
        0xA,
        "Voice",
        "#3POver there!\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x146, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x129, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xA, -16520, 2000, -11870, 0)
    SetChrPos(0xB, -17490, 2000, -11830, 0)
    SetChrPos(0xC, -16520, 1000, -10800, 0)
    SetChrPos(0xD, -17500, 1000, -10870, 0)
    SetChrChipByIndex(0xA, 16)
    SetChrChipByIndex(0xB, 16)
    SetChrChipByIndex(0xC, 16)
    SetChrChipByIndex(0xD, 16)

    def lambda_B50():
        OP_6D(-12670, 4000, -11680, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B50)

    def lambda_B68():
        OP_67(0, 6070, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B68)

    def lambda_B80():
        OP_6C(147000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_B80)

    def lambda_B90():
        OP_6B(2880, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B90)

    def lambda_BA0():
        OP_6E(322, 2000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BA0)
    OP_43(0xD, 0x3, 0x0, 0xB)

    def lambda_BB7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BB7)
    Sleep(100)

    def lambda_BCA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_BCA)
    Sleep(50)

    def lambda_BDD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_BDD)
    Sleep(100)

    def lambda_BF0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_BF0)
    Sleep(3000)
    OP_6D(-11430, 4000, -4670, 1500)

    ChrTalk(    #9
        0x129,
        "#192F#5PHells!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x12A,
        "#201F#5PDamn it! They found us!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x0)

    ChrTalk(    #11
        0xB,
        "#4PThe sky bandits!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xA,
        "#6PHow'd they--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xD,
        (
            "They must be the ones who knocked\x01",
            "out the captain! GET THEM!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 0)
    OP_0D()

    ChrTalk(    #14
        0x102,
        "#1032F#5PNo choice, then.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x146, 7)
    SetChrSubChip(0x146, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x12A, 11)
    SetChrSubChip(0x12A, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x129, 9)
    SetChrSubChip(0x129, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0x146,
        "#214F#5PNaptime, suckers!\x02",
    )

    CloseMessageWindow()

    def lambda_D59():
        OP_6D(-11680, 4000, -4390, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D59)

    def lambda_D71():
        OP_6B(2500, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D71)

    def lambda_D81():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D81)
    SetChrChipByIndex(0xA, 16)

    def lambda_DA1():
        OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_DA1)
    Sleep(50)

    def lambda_DC1():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_DC1)
    SetChrChipByIndex(0xB, 16)

    def lambda_DE1():
        OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DE1)
    Sleep(50)
    SetChrFlags(0x146, 0x1000)
    SetChrChipByIndex(0x146, 8)

    def lambda_E0B():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_E0B)
    SetChrChipByIndex(0xC, 16)

    def lambda_E2B():
        OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E2B)
    Sleep(50)

    def lambda_E4B():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_E4B)
    SetChrChipByIndex(0xD, 16)

    def lambda_E6B():
        OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E6B)
    Sleep(200)
    OP_44(0x102, 0xFF)
    OP_44(0x146, 0xFF)
    OP_44(0x129, 0xFF)
    OP_44(0x12A, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Battle(0xA6, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_17_9BA end

    def Function_18_EB3(): pass

    label("Function_18_EB3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x146, 65535)
    SetChrChipByIndex(0x129, 65535)
    SetChrChipByIndex(0x12A, 65535)
    OP_8C(0x102, 180, 0)
    OP_8C(0x146, 180, 0)
    OP_8C(0x129, 180, 0)
    OP_8C(0x12A, 180, 0)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Call(0, 33)
    SetChrPos(0x102, -12270, 4000, -1460, 0)
    SetChrPos(0x146, -12610, 4000, 500, 0)
    SetChrPos(0x129, -11560, 4000, 690, 0)
    SetChrPos(0x12A, -11070, 4000, -1280, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x146, 65535)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x12A, 65535)
    SetChrSubChip(0x12A, 0)
    SetChrChipByIndex(0x129, 65535)
    SetChrSubChip(0x129, 0)
    OP_6D(-11090, 4000, -1010, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(147000, 0)
    OP_6E(322, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x146,
        "#210F#6PAaaand down for the count!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#1035F#4PThat won't be the last of them.\x02\x03",

            "#1030FI'll hold them here.\x01",
            "Get the Bobcat ready for launch.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_105A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_105A)
    Sleep(50)

    def lambda_106D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_106D)
    Sleep(50)
    OP_8C(0x146, 180, 400)

    ChrTalk(    #18
        0x129,
        "#196F#6PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12A,
        "#202F#6PWe'll be just a minute!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_48()
    OP_8C(0x129, 90, 500)

    def lambda_10CD():
        OP_6D(-7230, 4000, -1520, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10CD)
    OP_43(0x129, 0x1, 0x0, 0x14)
    OP_8C(0x12A, 90, 500)
    OP_8C(0x146, 90, 500)
    OP_8C(0x102, 90, 500)
    Sleep(500)
    OP_43(0x12A, 0x1, 0x0, 0x15)
    Sleep(1000)
    OP_6D(-10160, 4000, -1430, 1500)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #20
        0x102,
        "#1034F#4PJosette? Why aren't you boarding?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x146, 180, 400)

    ChrTalk(    #21
        0x146,
        (
            "#210F#5PMy brothers can get the Bobcat in the\x01",
            "air just fine.\x02\x03",

            "I'm gonna stay here and back you up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#1032F#4PBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x146,
        (
            "#211F#5PHaha! No buts!\x02\x03",

            "You know, you try acting all cool,\x01",
            "but you're kinda near-sighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1034F#4PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x146,
        (
            "#210F#5PDespite the whole 'blargh emotional distance,\x01",
            "you are my chess pieces' thing, you've\x01",
            "been really helpin' us out. A lot.\x02\x03",

            "Do you really think I--we--are just gonna\x01",
            "dump you here and run at this point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1031F#4PWell...I do think I'm a fairly good judge\x01",
            "of character.\x02\x03",

            "Especially with someone who wears their\x01",
            "heart on their sleeve, like a certain\x01",
            "bandit I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x146,
        (
            "#216F#5PHey, who wears their heart on their sleeve?\x01",
            "I could say the same about you, buster!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -13110, 4000, -15810, 0)

    NpcTalk(    #28
        0x8,
        "Man's Voice",
        "#3PHm. I thought it was a bit noisy in here.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x146, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_14CB():
        OP_8C(0xFE, 192, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14CB)
    Sleep(50)

    def lambda_14DE():
        OP_8C(0xFE, 192, 500)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_14DE)
    OP_20(0x7D0)

    def lambda_14F1():
        OP_8E(0xFE, 0xFFFFCF22, 0xFA0, 0xFFFFE0C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_14F1)
    OP_6D(-11750, 4000, -5000, 2000)

    ChrTalk(    #29
        0x146,
        "#213F#5PWha?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #30
        0x8,
        (
            "#277F#4PThe Capua sky bandits...\x01",
            "What perfect timing you have.\x02\x03",

            "And HE'S with you, no less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1035F#1P...You remembered me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x146,
        (
            "#216F#5PWhat the--?!\x01",
            "Oh, CRAP, what's an Erebonian\x01",
            "army guy doing here?!\x02\x03",

            "And... Wait a second, you know him?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#1030F#1PWe've met...briefly.\x02\x03",

            "You're here to collect the ship prior to\x01",
            "the pact signing, I suspect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#270F#4PExactly.\x02\x03",

            "#272FTo be perfectly frank, I could not care\x01",
            "less if you take that ship and fly it\x01",
            "to the moon.\x02\x03",

            "Now that I am here, however...\x01",
            "I cannot simply let you pass.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-12170, 4000, -6200, 0)
    OP_67(0, 3810, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(175000, 0)
    OP_6E(322, 0)
    OP_0D()
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 1)
    OP_22(0x1F9, 0x0, 0x64)
    OP_99(0x8, 0x1, 0x6, 0x7D0)
    OP_1D(0x33)
    Sleep(500)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #35
        0x8,
        (
            "#270F#6PAllow me to introduce myself properly.\x02\x03",

            "I am Major Mueller Vander of the\x01",
            "Imperial Army's 7th Armored Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x146,
        "#212F#2POh, man...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x146, 7)
    SetChrSubChip(0x146, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x102,
        "#1032F#5PBe careful. This won't be a normal fight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#272F#6PI'd say that's due more to you, Joshua.\x01",
            "Regardless...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #39
        0x8,
        "#271F#6P#3SOn your guard!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_192A():
        OP_6D(-12230, 4000, -4280, 300)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_192A)

    def lambda_1942():
        OP_6B(2480, 300)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1942)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x1000)

    def lambda_195C():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_195C)
    Sleep(10)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 6)

    def lambda_1986():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1986)
    Sleep(50)
    SetChrFlags(0x146, 0x1000)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 8)

    def lambda_19B5():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_19B5)
    Sleep(100)
    RemoveParty(0x28, 0xFF)
    RemoveParty(0x29, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x146, 0xFF)
    OP_44(0x8, 0xFF)
    Battle(0xA8, 0x0, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_18_EB3 end

    def Function_19_1A11(): pass

    label("Function_19_1A11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    Call(0, 33)
    AddParty(0x28, 0xFF, 0xFF)
    AddParty(0x29, 0xFF, 0xFF)
    OP_44(0x102, 0x1)
    OP_44(0x146, 0x1)
    OP_44(0x8, 0x1)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x146, 0x1000)
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x129, 0x80)
    SetChrFlags(0x12A, 0x80)
    Call(0, 33)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x146, 7)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 6)
    SetChrPos(0x102, -12270, 4000, -1460, 180)
    SetChrPos(0x146, -12610, 4000, 500, 180)
    SetChrPos(0x8, -12510, 4000, -8000, 0)
    OP_6D(-12170, 4000, -6200, 0)
    OP_67(0, 3810, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(175000, 0)
    OP_6E(322, 0)
    OP_A3(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1AFD"),
        (1, "loc_1B03"),
        (SWITCH_DEFAULT, "loc_1B09"),
    )


    label("loc_1AFD")

    OP_A2(0x0)
    Jump("loc_1B09")

    label("loc_1B03")

    OP_A3(0x0)
    Jump("loc_1B09")

    label("loc_1B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B80")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as won vs. Mueller\x01",       # 0
            "Set as lost vs. Mueller\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B74"),
        (1, "loc_1B7A"),
        (SWITCH_DEFAULT, "loc_1B80"),
    )


    label("loc_1B74")

    OP_A2(0x0)
    Jump("loc_1B80")

    label("loc_1B7A")

    OP_A3(0x0)
    Jump("loc_1B80")

    label("loc_1B80")

    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BE4")

    ChrTalk(    #40
        0x146,
        (
            "#214F#2P*pant* *pant*\x02\x03",

            "What the hell?!\x01",
            "Go DOWN already, you sack of--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1B")

    label("loc_1BE4")


    ChrTalk(    #41
        0x146,
        (
            "#215F#2PAgh...!\x02\x03",

            "No way... How the hell is he...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1B")


    ChrTalk(    #42
        0x102,
        (
            "#1035F#5PMaster level swordplay...\x01",
            "and your last name is Vander.\x02\x03",

            "#1031FI think I can guess who 'Olivier'\x01",
            "must be, in that case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#272F#6PIf we're discussing identities,\x01",
            "yours was certainly a surprise.\x02\x03",

            "#270FJoshua Astray...lost child of Hamel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#1034F#5PWha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x146,
        "#213F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#276F#6PAs we thought.\x02\x03",

            "I guess even that idiot's guesses\x01",
            "can be right, sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1038F#5P...\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp056_00.eff")
    PlayEffect(0x0, 0x1, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x117, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #48
        0x146,
        "#216F#2PUm... Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1038F#5PMay I ask then, 'Major' Vander.\x02\x03",

            "How do you know about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#272F#6PSo you do have a killer's gleam\x01",
            "in your eye, after all.\x02\x03",

            "#270FI'll give you all I have, then, 'Enforcer.'\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp057_00.eff")
    PlayEffect(0x2, 0x2, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x117, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x146, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #51
        0x146,
        "#216F#2PW-Wait! No...!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    OP_43(0x12A, 0x0, 0x0, 0x1F)
    Sleep(1000)
    OP_62(0x146, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x146, 65535)
    OP_8C(0x146, 90, 400)

    def lambda_1FE7():
        OP_6D(-7530, 6580, -2230, 8000)
        ExitThread()

    QueueWorkItem(0x146, 0, lambda_1FE7)

    def lambda_1FFF():
        OP_67(0, 6340, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_1FFF)

    def lambda_2017():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x146, 2, lambda_2017)

    def lambda_2027():
        OP_6E(603, 8000)
        ExitThread()

    QueueWorkItem(0x146, 3, lambda_2027)

    def lambda_2037():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_2037)
    WaitChrThread(0x12A, 0x0)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x0, 160)
    OP_70(0x0, 0x50)
    OP_73(0x0)
    Sleep(200)
    ClearChrFlags(0x12A, 0x80)
    SetChrFlags(0x12A, 0x4)
    SetChrPos(0x12A, -3020, 9000, -1200, 270)
    OP_8F(0x12A, 0xFFFFF434, 0x251C, 0xFFFFFB50, 0x7D0, 0x0)
    OP_82(0x4, 0x2)
    WaitChrThread(0x146, 0x0)
    Sleep(500)

    ChrTalk(    #52
        0x12A,
        (
            "#201F#6PAaaaand it lives!\x02\x03",

            "Oy, Josette! Joshua! Hop on!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x1, 0x2)
    Sleep(300)
    OP_82(0x2, 0x2)
    Sleep(300)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    Sleep(200)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x102, 90, 400)
    OP_8C(0x8, 45, 400)

    ChrTalk(    #53
        0x146,
        "#210F#5PRight!\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    def lambda_2136():
        OP_8F(0x12A, 0xFFFFF434, 0x2328, 0xFFFFFB50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_2136)
    Fade(500)
    OP_6D(-10520, 4000, -1950, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(145000, 0)
    OP_6E(603, 0)
    PlayEffect(0x1, 0x4, 0x12, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_21C8():
        OP_8F(0x11, 0xFFFFF63C, 0x1F4, 0x9C4, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_21C8)

    def lambda_21E3():
        OP_8F(0x12, 0xFFFFF63C, 0x1F4, 0x9C4, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 2, lambda_21E3)
    WaitChrThread(0x12A, 0x1)
    OP_6F(0x0, 80)
    OP_70(0x0, 0xA0)
    OP_23(0x6A)
    OP_22(0xE6, 0x0, 0x64)
    SetChrFlags(0x12A, 0x80)
    OP_48()
    SetChrFlags(0x146, 0x4)
    SetChrBattleFlags(0x146, 0x20)
    OP_8F(0x146, 0xFFFFD562, 0xFA0, 0xFFFFFF1A, 0x1388, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x146, 22)
    SetChrSubChip(0x146, 5)
    OP_96(0x146, 0xFFFFE08E, 0x14D2, 0x28, 0x7D0, 0x1388)
    SetChrChipByIndex(0x146, 65535)
    SetChrSubChip(0x146, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x146, 0x4)
    OP_8E(0x146, 0xFFFFEDA4, 0x17A2, 0xFFFFFD80, 0xFA0, 0x0)
    OP_8C(0x146, 270, 400)

    ChrTalk(    #54
        0x146,
        (
            "#214F#3PJoshua! Come on!\x01",
            "What're you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#1033F#6P...Hmph.\x02",
    )

    CloseMessageWindow()

    def lambda_22DA():
        OP_6D(-10520, 4000, -9000, 4000)
        ExitThread()

    QueueWorkItem(0x12A, 0, lambda_22DA)
    OP_43(0x11, 0x1, 0x0, 0x1E)
    OP_43(0xE, 0x1, 0x0, 0x16)
    OP_43(0xF, 0x1, 0x0, 0x18)
    OP_43(0x10, 0x1, 0x0, 0x19)
    OP_43(0x9, 0x1, 0x0, 0x1B)
    OP_8C(0x146, 180, 400)

    def lambda_231C():

        label("loc_231C")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_231C")

    QueueWorkItem2(0x8, 1, lambda_231C)
    OP_8E(0x102, 0xFFFFD6F2, 0xFA0, 0xFFFFF830, 0x1388, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrBattleFlags(0x102, 0x20)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x102, 21)
    SetChrSubChip(0x102, 5)

    def lambda_235A():
        OP_96(0x102, 0xFFFFE2B4, 0x1770, 0xFFFFF830, 0x8FC, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_235A)
    WaitChrThread(0x102, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x4)
    OP_8C(0x102, 180, 600)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 23)
    SetChrSubChip(0x102, 3)
    Sleep(500)
    OP_44(0x12A, 0x0)
    Fade(250)
    OP_6D(-5290, 6330, -19870, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(145000, 0)
    OP_6E(466, 0)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)

    def lambda_2401():

        label("loc_2401")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2401")

    QueueWorkItem2(0xE, 1, lambda_2401)

    def lambda_2412():

        label("loc_2412")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2412")

    QueueWorkItem2(0xF, 1, lambda_2412)

    def lambda_2423():

        label("loc_2423")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2423")

    QueueWorkItem2(0x10, 1, lambda_2423)

    ChrTalk(    #56 op#A op#5
        0xE,
        "#4A#3PWhaaaa...?!\x05\x02",
    )

    Sleep(400)

    ChrTalk(    #57 op#A op#5
        0xF,
        "#15A#2PStop them!\x05\x02",
    )

    Sleep(1500)
    WaitChrThread(0x9, 0x1)

    def lambda_2470():

        label("loc_2470")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2470")

    QueueWorkItem2(0x9, 1, lambda_2470)
    OP_43(0xE, 0x2, 0x0, 0x1C)
    Sleep(100)
    OP_43(0xF, 0x2, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x10, 0x2, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x9, 0x2, 0x0, 0x1D)

    ChrTalk(    #58 op#A op#5
        0x9,
        "#25A#153F#2PWhoooa! What a photo op!\x05\x02",
    )

    Sleep(1000)
    WaitChrThread(0x11, 0x1)
    OP_20(0xBB8)
    FadeToDark(2500, 0, -1)
    OP_0D()
    OP_6D(-11550, 6400, -22050, 0)
    OP_67(0, 3700, -10000, 0)
    OP_6B(3970, 0)
    OP_6C(157000, 0)
    OP_6E(262, 0)
    OP_44(0xE, 0x2)
    OP_44(0xF, 0x2)
    OP_44(0x10, 0x2)
    OP_44(0x9, 0x2)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x146, 0x80)
    SetChrFlags(0x129, 0x80)
    SetChrFlags(0x12A, 0x80)
    Sleep(2000)
    OP_1D(0x54)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #59
        0xE,
        "Oh, hell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xF,
        "#5PWhat happened to the commander?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        "Get Haken Gate on the line!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 1)
    SetChrChipByIndex(0xF, 1)
    SetChrChipByIndex(0x10, 1)
    SetChrChipByIndex(0x9, 3)

    def lambda_25D9():
        OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0xFFFF6DAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_25D9)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(100)
    OP_43(0x10, 0x1, 0x0, 0x1A)
    Sleep(2000)

    def lambda_2611():
        OP_6D(-14870, 6400, -19960, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2611)

    def lambda_2629():
        OP_67(0, 6180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2629)

    def lambda_2641():
        OP_6B(3550, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2641)
    OP_6E(215, 3000)
    SetMapFlags(0x2000000)

    ChrTalk(    #62
        0x9,
        (
            "#154FHuuuuuh?\x02\x03",

            "I thiiiink I've seen that boy somewhere\x01",
            "before...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #63
        0x9,
        (
            "#153FAaaaaaah! What does this mean?!\x02\x03",

            "#152FI gotta tell Nial!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1305   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1A11 end

    def Function_20_272D(): pass

    label("Function_20_272D")

    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_8C(0xFE, 90, 0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 24)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0x370, 0xFA0, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)
    OP_96(0xFE, 0xFFFFE0C0, 0x14D2, 0xC8, 0x7D0, 0xFA0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFEBB0, 0x1770, 0x46A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEEBC, 0x15AE, 0xFFFFF98E, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFF51A, 0x15AE, 0xFFFFF93E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_272D end

    def Function_21_27FC(): pass

    label("Function_21_27FC")

    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xFFFFD6D4, 0xFA0, 0xFFFFFCE0, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)
    OP_96(0xFE, 0xFFFFE0C0, 0x14D2, 0xC8, 0x7D0, 0xFA0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFEB6A, 0x1770, 0x37A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEC1E, 0x178E, 0x17C, 0xBB8, 0x0)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEE94, 0x15AE, 0xFFFFF7FE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF51A, 0x15AE, 0xFFFFF93E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Sleep(200)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_23(0x6A)
    OP_22(0xE6, 0x0, 0x64)
    Return()

    # Function_21_27FC end

    def Function_22_28DB(): pass

    label("Function_22_28DB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17060, 0, -8830, 0)

    def lambda_2902():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2902)
    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFD2A6, 0xFA0, 0xFFFFB136, 0x1770, 0x0)
    TurnDirection(0xFE, 0x11, 400)
    Return()

    # Function_22_28DB end

    def Function_23_293E(): pass

    label("Function_23_293E")

    OP_8E(0xFE, 0xFFFFD120, 0xFA0, 0xFFFFDCD8, 0xFA0, 0x0)

    label("loc_2952")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2976")
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 325, 400)
    Sleep(1000)
    Jump("loc_2952")

    label("loc_2976")

    Return()

    # Function_23_293E end

    def Function_24_2977(): pass

    label("Function_24_2977")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17060, 0, -8830, 0)

    def lambda_29A3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29A3)
    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFD1C0, 0xFA0, 0xFFFFA808, 0x1770, 0x0)
    TurnDirection(0xFE, 0x11, 400)
    Return()

    # Function_24_2977 end

    def Function_25_29DF(): pass

    label("Function_25_29DF")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17060, 0, -8830, 0)

    def lambda_2A0B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A0B)
    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFCC48, 0xFA0, 0xFFFFB096, 0x1770, 0x0)
    TurnDirection(0xFE, 0x11, 400)
    Return()

    # Function_25_29DF end

    def Function_26_2A47(): pass

    label("Function_26_2A47")

    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFBD5C, 0xFA0, 0xFFFFDD82, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_2A47 end

    def Function_27_2A75(): pass

    label("Function_27_2A75")

    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17060, 0, -8830, 0)

    def lambda_2AA1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AA1)
    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFCA22, 0xFA0, 0xFFFFA90C, 0x1770, 0x0)
    TurnDirection(0xFE, 0x11, 400)
    Return()

    # Function_27_2A75 end

    def Function_28_2ADD(): pass

    label("Function_28_2ADD")

    SetChrChipByIndex(0xFE, 18)

    label("loc_2AE2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B0F")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(500)
    Jump("loc_2AE2")

    label("loc_2B0F")

    Return()

    # Function_28_2ADD end

    def Function_29_2B10(): pass

    label("Function_29_2B10")

    LoadEffect(0x0, "map\\\\mp032_00.eff")
    SetChrChipByIndex(0xFE, 4)

    label("loc_2B29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B74")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("loc_2B29")

    label("loc_2B74")

    Return()

    # Function_29_2B10 end

    def Function_30_2B75(): pass

    label("Function_30_2B75")


    def lambda_2B7B():
        OP_8F(0xFE, 0xFFFFF63C, 0x1F4, 0xFFFFF63C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2B7B)

    def lambda_2B96():
        OP_8F(0xFE, 0xFFFFF63C, 0x1F4, 0xFFFFF63C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2B96)
    Sleep(500)

    def lambda_2BB6():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2BB6)

    def lambda_2BD1():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2BD1)
    Sleep(500)
    OP_6F(0x0, 200)
    OP_70(0x0, 0xF0)

    def lambda_2BFF():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2BFF)

    def lambda_2C1A():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2C1A)
    Sleep(500)

    def lambda_2C3A():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C3A)

    def lambda_2C55():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2C55)
    Sleep(500)

    def lambda_2C75():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C75)

    def lambda_2C90():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2C90)
    Sleep(500)

    def lambda_2CB0():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2CB0)

    def lambda_2CCB():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2CCB)
    Sleep(500)

    def lambda_2CEB():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2CEB)

    def lambda_2D06():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2D06)
    Sleep(500)

    def lambda_2D26():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2D26)

    def lambda_2D41():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2D41)
    Sleep(500)

    def lambda_2D61():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2D61)

    def lambda_2D7C():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2D7C)
    Sleep(500)

    def lambda_2D9C():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2D9C)

    def lambda_2DB7():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2DB7)
    Sleep(500)
    WaitChrThread(0x11, 0x2)
    WaitChrThread(0x12, 0x2)
    OP_24(0x77, 0x5A)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x79, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x79, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x79, 0x1E)
    Sleep(100)
    OP_24(0x77, 0x14)
    OP_24(0x79, 0x14)
    Sleep(100)
    OP_24(0x77, 0xA)
    OP_24(0x79, 0xA)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x79)
    OP_82(0x4, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    Return()

    # Function_30_2B75 end

    def Function_31_2E64(): pass

    label("Function_31_2E64")

    PlayEffect(0x1, 0x4, 0x12, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_24(0x79, 0x46)
    Sleep(500)
    OP_24(0x79, 0x50)
    Sleep(500)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x64)
    Sleep(500)
    SetChrFlags(0x11, 0x4)
    OP_22(0x77, 0x0, 0x64)
    Sleep(500)
    OP_6F(0x0, 160)
    OP_70(0x0, 0xC8)

    def lambda_2EE5():
        OP_8F(0x11, 0xFFFFFBDC, 0x3E8, 0x0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_2EE5)

    def lambda_2F00():
        OP_8F(0x12, 0xFFFFFBDC, 0x0, 0x0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 2, lambda_2F00)
    WaitChrThread(0x129, 0x1)
    WaitChrThread(0x129, 0x2)
    Sleep(300)

    def lambda_2F2A():
        OP_8C(0xFE, 315, 5)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2F2A)

    def lambda_2F38():
        OP_8C(0xFE, 315, 5)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2F38)
    Sleep(400)

    def lambda_2F4B():
        OP_8C(0xFE, 270, 8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2F4B)

    def lambda_2F59():
        OP_8C(0xFE, 270, 8)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2F59)
    Sleep(400)

    def lambda_2F6C():
        OP_8C(0xFE, 270, 10)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2F6C)

    def lambda_2F7A():
        OP_8C(0xFE, 270, 10)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2F7A)
    Sleep(400)

    def lambda_2F8D():
        OP_8C(0xFE, 225, 13)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2F8D)

    def lambda_2F9B():
        OP_8C(0xFE, 225, 13)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2F9B)
    Sleep(400)

    def lambda_2FAE():
        OP_8C(0xFE, 225, 15)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2FAE)

    def lambda_2FBC():
        OP_8C(0xFE, 225, 15)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2FBC)
    Sleep(400)

    def lambda_2FCF():
        OP_8C(0xFE, 180, 18)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2FCF)

    def lambda_2FDD():
        OP_8C(0xFE, 180, 18)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2FDD)
    Sleep(400)

    def lambda_2FF0():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2FF0)

    def lambda_2FFE():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2FFE)
    Sleep(400)

    def lambda_3011():
        OP_8C(0xFE, 180, 23)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3011)

    def lambda_301F():
        OP_8C(0xFE, 180, 23)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_301F)
    Sleep(400)

    def lambda_3032():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3032)

    def lambda_3040():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_3040)
    Sleep(400)

    def lambda_3053():
        OP_8C(0xFE, 180, 28)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3053)

    def lambda_3061():
        OP_8C(0xFE, 180, 28)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_3061)
    Sleep(3000)

    def lambda_3074():
        OP_8F(0x11, 0xFFFFF63C, 0x0, 0x9C4, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_3074)

    def lambda_308F():
        OP_8F(0x12, 0xFFFFF63C, 0x0, 0x9C4, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 2, lambda_308F)

    def lambda_30AA():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_30AA)

    def lambda_30B8():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_30B8)
    Sleep(400)

    def lambda_30CB():
        OP_8C(0xFE, 180, 23)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_30CB)

    def lambda_30D9():
        OP_8C(0xFE, 180, 23)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_30D9)
    Sleep(400)

    def lambda_30EC():
        OP_8C(0xFE, 180, 18)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_30EC)

    def lambda_30FA():
        OP_8C(0xFE, 180, 18)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_30FA)
    Sleep(400)

    def lambda_310D():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_310D)

    def lambda_311B():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_311B)
    Sleep(400)

    def lambda_312E():
        OP_8C(0xFE, 180, 8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_312E)

    def lambda_313C():
        OP_8C(0xFE, 180, 8)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_313C)
    Sleep(400)
    WaitChrThread(0x11, 0x3)
    WaitChrThread(0x129, 0x1)
    WaitChrThread(0x129, 0x2)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    Return()

    # Function_31_2E64 end

    def Function_32_3174(): pass

    label("Function_32_3174")

    SetChrChipByIndex(0x8, 0)
    OP_8E(0xFE, 0xFFFFCAA4, 0xFA0, 0xFFFFC180, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFBE4C, 0xFA0, 0xFFFFBDE8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFBDB6, 0x0, 0xFFFFDC38, 0xBB8, 0x0)
    Return()

    # Function_32_3174 end

    def Function_33_31B6(): pass

    label("Function_33_31B6")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 17)
    SetChrChipByIndex(0xD, 17)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    SetChrPos(0xA, -11960, 4000, 4040, 315)
    SetChrPos(0xB, -12210, 4000, 6160, 90)
    SetChrPos(0xC, -13650, 4000, 6030, 180)
    SetChrPos(0xD, -13510, 4000, 3710, 45)
    Return()

    # Function_33_31B6 end

    SaveToFile()

Try(main)
