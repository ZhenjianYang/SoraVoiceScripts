from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0302   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0302.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        'Josette',                              # 9
        'Lonnie',                               # 10
        'Dino',                                 # 11
        'Lyall',                                # 12
        'Kyle',                                 # 13
        'Bobcat',                               # 14
        'Bobcat (Shadow)',                      # 15
        'Target Camera',                        # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 19,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00310 ._CH',             # 00
        'ED6_DT07/CH00311 ._CH',             # 01
        'ED6_DT07/CH00314 ._CH',             # 02
        'ED6_DT07/CH00360 ._CH',             # 03
        'ED6_DT07/CH00361 ._CH',             # 04
        'ED6_DT07/CH00364 ._CH',             # 05
        'ED6_DT07/CH00100 ._CH',             # 06
        'ED6_DT07/CH00101 ._CH',             # 07
        'ED6_DT07/CH00110 ._CH',             # 08
        'ED6_DT07/CH00111 ._CH',             # 09
        'ED6_DT07/CH00120 ._CH',             # 0A
        'ED6_DT07/CH00121 ._CH',             # 0B
        'ED6_DT07/CH00122 ._CH',             # 0C
        'ED6_DT07/CH02130 ._CH',             # 0D
        'ED6_DT07/CH02330 ._CH',             # 0E
        'ED6_DT07/CH02120 ._CH',             # 0F
        'ED6_DT07/CH01380 ._CH',             # 10
        'ED6_DT09/CH10010 ._CH',             # 11
        'ED6_DT09/CH10011 ._CH',             # 12
        'ED6_DT09/CH10280 ._CH',             # 13
        'ED6_DT09/CH10281 ._CH',             # 14
        'ED6_DT09/CH10230 ._CH',             # 15
        'ED6_DT09/CH10231 ._CH',             # 16
        'ED6_DT09/CH10240 ._CH',             # 17
        'ED6_DT09/CH10241 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH00310P._CP',             # 00
        'ED6_DT07/CH00311P._CP',             # 01
        'ED6_DT07/CH00314P._CP',             # 02
        'ED6_DT07/CH00360P._CP',             # 03
        'ED6_DT07/CH00361P._CP',             # 04
        'ED6_DT07/CH00364P._CP',             # 05
        'ED6_DT07/CH00100P._CP',             # 06
        'ED6_DT07/CH00101P._CP',             # 07
        'ED6_DT07/CH00110P._CP',             # 08
        'ED6_DT07/CH00111P._CP',             # 09
        'ED6_DT07/CH00120P._CP',             # 0A
        'ED6_DT07/CH00121P._CP',             # 0B
        'ED6_DT07/CH00122P._CP',             # 0C
        'ED6_DT07/CH02130P._CP',             # 0D
        'ED6_DT07/CH02330P._CP',             # 0E
        'ED6_DT07/CH02120P._CP',             # 0F
        'ED6_DT07/CH01380P._CP',             # 10
        'ED6_DT09/CH10010P._CP',             # 11
        'ED6_DT09/CH10011P._CP',             # 12
        'ED6_DT09/CH10280P._CP',             # 13
        'ED6_DT09/CH10281P._CP',             # 14
        'ED6_DT09/CH10230P._CP',             # 15
        'ED6_DT09/CH10231P._CP',             # 16
        'ED6_DT09/CH10240P._CP',             # 17
        'ED6_DT09/CH10241P._CP',             # 18
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 52120,
        Z                   = 240,
        Y                   = -16250,
        Unknown_0C          = 93,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x4D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 61090,
        Z                   = -350,
        Y                   = 5020,
        Unknown_0C          = 237,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x47,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 73730,
        Z                   = -80,
        Y                   = -3560,
        Unknown_0C          = 208,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x47,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 53060,
        Z                   = -210,
        Y                   = 8160,
        Unknown_0C          = 61,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -74120,
        Y                   = -1000,
        Z                   = -14700,
        Range               = -71420,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFA92A,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = 72710,
        TriggerZ            = 0,
        TriggerY            = 10290,
        TriggerRange        = 1500,
        ActorX              = 72710,
        ActorZ              = 1500,
        ActorY              = 10290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45900,
        TriggerZ            = -60,
        TriggerY            = 4140,
        TriggerRange        = 1000,
        ActorX              = 45300,
        ActorZ              = 1440,
        ActorY              = 3640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_34A",          # 00, 0
        "Function_1_360",          # 01, 1
        "Function_2_3B0",          # 02, 2
        "Function_3_2F02",         # 03, 3
        "Function_4_2F22",         # 04, 4
        "Function_5_2F88",         # 05, 5
        "Function_6_32C3",         # 06, 6
        "Function_7_358D",         # 07, 7
        "Function_8_35B4",         # 08, 8
        "Function_9_37B5",         # 09, 9
        "Function_10_3955",        # 0A, 10
        "Function_11_3A1F",        # 0B, 11
    )


    def Function_0_34A(): pass

    label("Function_0_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_END)), "loc_35F")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_35F")

    Return()

    # Function_0_34A end

    def Function_1_360(): pass

    label("Function_1_360")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x385), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SoundLoad(119)
    SoundLoad(121)
    SoundLoad(502)

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390")
    OP_6F(0x4, 0)
    Jump("loc_397")

    label("loc_390")

    OP_6F(0x4, 60)

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_END)), "loc_3AC")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_3AC")

    OP_10(0x1, 0x1)
    Return()

    # Function_1_360 end

    def Function_2_3B0(): pass

    label("Function_2_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F01")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x103, 0x8, 0)
    SetChrPos(0x8, -60860, -320, 5360, 135)
    SetChrPos(0x9, -60550, -150, 2920, 341)
    SetChrPos(0xA, -59230, -300, 3520, 317)
    SetChrPos(0xB, -58760, -350, 5070, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8)
    OP_20(0xFA0)

    def lambda_499():
        OP_67(0, 6280, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_499)

    def lambda_4B1():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B1)
    OP_6D(-59790, -340, 4800, 4000)
    SetChrPos(0x101, -57980, 130, -9190, 356)
    SetChrPos(0x102, -56650, 110, -9280, 356)
    SetChrPos(0x103, -57400, -130, -10020, 356)
    OP_22(0x80, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x8, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_1D(0x57)

    ChrTalk(    #0
        0x8,
        (
            "#219FHehheh...\x01",
            "That was too easy.\x02\x03",

            "#219FAnd to think that something as\x01",
            "exquisite as this fell into my\x01",
            "hands with almost no effort.\x02\x03",

            "#219FWait till Don and Kyle hear\x01",
            "about this!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #1
        0x9,
        (
            "#6PYou surprised me,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#6PThe way you pulled off that act\x01",
            "wearing that school uniform was\x01",
            "simply astounding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xA,
        (
            "Just what you'd expect from the\x01",
            "mademoiselle of an ex-aristocratic\x01",
            "family.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x8,
        (
            "#219FYeah, yeah...but what's in the\x01",
            "past is in the past.\x02\x03",

            "#219FBut it certainly doesn't hurt\x01",
            "that in this outfit I can deceive\x01",
            "almost anyone.\x02\x03",

            "#219FThat gullible mayor and dim-witted\x01",
            "bracer girl...\x02\x03",

            "#410FIdiots! The whole lot of 'em!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_855():
        OP_6D(-58480, 30, -5380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_855)

    def lambda_86D():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_86D)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x101,
        "#005F(What was that?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#012F(Calm down... Let's see what\x01",
            "else they have to say.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "(Do you expect me to just sit here and listen to this?!)\x01",      # 0
            "(F-Fine! But I'm not happy about this...)\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4A")
    SetChrChipByIndex(0x101, 6)

    ChrTalk(    #7
        0x101,
        (
            "#005F(Do you expect me to just sit\x01",
            "here and listen to this?!)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9F1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F1)

    def lambda_9FF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9FF)
    OP_8E(0x101, 0xFFFF1974, 0x14, 0xFFFFDBF2, 0x1770, 0x0)

    def lambda_A21():

        label("loc_A21")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_A21")

    QueueWorkItem2(0x102, 1, lambda_A21)

    def lambda_A32():

        label("loc_A32")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_A32")

    QueueWorkItem2(0x103, 1, lambda_A32)
    OP_8E(0x101, 0xFFFF1406, 0x0, 0xFFFFE034, 0x1770, 0x0)

    def lambda_A57():
        OP_8E(0xFE, 0xFFFF1334, 0x1E, 0xFFFFF646, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A57)

    ChrTalk(    #8
        0x102,
        "#014F(What are you...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        "#025F(There she goes again...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#005F#6PHey! I hope you're all prepared\x01",
            "to take a beating!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 8)
    SetChrChipByIndex(0x103, 10)

    def lambda_AFD():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AFD)

    def lambda_B0D():
        OP_6D(-60120, -80, 1150, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B0D)

    def lambda_B25():
        OP_8E(0xFE, 0xFFFF1302, 0x14, 0xFFFFDD64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B25)
    Sleep(600)

    def lambda_B45():
        OP_8E(0xFE, 0xFFFF1302, 0x14, 0xFFFFDD64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B45)
    WaitChrThread(0x102, 0x1)

    def lambda_B65():
        OP_8E(0xFE, 0xFFFF0FB0, 0xFFFFFF74, 0xFFFFF114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B65)
    WaitChrThread(0x103, 0x1)

    def lambda_B85():
        OP_8E(0xFE, 0xFFFF16CC, 0xA, 0xFFFFF114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B85)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C0B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C0B)

    def lambda_C19():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C19)

    def lambda_C27():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C27)

    def lambda_C35():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C35)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Jump("loc_1105")

    label("loc_C4A")

    OP_2B(0x1A, 0x1)

    ChrTalk(    #11
        0x101,
        (
            "#509F(F-Fine! But I'm not happy\x01",
            "about this...)\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-59850, -340, 4500, 1500)

    ChrTalk(    #12
        0xB,
        (
            "Yeah, but that girl seemed\x01",
            "pretty tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        (
            "I mean, she took care of all the\x01",
            "monsters that appeared in the\x01",
            "mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#219FThe mine? Oh, so you're the\x01",
            "one who screwed up their job.\x02\x03",

            "#219FIf you had just done it like you were\x01",
            "supposed to, I wouldn't have had to\x01",
            "put on a monkey show to get this thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        "My apologies...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#219FEh, forget about it.\x01",
            "All's well that ends well.\x02\x03",

            "#219FAt any rate...those two kids being\x01",
            "bracers was an absolute joke.\x02\x03",

            "#219FEspecially, that brainless bimbo!\x01",
            "She honestly believed that we\x01",
            "could be friends!\x02\x03",

            "#410FWhadda freaking moron!\x01",
            "I had to try so hard just\x01",
            "to keep from laughing. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        "#3P#1KNow that IS rich!\x02",
    )


    ChrTalk(    #18
        0xB,
        (
            "#2P#1KWahahaha!\x01",
            "How stupid can she be?!\x02",
        )
    )


    ChrTalk(    #19
        0xA,
        (
            "#4P#1KHyahahaha!\x01",
            "It's just so absurd!!!\x02",
        )
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x102, 8)
    SetChrChipByIndex(0x103, 10)
    SetChrPos(0x101, -60670, 20, -8860, 270)
    SetChrPos(0x102, -60670, 20, -8860, 270)
    SetChrPos(0x103, -60670, 20, -8860, 270)

    ChrTalk(    #20
        0x101,
        "#5P...What's so funny?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1057():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1057)

    def lambda_1065():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1065)

    def lambda_1073():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1073)

    def lambda_1081():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1081)

    def lambda_108F():
        OP_8E(0xFE, 0xFFFF133E, 0x1E, 0xFFFFF650, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_108F)
    Sleep(300)

    def lambda_10AF():
        OP_8E(0xFE, 0xFFFF0FB0, 0xFFFFFF74, 0xFFFFF114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10AF)
    Sleep(300)

    def lambda_10CF():
        OP_8E(0xFE, 0xFFFF16CC, 0xA, 0xFFFFF114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10CF)

    def lambda_10EA():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10EA)
    OP_6D(-60120, -80, 1150, 1500)

    label("loc_1105")

    WaitChrThread(0x8, 0x1)

    ChrTalk(    #21
        0x8,
        "#411FI-It's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#582FYep. It's the 'brainless bimbo'\x01",
            "and her absolute joke of a\x01",
            "bracer partner.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(    #23
        0x101,
        (
            "#005F#3SAnd this probably won't come\x01",
            "as a surprise, but we're going\x01",
            "to beat you up now.\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x9, 3)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xA, 3)

    ChrTalk(    #24
        0xB,
        "What?! Bracers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        "How did they find...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        (
            "#027FYou did a fine job stealing that\x01",
            "septium from the mayor's residence,\x01",
            "but...\x02\x03",

            "#027FIt looks like you were a little\x01",
            "careless in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#012FIn accordance with the laws of the Bracer Guild,\x01",
            "you are hereby under arrest and charged with\x01",
            "breaking and entering, vandalism, and burglary.\x02\x03",

            "It would be in your best interest\x01",
            "not to resist, but I'm sure Estelle\x01",
            "is hoping you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xA,
        "This doesn't look good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "Wh-What are we going\x01",
            "to do now, Josette?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#412FHow about you quit quaking\x01",
            "in your boots for starters!\x02\x03",

            "These bracers are nothing more\x01",
            "than a ragtag group of kids!\x02\x03",

            "I think it's time we showed them the\x01",
            "real strength of the Capua family!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#005FWho are you to be calling us 'kids',\x01",
            "you...YOU BRAT!\x02\x03",

            "#005FI've had it up to here and I'm going\x01",
            "to do something about it right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        "#219FHey, that's my line!\x02",
    )

    CloseMessageWindow()

    def lambda_15B0():
        OP_6B(3000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15B0)

    def lambda_15C0():
        OP_6D(-60120, -80, 3200, 1000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_15C0)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0x8, 32, 800)
    SetChrChipByIndex(0x8, 0)
    OP_8C(0x8, 330, 800)
    OP_8C(0x8, 180, 800)
    Sleep(500)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #33
        0x8,
        "#210FAll right boys, get 'em!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        "#3P#1KMy pleasure!\x02",
    )


    ChrTalk(    #35
        0xA,
        "#2P#1KRoger that!\x02",
    )


    ChrTalk(    #36
        0x9,
        "#4P#1KUnderstood!\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    def lambda_1677():
        OP_6D(-60120, -80, 1150, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1677)
    SetChrChipByIndex(0xA, 4)

    def lambda_1694():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1694)
    SetChrChipByIndex(0x9, 4)

    def lambda_16AE():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16AE)
    SetChrChipByIndex(0xB, 4)

    def lambda_16C8():
        OP_92(0xFE, 0x103, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_16C8)
    SetChrChipByIndex(0x8, 1)

    def lambda_16E2():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16E2)
    Sleep(400)
    Battle(0x385, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_170F"),
        (SWITCH_DEFAULT, "loc_1714"),
    )


    label("loc_170F")

    OP_B4(0x0)
    Jump("loc_1714")

    label("loc_1714")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_6D(-56340, -330, 2350, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(68000, 0)
    OP_6E(291, 0)
    SetChrPos(0x103, -59720, -110, 320, 26)
    SetChrPos(0x102, -57190, -230, -570, 20)
    SetChrPos(0x101, -57720, -260, 480, 4)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 5)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xA, 5)
    SetChrPos(0x8, -55850, -280, 3840, 206)
    SetChrPos(0x9, -56410, -160, 5250, 213)
    SetChrPos(0xA, -54320, -160, 4210, 216)
    SetChrPos(0xB, -54160, -50, 5560, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #37
        0x8,
        "#216FHow in the world...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#502FYou had enough yet?\x01",
            "That's what you get for\x01",
            "taking bracers lightly.\x02\x03",

            "#507FAnd we'll be taking this back if\x01",
            "you don't mind, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x8, 0x320, 0xBB8, 0x0)
    Sleep(300)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x101, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x80, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #39
        "\x07\x00Recovered \x07\x02Septium Crystal\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #40
        0x8,
        (
            "#216FHey, that septium belongs\x01",
            "to me...\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x101, 0xFFFF2248, 0xFFFFFEC0, 0x848, 0x7D0, 0x0)

    ChrTalk(    #41
        0x101,
        (
            "#582FNo, not to you, to the people\x01",
            "of Rolent, that's who!\x02\x03",

            "#009FThe sheer nerve you have to\x01",
            "say something like that is\x01",
            "astounding...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x0)

    def lambda_1A9C():
        OP_8F(0xFE, 0xFFFF20C2, 0xFFFFFEE8, 0x2DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A9C)
    OP_8E(0x103, 0xFFFF1AC8, 0xFFFFFF06, 0x44C, 0xBB8, 0x0)
    OP_8E(0x103, 0xFFFF1F0A, 0xFFFFFED4, 0x6A4, 0xBB8, 0x0)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #42
        0x103,
        (
            "#021FNow that we've got the crystal\x01",
            "back, how about we move on to\x01",
            "confession time?\x02\x03",

            "#020FThat's an interesting name you\x01",
            "mentioned. The Capua family\x01",
            "was it...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x8,
        (
            "#216F(Me and my big mouth...)\x02\x03",

            "#211FI have absolutely no idea what you\x01",
            "are talking about.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 10)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #44
        0x103,
        (
            "#027FSo you want to be a tough egg to\x01",
            "crack do you? I don't mind at all.\x01",
            "In fact, I like them that way.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 12)
    OP_22(0x1F6, 0x0, 0x64)
    OP_99(0x103, 0x0, 0x4, 0x7D0)

    def lambda_1C95():
        OP_99(0x103, 0x7, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C95)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0x8, 0xFFFF268A, 0xFFFFFF24, 0x109A, 0x1F4, 0x1388)
    SetChrChipByIndex(0x8, 13)

    ChrTalk(    #45
        0x8,
        (
            "#213FAhhhhh!\x02\x03",

            "#214FWh-What are you trying to do?!\x01",
            "That's a dangerous thing to be\x01",
            "swinging around like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        (
            "#021FWell, if you can't answer with your\x01",
            "mouth then maybe your body can\x01",
            "answer instead.\x02\x03",

            "#021FBut don't worry,\x01",
            "I'll be EXTRA gentle.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)
    OP_8E(0x103, 0xFFFF2248, 0xFFFFFEC0, 0x848, 0x7D0, 0x0)
    TurnDirection(0x103, 0x8, 400)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 10)

    def lambda_1E09():

        label("loc_1E09")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_1E09")

    QueueWorkItem2(0x103, 1, lambda_1E09)
    OP_62(0x8, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #47
        0x8,
        (
            "#216FEek...\x02\x03",

            "#216FGet away from me, you crazy witch!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(    #48
        0x101,
        "#509F(I think Schera's enjoying this.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        "#019F(Let's just sit back and enjoy the show...)\x02",
    )

    CloseMessageWindow()
    OP_22(0x79, 0x1, 0x5A)
    Sleep(200)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 0)
    SetChrPos(0xD, -37060, 300, -13200, 291)
    TurnDirection(0x102, 0xD, 800)
    SetChrChipByIndex(0x102, 8)

    def lambda_1F72():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F72)

    ChrTalk(    #50
        0x102,
        "#016FLook out, Schera!\x02",
    )

    CloseMessageWindow()

    def lambda_1F9C():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F9C)
    OP_44(0x103, 0xFF)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x103, 0xD, 800)
    OP_96(0x103, 0xFFFF1A0A, 0xFFFFFF38, 0x104, 0x3E8, 0x1770)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -53890, -320, 1090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -54980, -320, 1650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -56310, -330, 2190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -57630, -300, 2760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -58980, -300, 3360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)

    ChrTalk(    #51
        0x103,
        "#023FAn orbal gun?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #52
        0x101,
        "#004FAre you all right, Schera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#024FI'm fine! Forget about me,\x01",
            "look at that!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 6)

    def lambda_2204():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2204)

    def lambda_2212():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2212)

    def lambda_2220():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2220)

    def lambda_222E():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_222E)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x40)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x3)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xE, 0x1, 0x0, 0x6)
    OP_B0(0x2, 0x1E)

    def lambda_2276():
        OP_6E(511, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2276)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x64)
    Sleep(2500)

    def lambda_2298():

        label("loc_2298")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2298")

    QueueWorkItem2(0x8, 1, lambda_2298)

    def lambda_22A9():

        label("loc_22A9")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_22A9")

    QueueWorkItem2(0x101, 1, lambda_22A9)

    def lambda_22BA():

        label("loc_22BA")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_22BA")

    QueueWorkItem2(0x103, 1, lambda_22BA)

    def lambda_22CB():

        label("loc_22CB")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_22CB")

    QueueWorkItem2(0x102, 1, lambda_22CB)

    def lambda_22DC():
        OP_6D(-61600, 3050, 5140, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22DC)

    def lambda_22F4():
        OP_6C(33000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_22F4)
    Sleep(5000)
    OP_43(0x9, 0x1, 0x0, 0x7)
    OP_43(0xB, 0x1, 0x0, 0x7)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(1000)

    ChrTalk(    #54
        0x101,
        "#580FAn airship?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#211FAh ha ha ha! Looks like the tables\x01",
            "are turned in our favor now,\x01",
            "aren't they?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2391():
        OP_8E(0xFE, 0xFFFF121C, 0xFFFFFEC0, 0x11D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2391)
    Sleep(200)
    SetChrChipByIndex(0x9, 4)

    def lambda_23B6():
        OP_8E(0xFE, 0xFFFF17B2, 0xFFFFFE8E, 0x159A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23B6)
    Sleep(200)
    SetChrChipByIndex(0xB, 4)

    def lambda_23DB():
        OP_8E(0xFE, 0xFFFF1668, 0xFFFFFEC0, 0x1040, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_23DB)
    Sleep(100)
    SetChrChipByIndex(0xA, 4)

    def lambda_2400():
        OP_8E(0xFE, 0xFFFF11A4, 0xFFFFFF4C, 0xC3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2400)
    WaitChrThread(0x8, 0x1)
    SetChrPos(0xC, -67370, 8500, 6060, 123)
    TurnDirection(0x8, 0xC, 0)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 3)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 3)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 3)
    WaitChrThread(0x101, 0x2)

    def lambda_245B():
        OP_6D(-62640, 4570, 5610, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_245B)

    def lambda_2473():
        OP_6E(363, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2473)

    def lambda_2483():
        OP_67(0, 10510, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2483)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x5F)
    OP_73(0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    OP_8F(0xC, 0xFFFEF8D6, 0x24B8, 0x17AC, 0xBB8, 0x0)
    Sleep(500)

    ChrTalk(    #56
        0xC,
        "#201FAre you okay, Josette?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "#214FKyle! You're late!\x01",
            "Where have you been?\x02\x03",

            "#210FOh, never mind, just hurry up\x01",
            "and give us a hand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xC,
        (
            "#201FNo can do. Our push into the\x01",
            "Rolent region has been put on\x01",
            "hold.\x02\x03",

            "Something big came up in the\x01",
            "Bose region while you were away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "#213FWhat's that supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xC,
        (
            "#201FI don't have time to explain.\x01",
            "Hurry and hop on or I'll have\x01",
            "to leave you behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0xC, 0xFFFEF8D6, 0x1F40, 0x17AC, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    OP_22(0xCE, 0x0, 0x64)
    OP_6F(0x2, 95)
    OP_70(0x2, 0xA0)

    ChrTalk(    #61
        0x8,
        "#215FCrap...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)

    def lambda_26C3():
        OP_8E(0xFE, 0xFFFF010B, 0xFFFFFF38, 0x13BA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_26C3)
    Sleep(200)

    def lambda_26E3():
        OP_6D(-61640, -300, 5890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_26E3)

    def lambda_26FB():
        OP_67(0, 9430, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26FB)

    def lambda_2713():
        OP_6C(9000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2713)
    SetChrChipByIndex(0x9, 4)

    def lambda_2728():
        OP_8E(0xFE, 0xFFFEBBB4, 0xFFFFFEB6, 0x6810, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2728)
    Sleep(200)
    SetChrChipByIndex(0xB, 4)

    def lambda_274D():
        OP_8E(0xFE, 0xFFFEBBB4, 0xFFFFFEB6, 0x6810, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_274D)
    Sleep(100)
    SetChrChipByIndex(0xA, 4)

    def lambda_2772():
        OP_8E(0xFE, 0xFFFEBBB4, 0xFFFFFEB6, 0x6810, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2772)

    def lambda_278D():
        OP_8E(0xFE, 0xFFFF19F6, 0xFFFFFEE8, 0x7D9, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_278D)

    def lambda_27A8():
        OP_8E(0xFE, 0xFFFF1410, 0x14, 0xFFFFFB46, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_27A8)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x8, 0x4)
    SetChrBattleFlags(0x8, 0x20)
    OP_96(0x8, 0xFFFEFDB8, 0x226, 0x125C, 0x3E8, 0x1F40)
    OP_8C(0x8, 160, 400)
    Sleep(500)

    ChrTalk(    #62
        0x101,
        (
            "#005FJust where do you think\x01",
            "you're going?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#214F#5PWe'll pick this up another day!\x01",
            "And don't think you've won either!\x02\x03",

            "#214FPayback's gonna be a beast!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2898():

        label("loc_2898")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2898")

    QueueWorkItem2(0x101, 0, lambda_2898)

    def lambda_28A9():

        label("loc_28A9")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_28A9")

    QueueWorkItem2(0x103, 0, lambda_28A9)

    def lambda_28BA():

        label("loc_28BA")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_28BA")

    QueueWorkItem2(0x102, 0, lambda_28BA)
    OP_22(0xCD, 0x0, 0x64)
    OP_43(0xD, 0x1, 0x0, 0x8)
    OP_43(0xE, 0x1, 0x0, 0x9)
    OP_43(0x8, 0x3, 0x0, 0x4)

    def lambda_28E5():
        OP_6D(-68070, 1230, 7050, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28E5)

    def lambda_28FD():
        OP_6C(69000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28FD)

    def lambda_290D():
        OP_6B(4000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_290D)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Sleep(3000)

    def lambda_2931():
        OP_6D(-60410, -60, 750, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2931)

    def lambda_2949():
        OP_67(0, 9000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2949)
    Sleep(3000)
    OP_82(0x2, 0x0)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_6D(-60200, -110, 1680, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(2009, 0)
    OP_6C(90000, 0)
    OP_6E(363, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, -60700, -40, 950, 225)
    SetChrPos(0x102, -60790, -80, 2280, 225)
    SetChrPos(0x103, -59390, -210, 1740, 225)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_24(0x79, 0x5F)
    OP_24(0xCD, 0x5F)
    Sleep(100)
    OP_24(0x79, 0x5A)
    OP_24(0xCD, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x55)
    OP_24(0xCD, 0x55)
    Sleep(100)
    OP_24(0x79, 0x50)
    OP_24(0xCD, 0x50)
    Sleep(50)
    OP_24(0x79, 0x46)
    OP_24(0xCD, 0x46)
    Sleep(50)
    OP_24(0x79, 0x3C)
    OP_24(0xCD, 0x3C)
    Sleep(50)
    OP_24(0x79, 0x32)
    OP_24(0xCD, 0x32)
    Sleep(50)
    OP_23(0x79)
    OP_23(0xCD)
    Sleep(500)
    OP_1D(0x15)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #64
        0x101,
        "#002F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#522FI sure wasn't expecting anything\x01",
            "like that to come out of the\x01",
            "woodwork...\x02\x03",

            "#021FHa ha ha. It looks like they caught\x01",
            "us all off guard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #66
        0x101,
        (
            "#007FThis isn't a laughing matter!\x02\x03",

            "#003FRight now I'm so frustrated I\x01",
            "don't even know what to think!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(    #67
        0x102,
        (
            "#019FWell, on the bright side, we did\x01",
            "get the Septium Crystal back.\x02\x03",

            "#012FSwitching gears...that group sure\x01",
            "looked to me like a bunch of sky\x01",
            "bandits.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(    #68
        0x103,
        (
            "#026FYes, they certainly seem\x01",
            "of that variety.\x02\x03",

            "It also sounds like they've made\x01",
            "the Bose region their base of\x01",
            "operations as well.\x02\x03",

            "#022FI certainly wouldn't have expected\x01",
            "a group like that to travel all the\x01",
            "way to a rural place like Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#509FI couldn't care less if they're\x01",
            "sky bandits or brigands!\x02\x03",

            "The next time I see that scruffy,\x01",
            "lying, jerk of a tomboy I'm going\x01",
            "to thwack-bam-kapow her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#019FWhat's 'thwack-bam-kapow'\x01",
            "supposed to mean...?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(    #71
        (
            "\x07\x05Thus the Septium Crystal stolen from the\x01",
            "mayor's residence was safely recovered.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #72
        (
            "\x07\x05After returning it to the mayor, Estelle\x01",
            "and the others returned to the guild to\x01",
            "report the details of the incident.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x266)
    OP_28(0x1B, 0x1, 0x80)
    OP_28(0x1B, 0x1, 0x100)
    Sleep(1000)
    NewScene("ED6_DT01/T0121   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_2F01")

    Return()

    # Function_2_3B0 end

    def Function_3_2F02(): pass

    label("Function_3_2F02")

    OP_24(0x79, 0x46)
    Sleep(500)
    OP_24(0x79, 0x50)
    Sleep(500)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x64)
    Return()

    # Function_3_2F02 end

    def Function_4_2F22(): pass

    label("Function_4_2F22")

    Sleep(6000)
    OP_24(0x79, 0x64)
    Sleep(200)
    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_23(0x77)
    OP_23(0x79)
    Return()

    # Function_4_2F22 end

    def Function_5_2F88(): pass

    label("Function_5_2F88")

    SetChrPos(0xFE, -37060, 17100, -13200, 291)
    LoadEffect(0x1, "map\\\\mp021_00.eff")

    def lambda_2FB3():
        OP_8E(0xFE, 0xFFFEF318, 0x283C, 0x24B8, 0x1838, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FB3)
    Sleep(3000)

    def lambda_2FD3():
        OP_8F(0xFE, 0xFFFEF318, 0x2454, 0x24B8, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FD3)
    Sleep(500)

    def lambda_2FF3():
        OP_8F(0xFE, 0xFFFEF318, 0x2454, 0x24B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FF3)

    def lambda_300E():
        OP_8C(0xFE, 155, 6)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_300E)
    Sleep(100)

    def lambda_3021():
        OP_8C(0xFE, 155, 8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3021)
    Sleep(100)

    def lambda_3034():
        OP_8C(0xFE, 155, 10)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3034)
    Sleep(100)

    def lambda_3047():
        OP_8C(0xFE, 155, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3047)
    Sleep(100)

    def lambda_305A():
        OP_8C(0xFE, 155, 14)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_305A)
    Sleep(100)

    def lambda_306D():
        OP_8C(0xFE, 155, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_306D)
    Sleep(100)

    def lambda_3080():
        OP_8C(0xFE, 155, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3080)
    Sleep(100)

    def lambda_3093():
        OP_8C(0xFE, 155, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3093)
    Sleep(100)

    def lambda_30A6():
        OP_8C(0xFE, 155, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_30A6)
    Sleep(100)

    def lambda_30B9():
        OP_8C(0xFE, 155, 25)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_30B9)

    def lambda_30C7():
        OP_8F(0xFE, 0xFFFEF318, 0x1C84, 0x24B8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30C7)
    Sleep(500)

    def lambda_30E7():
        OP_8F(0xFE, 0xFFFEF318, 0x1C84, 0x24B8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30E7)
    Sleep(100)

    def lambda_3107():
        OP_8C(0xFE, 155, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3107)
    Sleep(100)

    def lambda_311A():
        OP_8C(0xFE, 155, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_311A)
    Sleep(100)

    def lambda_312D():
        OP_8C(0xFE, 155, 32)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_312D)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xE, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)

    def lambda_317A():
        OP_8F(0xFE, 0xFFFEF318, 0x1C84, 0x24B8, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_317A)
    Sleep(100)

    def lambda_319A():
        OP_8C(0xFE, 155, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_319A)
    Sleep(100)

    def lambda_31AD():
        OP_8C(0xFE, 155, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31AD)
    Sleep(100)
    Sleep(100)

    def lambda_31C5():
        OP_8F(0xFE, 0xFFFEF318, 0xCE4, 0x24B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31C5)
    Sleep(300)

    def lambda_31E5():
        OP_8C(0xFE, 155, 25)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31E5)
    Sleep(100)

    def lambda_31F8():
        OP_8C(0xFE, 155, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31F8)
    Sleep(100)

    def lambda_320B():
        OP_8C(0xFE, 155, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_320B)

    def lambda_3219():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3219)
    Sleep(500)
    Sleep(300)

    def lambda_323E():
        OP_8C(0xFE, 155, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_323E)
    Sleep(100)

    def lambda_3251():
        OP_8C(0xFE, 155, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3251)
    Sleep(100)

    def lambda_3264():
        OP_8C(0xFE, 155, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3264)
    Sleep(100)

    def lambda_3277():
        OP_8C(0xFE, 155, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3277)
    Sleep(1000)

    def lambda_328A():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_328A)
    Sleep(2000)
    OP_82(0x2, 0x2)
    WaitChrThread(0xFE, 0x2)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Return()

    # Function_5_2F88 end

    def Function_6_32C3(): pass

    label("Function_6_32C3")

    SetChrPos(0xFE, -37060, 300, -13200, 291)

    def lambda_32DA():
        OP_8E(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x1838, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32DA)
    Sleep(3000)

    def lambda_32FA():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32FA)
    Sleep(500)

    def lambda_331A():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_331A)

    def lambda_3335():
        OP_8C(0xFE, 155, 6)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3335)
    Sleep(100)

    def lambda_3348():
        OP_8C(0xFE, 155, 8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3348)
    Sleep(100)

    def lambda_335B():
        OP_8C(0xFE, 155, 10)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_335B)
    Sleep(100)

    def lambda_336E():
        OP_8C(0xFE, 155, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_336E)
    Sleep(100)

    def lambda_3381():
        OP_8C(0xFE, 155, 14)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3381)
    Sleep(100)

    def lambda_3394():
        OP_8C(0xFE, 155, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3394)
    Sleep(100)

    def lambda_33A7():
        OP_8C(0xFE, 155, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_33A7)
    Sleep(100)

    def lambda_33BA():
        OP_8C(0xFE, 155, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_33BA)
    Sleep(100)

    def lambda_33CD():
        OP_8C(0xFE, 155, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_33CD)
    Sleep(100)

    def lambda_33E0():
        OP_8C(0xFE, 155, 25)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_33E0)

    def lambda_33EE():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33EE)
    Sleep(500)

    def lambda_340E():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_340E)
    Sleep(100)

    def lambda_342E():
        OP_8C(0xFE, 155, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_342E)
    Sleep(100)

    def lambda_3441():
        OP_8C(0xFE, 155, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3441)
    Sleep(100)

    def lambda_3454():
        OP_8C(0xFE, 155, 32)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3454)
    Sleep(100)

    def lambda_3467():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3467)
    Sleep(100)

    def lambda_3487():
        OP_8C(0xFE, 155, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3487)
    Sleep(100)

    def lambda_349A():
        OP_8C(0xFE, 155, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_349A)
    Sleep(100)
    Sleep(100)

    def lambda_34B2():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34B2)
    Sleep(300)

    def lambda_34D2():
        OP_8C(0xFE, 155, 25)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_34D2)
    Sleep(100)

    def lambda_34E5():
        OP_8C(0xFE, 155, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_34E5)
    Sleep(100)

    def lambda_34F8():
        OP_8C(0xFE, 155, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_34F8)

    def lambda_3506():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3506)
    Sleep(500)
    Sleep(300)

    def lambda_352B():
        OP_8C(0xFE, 155, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_352B)
    Sleep(100)

    def lambda_353E():
        OP_8C(0xFE, 155, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_353E)
    Sleep(100)

    def lambda_3551():
        OP_8C(0xFE, 155, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3551)
    Sleep(100)

    def lambda_3564():
        OP_8C(0xFE, 155, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3564)
    Sleep(1000)

    def lambda_3577():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3577)
    Return()

    # Function_6_32C3 end

    def Function_7_358D(): pass

    label("Function_7_358D")

    OP_99(0xFE, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0xFE, 3)
    TurnDirection(0xFE, 0xD, 200)

    def lambda_35A8():

        label("loc_35A8")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_35A8")

    QueueWorkItem2(0xFE, 2, lambda_35A8)
    Return()

    # Function_7_358D end

    def Function_8_35B4(): pass

    label("Function_8_35B4")

    LoadEffect(0x1, "map\\\\mp021_00.eff")
    PlayEffect(0x1, 0x2, 0xE, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_6F(0x2, 160)
    OP_70(0x2, 0xF0)

    def lambda_3616():
        OP_8F(0xFE, 0xFFFEF318, 0x2710, 0x24B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3616)

    def lambda_3631():
        OP_8C(0xFE, 243, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3631)
    Sleep(100)

    def lambda_3644():
        OP_8C(0xFE, 243, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3644)
    Sleep(100)

    def lambda_3657():
        OP_8C(0xFE, 243, 17)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3657)
    Sleep(500)
    Sleep(300)

    def lambda_366F():
        OP_8C(0xFE, 243, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_366F)
    Sleep(100)

    def lambda_3682():
        OP_8C(0xFE, 243, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3682)
    Sleep(100)
    Sleep(1000)

    def lambda_369A():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_369A)
    Sleep(500)

    def lambda_36BA():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36BA)
    Sleep(500)

    def lambda_36DA():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36DA)
    Sleep(500)

    def lambda_36FA():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36FA)
    Sleep(500)

    def lambda_371A():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_371A)
    Sleep(500)

    def lambda_373A():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_373A)
    Sleep(500)

    def lambda_375A():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_375A)
    Sleep(500)

    def lambda_377A():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_377A)
    Sleep(500)

    def lambda_379A():
        OP_8F(0xFE, 0xFFFEA0A2, 0x61A8, 0xFFFFB474, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_379A)
    Sleep(500)
    Return()

    # Function_8_35B4 end

    def Function_9_37B5(): pass

    label("Function_9_37B5")


    def lambda_37BB():
        OP_8F(0xFE, 0xFFFEF318, 0x12C, 0x24B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_37BB)

    def lambda_37D6():
        OP_8C(0xFE, 243, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_37D6)
    Sleep(100)

    def lambda_37E9():
        OP_8C(0xFE, 243, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_37E9)
    Sleep(100)

    def lambda_37FC():
        OP_8C(0xFE, 243, 17)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_37FC)
    Sleep(500)
    Sleep(300)

    def lambda_3814():
        OP_8C(0xFE, 243, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3814)
    Sleep(100)

    def lambda_3827():
        OP_8C(0xFE, 243, 12)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3827)
    Sleep(100)
    Sleep(2000)

    def lambda_383F():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_383F)
    Sleep(500)

    def lambda_385F():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_385F)
    Sleep(500)

    def lambda_387F():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_387F)
    Sleep(500)

    def lambda_389F():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_389F)
    Sleep(500)

    def lambda_38BF():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38BF)
    Sleep(500)

    def lambda_38DF():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38DF)
    Sleep(500)

    def lambda_38FF():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38FF)
    Sleep(500)

    def lambda_391F():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_391F)
    Sleep(500)

    def lambda_393F():
        OP_8F(0xFE, 0xFFFEA0A2, 0x12C, 0xFFFFB474, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_393F)
    Return()

    # Function_9_37B5 end

    def Function_10_3955(): pass

    label("Function_10_3955")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_39C6")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #73
        "\x07\x00Found \x07\x02Bear Claw\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x286)
    Jump("loc_3A16")

    label("loc_39C6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #74
        (
            "\x07\x00Found \x07\x02Bear Claw\x07\x00\x01",
            "but inventory full so gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3A16")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_3955 end

    def Function_11_3A1F(): pass

    label("Function_11_3A1F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF7, 1)"), scpexpr(EXPR_END)), "loc_3A99")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #75
        "\x07\x00Found \x07\x02Hide Jumpsuit\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x293)
    Jump("loc_3B17")

    label("loc_3A99")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #76
        (
            "\x07\x00Found \x07\x02Hide Jumpsuit\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Hide Jumpsuit\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_3B17")

    Jump("loc_3B5A")

    label("loc_3B1A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05The chest is o' so very empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x2)

    label("loc_3B5A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_3A1F end

    SaveToFile()

Try(main)
