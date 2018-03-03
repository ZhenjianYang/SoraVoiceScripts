from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2800   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2800.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Lechter',                              # 9
        'Target Camera',                        # 10
        'Academy - Back Road',                  # 11
        'Vista Forest Road',                    # 12
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
        'ED6_DT07/CH02670 ._CH',             # 00
        'ED6_DT07/CH00043 ._CH',             # 01
        'ED6_DT26/CH20777 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02670P._CP',             # 00
        'ED6_DT07/CH00043P._CP',             # 01
        'ED6_DT26/CH20777P._CP',             # 02
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
        X                   = 84080,
        Z                   = 0,
        Y                   = 28010,
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
        X                   = -3490,
        Z                   = 0,
        Y                   = 46180,
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


    DeclEvent(
        X                   = 43800,
        Y                   = 0,
        Z                   = 49800,
        Range               = 50300,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xB9F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 43800,
        Y                   = 0,
        Z                   = 44200,
        Range               = 50300,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xA4D8,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 43800,
        Y                   = 0,
        Z                   = 47600,
        Range               = 46500,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xACA8,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 41180,
        Y                   = 0,
        Z                   = 74060,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 67260,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 53150,
        Y                   = 0,
        Z                   = 59630,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 48380,
        Y                   = 0,
        Z                   = 45960,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 52870,
        Y                   = 0,
        Z                   = 32110,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 24850,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 47120,
        Y                   = 0,
        Z                   = 19010,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 22030,
        Y                   = 0,
        Z                   = 25660,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 22010,
        Y                   = 0,
        Z                   = 67170,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = 13480,
        TriggerZ            = 1000,
        TriggerY            = 46000,
        TriggerRange        = 1000,
        ActorX              = 13480,
        ActorZ              = 1000,
        ActorY              = 46000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22000,
        TriggerZ            = 500,
        TriggerY            = 68220,
        TriggerRange        = 500,
        ActorX              = 22000,
        ActorZ              = 1100,
        ActorY              = 68220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22000,
        TriggerZ            = 500,
        TriggerY            = 24820,
        TriggerRange        = 1000,
        ActorX              = 22000,
        ActorZ              = 1100,
        ActorY              = 24820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59440,
        TriggerZ            = 9000,
        TriggerY            = 17860,
        TriggerRange        = 1000,
        ActorX              = 59440,
        ActorZ              = 9500,
        ActorY              = 17860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_352",          # 00, 0
        "Function_1_3A7",          # 01, 1
        "Function_2_439",          # 02, 2
        "Function_3_44F",          # 03, 3
        "Function_4_646",          # 04, 4
        "Function_5_7BA",          # 05, 5
        "Function_6_9A1",          # 06, 6
        "Function_7_1D86",         # 07, 7
        "Function_8_1DC7",         # 08, 8
        "Function_9_1DEF",         # 09, 9
        "Function_10_1E15",        # 0A, 10
        "Function_11_1E19",        # 0B, 11
        "Function_12_1E1D",        # 0C, 12
        "Function_13_1E21",        # 0D, 13
        "Function_14_1E25",        # 0E, 14
        "Function_15_1E29",        # 0F, 15
        "Function_16_1E83",        # 10, 16
        "Function_17_1ED6",        # 11, 17
    )


    def Function_0_352(): pass

    label("Function_0_352")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_374")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_3A6")

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_38A")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_3A6")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3A6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_3A6")

    Return()

    # Function_0_352 end

    def Function_1_3A7(): pass

    label("Function_1_3A7")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x23004C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D5")
    OP_11(0x0, 0x0, 0x0, 0x9470, 0x14C08, 0x0)

    label("loc_3D5")

    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_438")
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_B2(0x1, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_438")

    Return()

    # Function_1_3A7 end

    def Function_2_439(): pass

    label("Function_2_439")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_439")

    label("loc_44E")

    Return()

    # Function_2_439 end

    def Function_3_44F(): pass

    label("Function_3_44F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1CF, 0x0, 0x64)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_6F(0x9, 60)
    OP_11(0x64, 0x64, 0x96, 0x9470, 0x14C08, 0x0)
    OP_6D(48000, 0, 45460, 0)
    OP_67(0, 9460, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(130000, 0)
    OP_6E(440, 0)
    SetChrPos(0x105, -10000, 0, 45880, 90)

    def lambda_4D1():
        OP_6D(5440, 0, 45500, 12000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4D1)

    def lambda_4E9():
        OP_67(0, 7020, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4E9)

    def lambda_501():
        OP_6C(225000, 12000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_501)

    def lambda_511():
        OP_6E(354, 12000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_511)
    FadeToBright(2000, 0)
    Sleep(9000)

    def lambda_52F():
        OP_8E(0xFE, 0x16BC, 0x0, 0xB338, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52F)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x105,
        (
            "#045F#11PHeehee. I know I didn't intend to stay out\x01",
            "that long...\x02\x03",

            "#542FIt's so easy to lose track of time when I'm at\x01",
            "the orphanage.\x02\x03",

            "I'd better hurry back to the dorm.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_602():
        OP_8E(0xFE, 0x553C, 0x0, 0xB338, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_602)
    Sleep(2000)

    def lambda_622():
        OP_6B(2700, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_622)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T2812   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_44F end

    def Function_4_646(): pass

    label("Function_4_646")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_B2(0x1, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    SetChrPos(0x105, 22000, 250, 67020, 180)
    OP_6D(22640, 0, 67720, 0)
    OP_67(0, 8700, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #1
        0x105,
        (
            "#049F#40WShe's... She's got me all wrong...\x02\x03",

            "#049FI'm not some kind of model student or 'good girl'\x01",
            "like she thinks I am...\x02\x03",

            "That's not why I'm always going to the orphanage!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F6E)
    EventEnd(0x0)
    Return()

    # Function_4_646 end

    def Function_5_7BA(): pass

    label("Function_5_7BA")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1500)
    OP_6D(47000, 0, 44700, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(135000, 0)
    OP_6E(286, 0)
    SetChrPos(0x105, 45700, 250, 46000, 90)
    OP_6F(0x0, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)
    OP_8C(0x105, 270, 400)
    Sleep(500)

    ChrTalk(    #2
        0x105,
        "#049F#5P#40W...*sigh*...\x02",
    )

    CloseMessageWindow()

    def lambda_871():
        OP_6D(44910, -300, 44260, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_871)

    def lambda_889():
        OP_8E(0xFE, 0xAB7C, 0x0, 0xB194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_889)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x11, 0x0)
    Sleep(500)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x105, 43700, -300, 45460, 270)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 1)
    Sleep(1000)

    ChrTalk(    #3
        0x105,
        (
            "#047F#5P#40W...\x02\x03",

            "...*sigh*...\x02\x03",

            "#049F(...What's wrong with me? \x01",
            "#5W  #40WMy heart just won't stop pounding...)\x02\x03",

            "(Why am I acting like this...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearParty()
    AddParty(0x3A, 0xEE, 0xFF)
    NewScene("ED6_DT21/T2812   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_7BA end

    def Function_6_9A1(): pass

    label("Function_6_9A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(44910, -300, 44260, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(135000, 0)
    OP_6E(286, 0)
    OP_6D(36010, -300, 44770, 0)
    OP_67(0, 3570, -10000, 0)
    OP_6B(980, 0)
    OP_6C(225000, 0)
    OP_6E(806, 0)
    SetChrPos(0x105, 43700, -300, 45460, 270)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 45630, 0, 50000, 180)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)

    def lambda_A7F():
        OP_6D(41260, -300, 44200, 4000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A7F)

    def lambda_A97():
        OP_67(0, 4930, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A97)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x105, 0x1)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #4
        0x105,
        "#049F#5P...*sigh*...\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_ADD():
        OP_6B(1090, 2000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ADD)
    OP_43(0x10, 0x3, 0x0, 0x8)
    WaitChrThread(0x10, 0x3)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #5
        0x10,
        (
            "#1774F#6P...'I feel like I can't understand myself at all\x01",
            "these days.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#047F#5PPlease don't stand behind me like that.\x02\x03",

            "#042FIt's creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        "#1771F#6PHahaha. Someone's in a bad mood.\x02",
    )

    CloseMessageWindow()

    def lambda_BC2():
        OP_8E(0xFE, 0xAB7C, 0x0, 0xB7FC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BC2)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 270, 0)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x10, 43700, -300, 47100, 270)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Fade(1000)
    OP_6D(44120, -300, 45540, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(1250, 0)
    OP_6C(134000, 0)
    OP_6E(572, 0)
    OP_6D(44200, -300, 45280, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(1250, 0)
    OP_6C(134000, 0)
    OP_6E(572, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(    #8
        0x10,
        "#1776F#6P(She's not looking too good.)\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #9
        0x105,
        (
            "#049F#5P...I always wished I could have a 'normal'\x01",
            "life like everyone else.\x02\x03",

            "An ordinary family, ordinary friends...\x02\x03",

            "But wishing for those things just doesn't\x01",
            "get you them, and no matter how hard\x01",
            "I try, nothing seems to work out.\x02\x03",

            "I just can't seem to make any progress...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#1775F#6P...I get'cha.\x02\x03",

            "#1779FYou were so frustrated, you ended up lashing\x01",
            "out against a friend who's kinda on the dense\x01",
            "side.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    Fade(300)
    SetChrSubChip(0x105, 2)
    Sleep(500)

    ChrTalk(    #11
        0x105,
        (
            "#042F#5PThat's not what happened at all. I'm not you.\x02\x03",

            "I might be annoyed at her, but Jill is still very\x01",
            "important to me.\x02\x03",

            "#049FBut...\x02\x03",

            "#046F#3SBut I'm not wrong, either!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    def lambda_F77():
        OP_6B(1200, 30000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F77)
    Sleep(500)

    ChrTalk(    #12
        0x105,
        (
            "#049F#5P#40WI'm not going there because I pity the children\x01",
            "or because I'm a good girl...\x02\x03",

            "The children there are wonderful. They don't\x01",
            "need pity!\x02\x03",

            "#047FI'm going there because I enjoy being there,\x01",
            "and because it's important to me!\x02\x03",

            "I don't need to be made out to be some kind\x01",
            "of saint for going somewhere I like!\x02\x03",

            "#049FBecause I'm not. That's not who I am!\x02\x03",

            "I just... I just wanted to be family!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_111F():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_111F)
    Sleep(1000)

    ChrTalk(    #13
        0x105,
        (
            "#049F#5P#40W(Why does nothing work out how I want it to...?)\x02\x03",

            "(No matter how much I want friends and family,\x01",
            "I just can't get them.)\x02\x03",

            "(Are they destined to forever be out of my reach?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#1775F#6PYou're spillin' all the beans tonight, huh?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    SetChrSubChip(0x105, 2)
    Sleep(300)

    ChrTalk(    #15
        0x105,
        "#047F#5P...What about you?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #16
        0x105,
        (
            "#046F#5P#3SIs there anything in the world\x01",
            "that you take seriously?!#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #17
        0x105,
        (
            "#046F#5P#3SJust one thing where you refuse\x01",
            "to compromise?!#2S\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #18
        0x10,
        (
            "#1773F#6PYou know, you can be preeetty scary when\x01",
            "you start shouting.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #19
        0x105,
        (
            "#049F#5P#40W...Forget it.\x01",
            "*sigh*...\x02\x03",

            "#047FShouting at you isn't going to solve anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3500)

    ChrTalk(    #20
        0x10,
        (
            "#1775F#6PSo?\x02\x03",

            "#1777FYou still don't know why you're mad, right?\x02",
        )
    )

    OP_63(0x105)
    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    Fade(100)
    SetChrSubChip(0x105, 2)
    Sleep(300)

    ChrTalk(    #21
        0x105,
        (
            "#042F#5PYou're not even listening to me, are you?\x02\x03",

            "I just told you why! It's because, well...\x01",
            "It's because I'm not going there out of\x01",
            "pity.\x02\x03",

            "#046FThat's not why I'm going there at all!\x02\x03",

            "It's because it's genuinely important to me,\x01",
            "and because...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#1776F#6P*sigh* Now we're just going around in circles.\x02\x03",

            "Sorry, but this is boring as sin.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0xA4, 0x0, 0x64)
    Fade(250)
    SetChrPos(0x10, 43900, 0, 47100, 270)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x105,
        (
            "#043F#5PWh-Where are you going? At least listen to me!\x02\x03",

            "#042FI'm trying to have a serious discussion with you!\x01",
            "You can't walk away in the middle of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1775F#6PListen. All I'm gonna say is, get yourself a clear\x01",
            "answer to my question.\x02\x03",

            "#1777FThese things are like a knotted-up rope--if you\x01",
            "don't untangle the heart of the problem, you'll \x01",
            "just get more and more wrapped up in yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        "#043F#5P#40W...What does that even mean?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x10, 120, 500)

    def lambda_17D3():
        OP_6D(45580, -300, 42590, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_17D3)
    OP_43(0x10, 0x3, 0x0, 0x7)
    SetChrSubChip(0x105, 0)

    ChrTalk(    #26 op#A
        0x10,
        "#1771F#15A#5PThat's for you to find out! ♪\x02",
    )

    Sleep(2000)
    SetChrSubChip(0x105, 1)

    ChrTalk(    #27 op#A
        0x105,
        "#043F#3S#6P#15ALechter!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    WaitChrThread(0x10, 0x3)

    def lambda_1867():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1867)
    WaitChrThread(0x11, 0x0)

    def lambda_187E():
        OP_6D(44590, -300, 44500, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_187E)
    WaitChrThread(0x11, 0x0)
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #28
        0x105,
        (
            "#043F#5P#40W...\x02\x03",

            "#047F#20WOh, who am I even kidding?\x02\x03",

            "He's probably just trying to bully me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #29
        0x105,
        (
            "#049F#5P(...No, he's not.)\x02\x03",

            "(He seems like he never takes anything seriously,\x01",
            "but in reality, he does.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, 100)
    OP_C4(0x0, 0x800)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x18\x07\x05#40WYou still don't know why you're mad, right?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x18\x07\x05#40WThese things are like a knotted-up rope--if you\x01",
            "don't untangle the heart of the problem, you'll \x01",
            "just get more and more wrapped up in yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x105,
        (
            "#043F#5P#40W...He's right...\x02\x03",

            "Why am I so angry about this...?\x02\x03",

            "#047FWhat's got me so worked up?\x02\x03",

            "...Why?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B26():
        OP_6B(1100, 3000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1B26)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x11, 0x0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "\x18\x07\x0C#40WDeep down, I knew all along what I was doing.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "\x18\x07\x0C#40WAll that time, I'd been pretending not to notice the\x01",
            "truth, but I had known since the very beginning.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x18\x07\x0C#40WAnd to avoid facing that fact, I kept desperately \x01",
            "clinging on to everything I could, telling myself I was\x01",
            "right over and over again... Trying to convince myself\x01",
            "it was true.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x18\x07\x0C#40WMaybe it was because I was afraid that if I accepted\x01",
            "it, I was going to lose everything.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #37
        "\x18\x07\x0C#40WThat was why my heart was so restless.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_20(0xFA0)
    OP_21()
    Sleep(2000)
    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_9A1 end

    def Function_7_1D86(): pass

    label("Function_7_1D86")


    def lambda_1D8C():
        OP_8F(0xFE, 0xB1A8, 0x0, 0xB158, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1D8C)
    WaitChrThread(0x10, 0x1)

    def lambda_1DAC():
        OP_8E(0xFE, 0xB194, 0x0, 0x7814, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1DAC)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_7_1D86 end

    def Function_8_1DC7(): pass

    label("Function_8_1DC7")


    def lambda_1DCD():
        OP_8E(0xFE, 0xAED8, 0x0, 0xB2E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1DCD)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x105, 400)
    Return()

    # Function_8_1DC7 end

    def Function_9_1DEF(): pass

    label("Function_9_1DEF")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #38
        0x105,
        "#049F...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_9_1DEF end

    def Function_10_1E15(): pass

    label("Function_10_1E15")

    SetPlaceName(0x5F)
    Return()

    # Function_10_1E15 end

    def Function_11_1E19(): pass

    label("Function_11_1E19")

    SetPlaceName(0x5C)
    Return()

    # Function_11_1E19 end

    def Function_12_1E1D(): pass

    label("Function_12_1E1D")

    SetPlaceName(0x5D)
    Return()

    # Function_12_1E1D end

    def Function_13_1E21(): pass

    label("Function_13_1E21")

    SetPlaceName(0x6C)
    Return()

    # Function_13_1E21 end

    def Function_14_1E25(): pass

    label("Function_14_1E25")

    SetPlaceName(0x6D)
    Return()

    # Function_14_1E25 end

    def Function_15_1E29(): pass

    label("Function_15_1E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E41")

    ChrTalk(    #39
        0x105,
        "#047F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E7F")

    label("loc_1E41")


    ChrTalk(    #40
        0x105,
        (
            "#042F...\x02\x03",

            "#047FI don't want to talk to her right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1E7F")

    TalkEnd(0xFF)
    Return()

    # Function_15_1E29 end

    def Function_16_1E83(): pass

    label("Function_16_1E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E9B")

    ChrTalk(    #41
        0x105,
        "#047F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ED2")

    label("loc_1E9B")


    ChrTalk(    #42
        0x105,
        "#049FI don't want to talk to anyone right now.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1ED2")

    TalkEnd(0xFF)
    Return()

    # Function_16_1E83 end

    def Function_17_1ED6(): pass

    label("Function_17_1ED6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2811   ._SN", 112, 0, 0)
    IdleLoop()
    TalkEnd(0xFF)
    Return()

    # Function_17_1ED6 end

    SaveToFile()

Try(main)
