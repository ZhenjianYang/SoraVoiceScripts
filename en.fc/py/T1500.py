from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1500   ._SN',
        MapName             = 'Bose',
        Location            = 'T1500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Lloyd',                                # 9
        'Elke',                                 # 10
        'Anette',                               # 11
        'Guardian',                             # 12
        'Joshua',                               # 13
        'Book',                                 # 14
        'Target Camera',                        # 15
        'Boat',                                 # 16
        'New Ansel Path',                       # 17
    )

    DeclEntryPoint(
        Unknown_00              = -7000,
        Unknown_04              = 0,
        Unknown_08              = 82000,
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
        Unknown_30              = 225,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 50,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01180 ._CH',             # 01
        'ED6_DT07/CH01210 ._CH',             # 02
        'ED6_DT09/CH10040 ._CH',             # 03
        'ED6_DT07/CH00010 ._CH',             # 04
        'ED6_DT07/CH00013 ._CH',             # 05
        'ED6_DT06/CH20032 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
        'ED6_DT06/CH20030 ._CH',             # 08
        'ED6_DT07/CH00003 ._CH',             # 09
        'ED6_DT06/CH20092 ._CH',             # 0A
        'ED6_DT06/CH20161 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01180P._CP',             # 01
        'ED6_DT07/CH01210P._CP',             # 02
        'ED6_DT09/CH10040P._CP',             # 03
        'ED6_DT07/CH00010P._CP',             # 04
        'ED6_DT07/CH00013P._CP',             # 05
        'ED6_DT06/CH20032P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
        'ED6_DT06/CH20030P._CP',             # 08
        'ED6_DT07/CH00003P._CP',             # 09
        'ED6_DT06/CH20092P._CP',             # 0A
        'ED6_DT06/CH20161P._CP',             # 0B
    )

    DeclNpc(
        X                   = -44990,
        Z                   = -1970,
        Y                   = 38500,
        Direction           = 190,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -9420,
        Z                   = 400,
        Y                   = 41260,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 3200,
        Z                   = -2000,
        Y                   = 42700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -45026,
        Z                   = -4000,
        Y                   = 32900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3882,
        Z                   = 500,
        Y                   = 41320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4990,
        Z                   = 900,
        Y                   = 41500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703943,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8640,
        Z                   = 0,
        Y                   = 96040,
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
        X                   = -34266,
        Y                   = -3000,
        Z                   = 54198,
        Range               = -31910,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xC274,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -29829,
        Y                   = -3000,
        Z                   = 55042,
        Range               = -27300,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xC5B2,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -5850,
        Y                   = -1000,
        Z                   = 80880,
        Range               = -10140,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x14438,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = -2900,
        TriggerZ            = -3000,
        TriggerY            = 30600,
        TriggerRange        = 3000,
        ActorX              = -2900,
        ActorZ              = -3000,
        ActorY              = 30600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_40E",          # 01, 1
        "Function_2_46C",          # 02, 2
        "Function_3_482",          # 03, 3
        "Function_4_4A6",          # 04, 4
        "Function_5_2839",         # 05, 5
        "Function_6_29A5",         # 06, 6
        "Function_7_2A90",         # 07, 7
        "Function_8_2BFB",         # 08, 8
        "Function_9_31BB",         # 09, 9
        "Function_10_3796",        # 0A, 10
        "Function_11_4A39",        # 0B, 11
        "Function_12_4E85",        # 0C, 12
        "Function_13_57F5",        # 0D, 13
        "Function_14_639D",        # 0E, 14
        "Function_15_67BE",        # 0F, 15
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2C2")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_3A5")

    label("loc_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_2CC")
    Jump("loc_3A5")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_2E5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_71(0x3, 0x4)
    Jump("loc_3A5")

    label("loc_2E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_319")
    SetChrChipByIndex(0xC, 5)
    SetChrPos(0xC, -6920, 700, 41300, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_71(0x3, 0x4)
    Jump("loc_3A5")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_332")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_71(0x3, 0x4)
    Jump("loc_3A5")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_END)), "loc_345")
    SetChrChipByIndex(0x8, 10)
    OP_44(0x8, 0xFF)
    Jump("loc_3A5")

    label("loc_345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_35D")
    SetChrChipByIndex(0x8, 10)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x8, 0x10)
    Jump("loc_3A5")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_376")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_3A5")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_38A")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_3A5")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3A5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3B3")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3CF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_3EB")
    SetMapFlags(0x10000000)
    OP_A3(0x3FC)
    Event(0, 11)
    OP_B1("t1500_y")

    label("loc_3EB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3F7"),
        (SWITCH_DEFAULT, "loc_40D"),
    )


    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40A")
    OP_A2(0x33B)
    Event(0, 8)

    label("loc_40A")

    Jump("loc_40D")

    label("loc_40D")

    Return()

    # Function_0_2AE end

    def Function_1_40E(): pass

    label("Function_1_40E")

    OP_16(0x2, 0xFA0, 0xFFFDC998, 0xFFFEE2D8, 0x30046)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43D")
    OP_B1("t1500_y")
    Jump("loc_446")

    label("loc_43D")

    OP_B1("t1500_n")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45A")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_466")

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466")
    OP_64(0x0, 0x1)

    label("loc_466")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_40E end

    def Function_2_46C(): pass

    label("Function_2_46C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_481")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_46C")

    label("loc_481")

    Return()

    # Function_2_46C end

    def Function_3_482(): pass

    label("Function_3_482")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A5")
    OP_8D(0xFE, 2000, 45800, 3600, 39900, 2000)
    Jump("Function_3_482")

    label("loc_4A5")

    Return()

    # Function_3_482 end

    def Function_4_4A6(): pass

    label("Function_4_4A6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_68A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_615")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "I've been watching you for\x01",
            "a bit and you've got some\x01",
            "darn good fishing skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#001FYou really think so?\x02\x03",

            "I've actually been fishing ever\x01",
            "since I was a little girl.\x02\x03",

            "Although, unlike you, Lloyd,\x01",
            "I only do it for fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I see. Well, if you ever decide to take\x01",
            "up the rod for a living, you're welcome\x01",
            "to join the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_687")

    label("loc_615")


    ChrTalk(    #3
        0xFE,
        (
            "Well, it looks like the bites\x01",
            "have stopped coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I guess it's past the peak\x01",
            "fishing time for the day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_687")

    Jump("loc_2835")

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_6CF")

    ChrTalk(    #5
        0xFE,
        (
            "Hi there, would you like to\x01",
            "try your hand at fishing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_76D")

    ChrTalk(    #6
        0xFE,
        (
            "The Guardian has already gotten\x01",
            "away from me once today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I guess I'll try searching for\x01",
            "another prime fishing spot\x01",
            "and try my luck again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_END)), "loc_264F")
    OP_A2(0x33D)
    OP_28(0x38, 0x1, 0x4)
    OP_28(0x38, 0x1, 0x8)
    OP_28(0x38, 0x1, 0x10)
    OP_28(0x38, 0x1, 0x20)
    OP_8C(0xFE, 180, 0)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-44970, -1970, 39550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, -44510, -1970, 39560, 180)
    SetChrPos(0x102, -44260, -1970, 40650, 180)
    SetChrPos(0x103, -45160, -1970, 40920, 180)
    SetChrPos(0x104, -45360, -1970, 39650, 180)
    OP_0D()

    NpcTalk(    #8
        0xFE,
        "Man with Pole",
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#501F#4PUm, excuse me...\x02\x03",

            "Are you the man named Lloyd\x01",
            "who's from the Royal City?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0xFE,
        "Man with Pole",
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#014FWow, he's really focused...\x01",
            "He's tuned everything out\x01",
            "of his mind but fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x104,
        (
            "#030F#4PIt looks like this is where my\x01",
            "skills come into play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#004FWhat are you...?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x104, 0x40)
    SetChrFlags(0x104, 0x4)
    OP_8E(0x104, 0xFFFF4E8A, 0xFFFFF84E, 0x96AA, 0x7D0, 0x0)
    OP_8C(0x104, 135, 400)
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    ChrTalk(    #14
        0x104,
        "#035FJust sit back and enjoy...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05Olivier leaned over, and with a smile that left all\x01",
            "kinds of things up to interpretation, blew into the\x01",
            "man's ear.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0x1F40)

    NpcTalk(    #16
        0xFE,
        "Man with Pole",
        (
            "#5SOh-oh-oh my goodness!\x01",
            "What in the...?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC3():
        OP_8E(0xFE, 0xFFFF4E44, 0xFFFFF84E, 0x9A24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC3)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 135, 400)
    SetChrChipByIndex(0xFE, 0)
    TurnDirection(0xFE, 0x104, 400)
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x4)

    NpcTalk(    #17
        0xFE,
        "Middle-Aged Man",
        "Wh-Who are you kids?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #18
        0xFE,
        "Middle-Aged Man",
        "A-And where did you come from?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#509FTh-That was a dirty trick to play\x01",
            "on him, Olivier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x103,
        "#025FYeah, that was pretty low.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        (
            "#031FHow do you do this evening,\x01",
            "good sir?\x02\x03",

            "We tried calling out to you a moment ago, but\x01",
            "we could see that, like a true professional,\x01",
            "your attention was fixed upon your task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#010FYou're Lloyd, aren't you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #23
        0xFE,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "But how did you know my name?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x103,
        (
            "#020FWe heard from a certain old man\x01",
            "about you.\x02\x03",

            "Do you have some time you could\x01",
            "spare to speak with us?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-44670, -2000, 43660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0xFE, -44640, -2000, 42760, 0)
    SetChrPos(0x101, -44550, -2000, 44760, 180)
    SetChrPos(0x102, -45710, -2000, 44500, 135)
    SetChrPos(0x103, -43620, -2000, 44550, 225)
    SetChrPos(0x104, -44920, -2000, 45730, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #26
        0x8,
        (
            "#3PI see...so you heard from\x01",
            "Mr. Kuwano, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#3PYeah, I saw that strange pair\x01",
            "about two nights ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#006FI knew it...\x02\x03",

            "Could we get you to fill us in\x01",
            "a little more on the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#3PBefore that, are you all bracers\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#3PIs this somehow related to some\x01",
            "sorta crime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#012FWe can't say for sure, but there\x01",
            "does appear to be a possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#3PGot'cha... In that case, I'll\x01",
            "do what I can to help you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#3PIt was the other night when\x01",
            "I was out fishing on my boat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#3PI was returning to the inn, dead\x01",
            "tired after a day of battling it out\x01",
            "with this lake's Guardian...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#3PIt had gotten late into the night, and\x01",
            "it was about the time when everyone at\x01",
            "the inn was asleep in their beds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#022F#6PNow hold on a minute.\x01",
            "What do you mean by\x01",
            "this lake's 'Guardian'?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #37
        0x8,
        "#3P#3SI'm glad you asked!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#3PThe Guardian is a giant salmon\x01",
            "that swims the murky depths of\x01",
            "Valleria Lake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#3PIt has been the feared king of\x01",
            "the waters among fishing-lovers\x01",
            "for over a decade!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0x103,
        "#522F#6P(Crap...I shouldn't have asked...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#017F(It looks like you've thrown a\x01",
            "log onto the maniac's fire...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#004FI-Is it really that huge of a fish\x01",
            "like you say?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #43
        0x8,
        (
            "#3PYou bet your last mira it is!\x01",
            "And I've been chasing the darn thing\x01",
            "for the last five years of my life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#3PIt comes and goes in different parts\x01",
            "of Valleria Lake and changes its\x01",
            "feeding spots on a whim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "#3PI heard from a buddy of mine that it\x01",
            "had appeared in these parts, so I\x01",
            "came a runnin' from the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x104,
        (
            "#035F#4PHa! Now that's what I call passion.\x01",
            "I can completely understand where\x01",
            "you're coming from.\x02\x03",

            "Whenever I find something I like,\x01",
            "I stop at nothing until I get ahold\x01",
            "of it.\x02\x03",

            "For example, a bottle of Grand\x01",
            "Chardonnay and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#509FIn your case 'steal it' is more\x01",
            "accurate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#026F#6P*cough* How about we get back\x01",
            "to our story?\x02\x03",

            "#020FSo Lloyd, what happened when you\x01",
            "came back from fishing that night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "#3POh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#3PI had returned the boat and was\x01",
            "on my way into the inn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#3PWhen I saw an odd couple head\x01",
            "out onto the road from the grounds\x01",
            "behind the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#014FOnto the road...in the middle of\x01",
            "the night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#3PYep, no doubt about it.\x01",
            "They headed out on the\x01",
            "New Ansel Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#3PAt first I thought they were a group\x01",
            "of people visiting from the city,\x01",
            "heading back home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#3PBut it was way too late for something like\x01",
            "that and when I asked at the inn the next\x01",
            "day, nobody knew a thing about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#3PThought maybe I'd seen a coupla\x01",
            "ghosts or something then!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #57
        0x101,
        (
            "#580FGh-ghosts?!\x02\x03",

            "Th-There are ghosts that come\x01",
            "out here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#3PHa ha, just so you know, the two\x01",
            "I saw were a young couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#3PThey mighta been two lost souls who committed\x01",
            "a double suicide after not being accepted by\x01",
            "those around them...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x101,
        "#504FAwww, d-don't tell me any more!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #61
        0x103,
        (
            "#027F#6POh, brother... A bracer that's afraid\x01",
            "of ghosts? The guild is doomed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #62
        0x102,
        (
            "#019FNot to mention, her habit of always\x01",
            "wanting to hear more ghost stories\x01",
            "and other bizarre stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x104,
        (
            "#031F#4PNow, now. Isn't your being scared\x01",
            "attractive in its own right, Estelle? Not\x01",
            "sexy, but cute nonetheless.\x02\x03",

            "Like a little kitten shivering\x01",
            "in the cold.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x101, 0x104, 800)

    ChrTalk(    #64
        0x101,
        (
            "#009F#6P...You'd better watch out because\x01",
            "this little kitten bites!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#3PHa ha ha. Well, I was just kidding\x01",
            "about the ghost part.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BE7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BE7)

    def lambda_1BF5():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BF5)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #66
        0x8,
        (
            "#3PBut the couple did, in fact, seem to\x01",
            "be one with a purpose and reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#3PI say this, because the girl was\x01",
            "wearing some rather odd clothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        "#014FWhat do you mean by that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#3PI only saw her from behind,\x01",
            "so I couldn't say for sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#3PBut it looked to me like she was\x01",
            "wearing some kinda school\x01",
            "uniform.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x101,
        (
            "#580FA school uniform...\x01",
            "It couldn't be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#012FIt wasn't one from the Jenis\x01",
            "Royal Academy was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#3PWow, you really know your\x01",
            "stuff, kid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#3PYou bet'cha. My niece goes there\x01",
            "as well, and it looked exactly the\x01",
            "same as the one she wears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x103,
        (
            "#026F#6PI see... This whole event just\x01",
            "got a lot more interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#005FIt's her! I know it's that lying\x01",
            "tomboy for sure!\x02\x03",

            "We're finally onto her trail!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#3PWhat...so she's an acquaintance\x01",
            "of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#3PThen while you're at it, tell the two\x01",
            "of them not to fret and rush into\x01",
            "anything they'll regret later on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#3PIf my mind isn't failing me, I coulda\x01",
            "sworn they said something about\x01",
            "coming again tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#014FIs that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#3PYep. 'We'll meet back here in two\x01",
            "days,' is what the young man said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#3PHis tone seemed rather serious,\x01",
            "so I couldn't help but think on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x103,
        (
            "#020F#6PWell, that's understandable...\x02\x03",

            "We appreciate the valuable information.\x01",
            "Just leave the rest up to us.\x02\x03",

            "We won't let them get into any more\x01",
            "trouble than they already are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "#3POh, I see...that's a relief to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#3PI feel like a weight's been lifted\x01",
            "off my shoulders now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#3PNow that that is off my chest\x01",
            "I feel like taking a boat out\x01",
            "and fishing again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#3PWell, there's no time to lose!\x01",
            "I'll leave you youngins to your\x01",
            "work!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22C7():

        label("loc_22C7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22C7")

    QueueWorkItem2(0x101, 1, lambda_22C7)

    def lambda_22D8():

        label("loc_22D8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22D8")

    QueueWorkItem2(0x102, 1, lambda_22D8)

    def lambda_22E9():

        label("loc_22E9")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22E9")

    QueueWorkItem2(0x103, 1, lambda_22E9)

    def lambda_22FA():

        label("loc_22FA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22FA")

    QueueWorkItem2(0x104, 1, lambda_22FA)
    OP_8E(0x8, 0xFFFF59C0, 0xFFFFF830, 0xA8CA, 0x1770, 0x0)
    OP_8E(0x8, 0xFFFF7270, 0xFFFFF830, 0xBEBE, 0x1770, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)

    ChrTalk(    #88
        0x101,
        (
            "#506F#6PMan...I don't even measure up when\x01",
            "it comes to that fishing nut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#010FHe mentioned something about a\x01",
            "'Fisherman's Guild' too. I wonder\x01",
            "what kind of group that is.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #90
        0x104,
        (
            "#033F#4PSo how is this couple involved with\x01",
            "the missing airliner incident exactly?\x02\x03",

            "If you don't mind telling me,\x01",
            "that is.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #91
        0x103,
        "#020F#6PWell, in a nutshell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #92
        (
            "\x07\x05Schera explained that they encountered\x01",
            "Josette in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #93
        0x104,
        (
            "#030F#4PI see... That seems to be the\x01",
            "person in question, all right.\x02\x03",

            "Which means that tonight is\x01",
            "the night, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        (
            "#020F#6PYeah...\x02\x03",

            "It looks like we should probably\x01",
            "get a room just in case.\x02\x03",

            "We're going to be in for a late\x01",
            "night tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#006F#6PAll right, let's go ask the receptionist\x01",
            "about a room.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_2835")

    label("loc_264F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BE")
    OP_A2(0x2)
    OP_A2(0x369)

    NpcTalk(    #96
        0xFE,
        "Man with Pole",
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#501FUm, could I ask you something?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #98
        0xFE,
        "Man with Pole",
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x103,
        "#023F(Wow, he's not responding at all...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        "#010F(He must be really into his fishing...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x104,
        (
            "#033F(Hmm... So this is what a fishing\x01",
            "maniac looks like, huh?\x02\x03",

            "#035F(They seem like a unique breed.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#509F(Not as 'unique' as you are,\x01",
            "that's for sure...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_27BE")


    NpcTalk(    #103
        0xFE,
        "Man with Pole",
        "...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #104
        (
            "\x07\x05The man seems to be concentrating\x01",
            "on his fishing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_2835")

    TalkEnd(0x8)
    Return()

    # Function_4_4A6 end

    def Function_5_2839(): pass

    label("Function_5_2839")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2934")
    OP_A2(0x1)

    ChrTalk(    #105
        0xFE,
        "It's so easy to relax here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "The surrounding scenery is great and\x01",
            "the food is absolutely delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "The only downside is that it's so cozy\x01",
            "here it's almost impossible to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "I want to stay here for several days.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29A1")

    label("loc_2934")


    ChrTalk(    #109
        0xFE,
        "It's so easy to relax here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "The surrounding scenery is great and\x01",
            "the food is absolutely delicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A1")

    TalkEnd(0x9)
    Return()

    # Function_5_2839 end

    def Function_6_29A5(): pass

    label("Function_6_29A5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2A38")

    ChrTalk(    #111
        0xFE,
        (
            "I'm thinking about inviting my\x01",
            "mom to go boat around the lake\x01",
            "in the afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "It looks like it will help me\x01",
            "with my diet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8C")

    label("loc_2A38")


    ChrTalk(    #113
        0xFE,
        "What a refreshing breeze.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Just taking a stroll around here\x01",
            "feels so good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A8C")

    TalkEnd(0xA)
    Return()

    # Function_6_29A5 end

    def Function_7_2A90(): pass

    label("Function_7_2A90")

    TalkBegin(0xC)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AB5")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2AD0")

    label("loc_2AB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ACB")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2AD0")

    label("loc_2ACB")

    SetChrSubChip(0xFE, 2)

    label("loc_2AD0")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #115
        0xC,
        (
            "#014FAren't you going to fish?\x02\x03",

            "That pier looks like a nice spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#007FTsk... How about you try too,\x01",
            "Joshua?\x02\x03",

            "You're not so bad yourself,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        (
            "#019FJust not as good as you.\x02\x03",

            "#010FI think I'll just sit here and watch\x01",
            "if all the fishing practice has\x01",
            "paid off.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xC)
    Return()

    # Function_7_2A90 end

    def Function_8_2BFB(): pass

    label("Function_8_2BFB")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-12880, 0, 26810, 0)
    OP_6B(5900, 0)
    OP_6C(45000, 0)
    StopSound(0x9470, 0x30D40, 0x0)
    SetChrPos(0x101, -9345, 0, 78200, 180)
    SetChrPos(0x102, -10370, 0, 78100, 180)
    SetChrPos(0x104, -8638, 0, 79300, 180)
    SetChrPos(0x103, -9788, 0, 79400, 180)

    def lambda_2C7C():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C7C)
    Sleep(1000)

    def lambda_2C91():
        OP_6D(-9385, 0, 77797, 9000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C91)
    OP_6B(3000, 9000)
    StopSound(0x9470, 0x186A0, 0x1F40)

    ChrTalk(    #118
        0x101,
        (
            "#000FSo this is the north shore of\x01",
            "Valleria Lake, huh...?\x02\x03",

            "It certainly seems peaceful and\x01",
            "quiet around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        (
            "#010FThe inn doesn't look too shabby\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x103,
        (
            "#020FI stayed here once before when I\x01",
            "was in the area on another job.\x02\x03",

            "The wine's great, the rooms are\x01",
            "nice...pretty much what you'd\x01",
            "expect from a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#007FToo bad this isn't a pleasure trip.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #122
        0x104,
        (
            "#033F#4PYou mean it's not? I, at least,\x01",
            "intended to toss my cares to\x01",
            "the wind for a while.\x02\x03",

            "#035FTaking catnaps in a rocking boat by\x01",
            "day and filling my belly with food\x01",
            "and wine by night... Heaven...\x02\x03",

            "This is what a vacation is all\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)
    TurnDirection(0x102, 0x104, 400)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #123
        0x101,
        "#009F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        "#018F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x103,
        "#027F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x104,
        (
            "#031F#4PHa ha ha. Come on everyone,\x01",
            "I was just joking.\x02\x03",

            "We can enjoy a vacation any time,\x01",
            "but now is the only time we can enjoy\x01",
            "taking care of some would-be thieves.\x02\x03",

            "Even I, Olivier Lenheim, know enough\x01",
            "to get my priorities straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#007F#3PI don't think this has anything to do\x01",
            "with enjoyment or not...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        (
            "#020F#6PHeh. Well, whatever. As long as he\x01",
            "does his share of the work he's\x01",
            "here to do.\x02\x03",

            "Let's see if we can find the old\x01",
            "man staying here that loves fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x102,
        (
            "#010FThe guest who said he saw some\x01",
            "suspicious individuals here two\x01",
            "nights ago, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x38, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_8_2BFB end

    def Function_9_31BB(): pass

    label("Function_9_31BB")

    EventBegin(0x0)
    OP_6D(1920, -2000, 40480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, -5540, 500, 43050, 180)
    SetChrPos(0x102, -5540, 500, 43050, 180)
    FadeToBright(1500, 0)
    OP_0D()

    def lambda_322C():
        OP_8E(0xFE, 0x3CA, 0xFFFFF830, 0xA60E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_322C)
    Sleep(800)

    def lambda_324C():
        OP_8E(0xFE, 0x3CA, 0xFFFFF830, 0xA60E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_324C)
    WaitChrThread(0x101, 0x1)

    def lambda_326C():
        OP_6D(1490, -2000, 38380, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_326C)

    def lambda_3284():
        OP_8E(0xFE, 0x8D4, 0xFFFFF830, 0x9B6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3284)
    WaitChrThread(0x102, 0x1)

    def lambda_32A4():
        OP_8E(0xFE, 0x668, 0xFFFFF830, 0xA104, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32A4)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0x102, 0x3)

    ChrTalk(    #130
        0x101,
        (
            "#004F#1PWow, what a picturesque view...\x02\x03",

            "The entire lake looks like it's\x01",
            "glowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        (
            "#010FToo bad we can't see the Royal City\x01",
            "on the opposite shore because of\x01",
            "the haze...\x02\x03",

            "But from here it's easy to tell\x01",
            "that this is the biggest lake in\x01",
            "the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#006F#1PThis lake is like a fisher's dream come\x01",
            "true... I bet it'd be a blast to throw\x01",
            "a line in those waters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#010FThen how 'bout it? It might be a\x01",
            "nice change of pace for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #134
        0x101,
        (
            "#501F#1PYeah, maybe I will.\x02\x03",

            "#501FWhat are you going to do,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        (
            "#010FMe? Umm, let's see...\x02\x03",

            "There's a book I've been meaning to\x01",
            "read, so maybe I'll just sit in that\x01",
            "chair and relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#009F#1PHow old are you again?\x01",
            "Only geezers talk about\x01",
            "'sitting back and relaxing'!\x02\x03",

            "Young boys are supposed to get\x01",
            "out and move their bodies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#019FAh ha ha...I'll leave that part\x01",
            "to you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_362A():

        label("loc_362A")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_362A")

    QueueWorkItem2(0x101, 1, lambda_362A)
    OP_8C(0x102, 270, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_8E(0x102, 0xFFFFE980, 0x1F4, 0xA708, 0xBB8, 0x0)
    SetChrChipByIndex(0xC, 5)
    SetChrPos(0xC, -6920, 700, 41300, 90)
    ClearChrFlags(0xC, 0x80)
    OP_44(0x101, 0xFF)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    SetChrPos(0x101, 2260, -2000, 39790, 225)
    TurnDirection(0x101, 0xC, 0)

    ChrTalk(    #138
        0x101,
        (
            "#007F#1PTsk... Sometimes you can be\x01",
            "such a drag.\x02\x03",

            "#006FOh well, I should hurry up and\x01",
            "decide on a fishing spot.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_6D(0, -2000, 35324, 1000)

    ChrTalk(    #139
        0x101,
        (
            "#006FHmm...somewhere around that pier\x01",
            "looks like it might be a lucky\x01",
            "spot for bites...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x33F)
    EventEnd(0x0)
    Return()

    # Function_9_31BB end

    def Function_10_3796(): pass

    label("Function_10_3796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A38")
    ClearMapFlags(0x1)
    EventBegin(0x0)

    ChrTalk(    #140
        0x101,
        (
            "#006FYes! This looks good...definitely\x01",
            "the best spot.\x02\x03",

            "Heehee. Now let's see\x01",
            "about casting a few lines...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Start fishing]\x01",      # 0
            "[Leave]\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_387D"),
        (0, "loc_38FB"),
        (SWITCH_DEFAULT, "loc_4A36"),
    )


    label("loc_387D")


    ChrTalk(    #141
        0x101,
        (
            "#000FUm...yeah, I think this is probably\x01",
            "the best spot...\x02\x03",

            "But maybe I should ask someone\x01",
            "at the inn just to be sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A36")

    label("loc_38FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 4)), scpexpr(EXPR_END)), "loc_49C7")
    OP_8E(0x101, 0xFFFFF48E, 0xFFFFF84E, 0x7EF4, 0x7D0, 0x0)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x1, 0x2)

    def lambda_3928():
        OP_6D(-3320, -1970, 30110, 3500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3928)

    def lambda_3940():
        OP_6C(225000, 3500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3940)

    def lambda_3950():
        OP_6B(3290, 3500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3950)

    def lambda_3960():
        OP_67(0, 9780, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3960)
    Sleep(3500)

    label("loc_3977")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49AA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AB9")

    ChrTalk(    #142
        0x101,
        "#000FI wonder what I should do?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Change fishing spot]\x01",      # 0
            "[Don't change]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A32"),
        (1, "loc_3AB3"),
        (SWITCH_DEFAULT, "loc_3AB6"),
    )


    label("loc_3A32")

    ClearChrFlags(0x101, 0x2)

    def lambda_3A3D():
        OP_6D(-2930, -1970, 32500, 1200)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3A3D)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_96(0x101, 0xFFFFF48E, 0xFFFFF84E, 0x7EF4, 0x258, 0xBB8)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #143
        0x101,
        (
            "#000FHmm. I wonder where the best place\x01",
            "to fish is...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB6")

    label("loc_3AB3")

    Jump("loc_3AB6")

    label("loc_3AB6")

    Jump("loc_3B31")

    label("loc_3AB9")

    OP_8C(0x101, 225, 400)
    Sleep(400)
    OP_8C(0x101, 135, 400)
    Sleep(400)
    OP_8C(0x101, 180, 400)
    Sleep(400)

    ChrTalk(    #144
        0x101,
        (
            "#000FLet's see...from this pier, which\x01",
            "would be the best place to drop a\x01",
            "line?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D62")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[To the west around the pier]\x01",                          # 0
            "[To the south where the sun is hitting the water]\x01",      # 1
            "[To the east where the shade reaches]\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C09"),
        (1, "loc_3C55"),
        (2, "loc_3CA1"),
        (SWITCH_DEFAULT, "loc_3CED"),
    )


    label("loc_3C09")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C19():
        OP_8C(0x101, 253, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C19)

    def lambda_3C27():
        OP_6C(278000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C27)

    def lambda_3C37():
        OP_6B(3290, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C37)
    OP_6D(-6980, -2200, 31000, 2000)
    Jump("loc_3CED")

    label("loc_3C55")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C65():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C65)

    def lambda_3C73():
        OP_6C(232000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C73)

    def lambda_3C83():
        OP_6B(3290, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C83)
    OP_6D(-3010, -2200, 29250, 2000)
    Jump("loc_3CED")

    label("loc_3CA1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3CB1():
        OP_8C(0x101, 100, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CB1)

    def lambda_3CBF():
        OP_6C(149000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CBF)

    def lambda_3CCF():
        OP_6B(3290, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CCF)
    OP_6D(1790, -2200, 32590, 2000)
    Jump("loc_3CED")

    label("loc_3CED")

    Sleep(1500)

    ChrTalk(    #145
        0x101,
        (
            "#006FRight around here looks nice.\x01",
            "C'mon fishy, fishy, fishes...\x02\x03",

            "#505FNow what should I do about bait?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E82")

    label("loc_3D62")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMUL_SAVE), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3D8B"),
        (100, "loc_3DCD"),
        (200, "loc_3E0F"),
        (SWITCH_DEFAULT, "loc_3E51"),
    )


    label("loc_3D8B")


    def lambda_3D91():
        OP_8C(0x101, 253, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D91)

    def lambda_3D9F():
        OP_6C(278000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D9F)

    def lambda_3DAF():
        OP_6B(3290, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3DAF)
    OP_6D(-6980, -2200, 31000, 1000)
    Jump("loc_3E51")

    label("loc_3DCD")


    def lambda_3DD3():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DD3)

    def lambda_3DE1():
        OP_6C(232000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DE1)

    def lambda_3DF1():
        OP_6B(3290, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3DF1)
    OP_6D(-3010, -2200, 29250, 1000)
    Jump("loc_3E51")

    label("loc_3E0F")


    def lambda_3E15():
        OP_8C(0x101, 100, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E15)

    def lambda_3E23():
        OP_6C(149000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E23)

    def lambda_3E33():
        OP_6B(3290, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E33)
    OP_6D(1790, -2200, 32590, 1000)
    Jump("loc_3E51")

    label("loc_3E51")


    ChrTalk(    #146
        0x101,
        (
            "#000FWhat should I do about bait this\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E82")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Use a lure]\x01",         # 0
            "[Use live bait]\x01",      # 1
            "[Use a fly]\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F00"),
        (1, "loc_3F0D"),
        (2, "loc_3F1A"),
        (SWITCH_DEFAULT, "loc_3F27"),
    )


    label("loc_3F00")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F27")

    label("loc_3F0D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F27")

    label("loc_3F1A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F27")

    label("loc_3F27")


    ChrTalk(    #147
        0x101,
        (
            "#001FAll right, let's sit back and relax,\x01",
            "and see what we come up with!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1500)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 11)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrSubChip(0x101, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE4")
    SetChrPos(0x101, -2950, -2200, 32080, 225)
    OP_0D()

    def lambda_3FC2():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3FC2)

    def lambda_3FD2():
        OP_6D(-4440, -2200, 30770, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FD2)

    label("loc_3FE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4031")
    SetChrPos(0x101, -2960, -2200, 32049, 180)
    OP_0D()

    def lambda_400F():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_400F)

    def lambda_401F():
        OP_6D(-2990, -2200, 31970, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_401F)

    label("loc_4031")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407E")
    SetChrPos(0x101, -2029, -2200, 32970, 90)
    OP_0D()

    def lambda_405C():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_405C)

    def lambda_406C():
        OP_6D(100, -2200, 32640, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_406C)

    label("loc_407E")

    OP_22(0x84, 0x0, 0x64)
    OP_99(0x101, 0x0, 0x6, 0x5DC)
    Sleep(400)
    OP_22(0x19, 0x0, 0x64)
    Sleep(1200)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40CE")
    Sleep(4000)
    Jump("loc_410A")

    label("loc_40CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E3")
    Sleep(3000)
    Jump("loc_410A")

    label("loc_40E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F8")
    Sleep(5000)
    Jump("loc_410A")

    label("loc_40F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_410A")
    Sleep(2000)

    label("loc_410A")

    OP_44(0x101, 0xFF)
    Fade(1000)

    def lambda_4119():
        OP_6B(2800, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4119)

    def lambda_4129():

        label("loc_4129")

        OP_99(0xFE, 0x8, 0xC, 0x5DC)
        OP_48()
        Jump("loc_4129")

    QueueWorkItem2(0x101, 3, lambda_4129)
    OP_63(0x101)
    Sleep(700)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #148
        0x101,
        (
            "#508FSweet! I got a bite!\x02\x03",

            "#002FNow this is the critical part.\x01",
            "How should I bring it up?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Reel it in all at once]\x01",                             # 0
            "[Wait a bit before reeling it in]\x01",                    # 1
            "[Wait until it gets tired before reeling it in]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #149
        0x101,
        "#009FAll right, let's see what we got!\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_42A4"),
        (1, "loc_42CC"),
        (2, "loc_4351"),
        (SWITCH_DEFAULT, "loc_43C8"),
    )


    label("loc_42A4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_44(0x101, 0xFF)
    OP_99(0x101, 0x6, 0x3, 0x5DC)
    OP_22(0x18, 0x0, 0x64)
    OP_99(0x101, 0x3, 0x1, 0x5DC)
    Jump("loc_43C8")

    label("loc_42CC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_44(0x101, 0xFF)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(300)
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    Sleep(100)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(200)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(300)
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    Sleep(100)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(200)
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    OP_99(0x101, 0x6, 0x3, 0x5DC)
    OP_22(0x18, 0x0, 0x64)
    OP_99(0x101, 0x3, 0x1, 0x5DC)
    Jump("loc_43C8")

    label("loc_4351")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_44(0x101, 0xFF)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(300)
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    Sleep(100)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(100)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    OP_99(0x101, 0x6, 0x1, 0x5DC)
    OP_9E(0x101, 0x1E, 0x0, 0x3E8, 0x1770)
    OP_99(0x101, 0x1, 0x3, 0x9C4)
    OP_99(0x101, 0x3, 0x1, 0x9C4)
    OP_22(0x18, 0x0, 0x64)
    Jump("loc_43C8")

    label("loc_43C8")

    Sleep(1000)
    OP_99(0x101, 0x10, 0x12, 0x5DC)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (100, "loc_4465"),
        (102, "loc_4465"),
        (112, "loc_4465"),
        (121, "loc_4465"),
        (122, "loc_4465"),
        (220, "loc_4465"),
        (0, "loc_4487"),
        (10, "loc_4487"),
        (20, "loc_4487"),
        (22, "loc_4487"),
        (110, "loc_4487"),
        (111, "loc_4487"),
        (120, "loc_4487"),
        (202, "loc_4487"),
        (210, "loc_4487"),
        (1, "loc_44A5"),
        (12, "loc_44A5"),
        (101, "loc_44A5"),
        (200, "loc_44A5"),
        (212, "loc_44A5"),
        (21, "loc_44C9"),
        (201, "loc_44C9"),
        (211, "loc_44C9"),
        (221, "loc_44C9"),
        (11, "loc_44EF"),
        (222, "loc_44EF"),
        (2, "loc_4516"),
        (SWITCH_DEFAULT, "loc_4535"),
    )


    label("loc_4465")


    AnonymousTalk(    #150
        "\x07\x00Reeled in \x07\x02Holey Boots\x07\x00!\x02",
    )

    Jump("loc_4535")

    label("loc_4487")


    AnonymousTalk(    #151
        "\x07\x00Reeled in a \x07\x02Smelt\x07\x00!\x02",
    )

    Jump("loc_4535")

    label("loc_44A5")


    AnonymousTalk(    #152
        "\x07\x00Reeled in a \x07\x02Liberl Carp\x07\x00!\x02",
    )

    Jump("loc_4535")

    label("loc_44C9")


    AnonymousTalk(    #153
        "\x07\x00Reeled in a \x07\x02Rainbow Trout\x07\x00!\x02",
    )

    Jump("loc_4535")

    label("loc_44EF")


    AnonymousTalk(    #154
        "\x07\x00Reeled in a \x07\x02Tiger Rockfish\x07\x00!\x02",
    )

    Jump("loc_4535")

    label("loc_4516")


    AnonymousTalk(    #155
        "\x07\x00Reeled in a \x07\x02Salmon\x07\x00!\x02",
    )

    Jump("loc_4535")

    label("loc_4535")

    FadeToBright(300, 0)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (100, "loc_45C9"),
        (102, "loc_45C9"),
        (112, "loc_45C9"),
        (121, "loc_45C9"),
        (122, "loc_45C9"),
        (220, "loc_45C9"),
        (0, "loc_460E"),
        (10, "loc_460E"),
        (20, "loc_460E"),
        (22, "loc_460E"),
        (110, "loc_460E"),
        (111, "loc_460E"),
        (120, "loc_460E"),
        (202, "loc_460E"),
        (210, "loc_460E"),
        (1, "loc_4698"),
        (12, "loc_4698"),
        (101, "loc_4698"),
        (200, "loc_4698"),
        (212, "loc_4698"),
        (21, "loc_46C7"),
        (201, "loc_46C7"),
        (211, "loc_46C7"),
        (221, "loc_46C7"),
        (11, "loc_46F4"),
        (222, "loc_46F4"),
        (2, "loc_474F"),
        (SWITCH_DEFAULT, "loc_483A"),
    )


    label("loc_45C9")

    OP_3E(0x11B, 1)

    ChrTalk(    #156
        0x101,
        (
            "#509FCurse you, Holey Boots...\x01",
            "This victory is yours...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483A")

    label("loc_460E")

    OP_3E(0x3AC, 1)

    ChrTalk(    #157
        0x101,
        (
            "#506FWhat a...little fishie... Joshua's gonna\x01",
            "make fun of me if he sees this. Should\x01",
            "I just eat it now to hide the evidence?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483A")

    label("loc_4698")

    OP_3E(0x3AD, 1)

    ChrTalk(    #158
        0x101,
        "#501FThis one is just my warm-up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_483A")

    label("loc_46C7")

    OP_3E(0x3AE, 1)

    ChrTalk(    #159
        0x101,
        "#000FNow THIS is quite a catch.\x02",
    )

    CloseMessageWindow()
    Jump("loc_483A")

    label("loc_46F4")

    OP_3E(0x3AF, 1)

    ChrTalk(    #160
        0x101,
        (
            "#508FWow, this one's a biggie. I believe\x01",
            "a little bragging may be in order.♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483A")

    label("loc_474F")

    OP_3E(0x3B0, 1)

    ChrTalk(    #161
        0x101,
        (
            "#001FYes yes YES! I am a GODDESS\x01",
            "of fishing! What a haul!\x02\x03",

            "#507FThis may just beat the record for the\x01",
            "size of my best catch to date!\x02\x03",

            "#502FI thought for certain it was just a\x01",
            "regular fish by the way it tugged\x01",
            "on the line.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_483A")

    label("loc_483A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4854")
    OP_83(0xD, 0x1)

    label("loc_4854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4864")
    OP_83(0xD, 0x2)

    label("loc_4864")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4874")
    OP_83(0xD, 0x3)

    label("loc_4874")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4884")
    OP_83(0xD, 0x4)

    label("loc_4884")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4894")
    OP_83(0xD, 0x5)

    label("loc_4894")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A4")
    OP_83(0xD, 0x6)

    label("loc_48A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B4")
    OP_83(0xD, 0x7)

    label("loc_48B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C4")
    OP_83(0xD, 0x8)

    label("loc_48C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48D4")
    OP_83(0xD, 0x9)

    label("loc_48D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E4")
    OP_83(0xD, 0xA)

    label("loc_48E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F7")
    Jump("loc_49AA")

    label("loc_48F7")

    OP_99(0x101, 0x12, 0x10, 0x5DC)
    Sleep(50)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #162
        0x101,
        (
            "#505FLet's see...\x02\x03",

            "What should I do now?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Continue fishing]\x01",      # 0
            "[Quit]\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49A2")
    Jump("loc_49AA")

    label("loc_49A2")

    Sleep(100)
    Jump("loc_3977")

    label("loc_49AA")

    OP_A2(0x345)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T1500   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_4A33")

    label("loc_49C7")

    OP_A2(0x346)

    ChrTalk(    #163
        0x101,
        (
            "#004FCrap...I don't have a fishing pole.\x02\x03",

            "I wonder if somebody at the inn\x01",
            "has a spare I can borrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A33")

    Jump("loc_4A36")

    label("loc_4A36")

    EventEnd(0x0)

    label("loc_4A38")

    Return()

    # Function_10_3796 end

    def Function_11_4A39(): pass

    label("Function_11_4A39")

    EventBegin(0x0)
    FadeToBright(5000, 0)
    OP_6D(-3320, -1970, 30110, 0)
    OP_6C(257000, 0)
    OP_6B(3290, 0)
    OP_67(0, 6980, -10000, 0)
    SetChrPos(0x101, -2930, -1970, 32500, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4850, 1140, 41360, 0)
    OP_64(0x0, 0x1)
    SetChrFlags(0xC, 0x80)

    def lambda_4AAE():
        OP_6D(-3013, -1970, 32740, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4AAE)

    def lambda_4AC6():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4AC6)

    def lambda_4AD6():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4AD6)

    def lambda_4AE6():
        OP_67(0, 11000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4AE6)
    Sleep(5000)

    ChrTalk(    #164
        0x101,
        (
            "#501FMan, it's already starting to get\x01",
            "dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#006FI guess I ended up with a pretty\x01",
            "good catch after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #166
        0x101,
        (
            "#001FCheck this out, Joshua!\x01",
            "Look what I caught!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BB3():
        OP_6D(-4150, 500, 37765, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BB3)

    def lambda_4BCB():
        OP_67(0, 4400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4BCB)

    def lambda_4BE3():
        OP_6B(3600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4BE3)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #167
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    def lambda_4C0A():
        OP_6D(-3850, 500, 42640, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C0A)

    def lambda_4C22():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C22)

    def lambda_4C3A():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4C3A)
    OP_8E(0x101, 0xFFFFF448, 0xFFFFF830, 0x9502, 0x1770, 0x0)
    OP_8E(0x101, 0x5A0, 0xFFFFF830, 0x9966, 0x1770, 0x0)
    OP_8E(0x101, 0x5A0, 0xFFFFF830, 0x9FF6, 0x1770, 0x0)
    OP_8E(0x101, 0xFFFFF0F6, 0x1F4, 0xA690, 0x1770, 0x0)

    ChrTalk(    #168
        0x101,
        "#002FJoshua?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 225, 400)

    ChrTalk(    #169
        0x101,
        "#004FWhat's this...?\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFEFE4, 0x1F4, 0xA433, 0x7D0, 0x0)
    SetChrFlags(0xD, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #170
        (
            "\x07\x00The book '\x07\x02Hundred Days War\x07\x00' seems to have\x01",
            "been left on the table. Estelle picked it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x331, 1)

    ChrTalk(    #171
        0x101,
        (
            "#501FI wonder if Joshua just forgot this.\x02\x03",

            "For being so sharp, he sure can\x01",
            "miss things sometimes.\x02\x03",

            "#001FI guess I'll just have to take it\x01",
            "to him myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 225, 400)
    Sleep(200)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #172
        0x101,
        (
            "#000FThen again, I wonder where he\x01",
            "could have taken off to...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_11_4A39 end

    def Function_12_4E85(): pass

    label("Function_12_4E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F4")
    EventBegin(0x0)
    AddParty(0x1, 0xFF)
    SetChrPos(0x102, -44990, -1970, 38500, 180)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 0)

    def lambda_4ED0():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4ED0)
    OP_6D(-44640, -1970, 41750, 3000)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -40520, -2000, 48190, 194)

    ChrTalk(    #173
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "Hey there, laddie!\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    OP_8E(0x101, 0xFFFF50BA, 0xFFFFF830, 0xA846, 0xBB8, 0x0)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #175
        0x101,
        (
            "#006F#4PWhat are you doing whittling away\x01",
            "the evening in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FBC():
        OP_8E(0xFE, 0xFFFF5038, 0xFFFFF84E, 0x9ECA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FBC)
    TurnDirection(0x102, 0x101, 400)
    OP_6D(-45080, -2000, 39790, 1500)

    ChrTalk(    #176
        0x102,
        (
            "#019FHa ha...not much.\x02\x03",

            "#010FHow about yourself? Are you done\x01",
            "fishing or are you heading back\x01",
            "into battle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#001F#4PNo, I've already had my fill.\x01",
            "It sure has been a while\x01",
            "since I did though.\x02\x03",

            "#501FOh...that reminds me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFF501A, 0xFFFFF84E, 0x9A4C, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #178
        "\x07\x05Estelle held out the book she found on the table.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #179
        0x101,
        (
            "#006F#4PYou said you were going to read,\x01",
            "but you ended up leaving your\x01",
            "book on the table.\x02\x03",

            "You should be more careful with\x01",
            "your stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x102,
        (
            "#013FOh, that...\x01",
            "I actually finished reading it.\x02\x03",

            "#010FMy eyes were starting to feel a bit\x01",
            "tired, so I thought I'd take a walk\x01",
            "for a change.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)
    OP_92(0x101, 0x102, 0x28A, 0x7D0, 0x0)

    ChrTalk(    #181
        0x101,
        "#007F#4PLiar.\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x102, 0x4)
    OP_8C(0x102, 45, 0)
    OP_8F(0x102, 0xFFFF4E80, 0xFFFFF84E, 0x954C, 0x7D0, 0x0)

    ChrTalk(    #182
        0x102,
        "#014FWh-What?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #183
        0x101,
        (
            "#509F#4PYou're hiding your feelings again,\x01",
            "aren't you?\x02\x03",

            "I can tell that's what you're doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#002F#4PAnd besides, that's not really fair.\x02\x03",

            "You always find a way to cheer\x01",
            "me up when I'm feeling down...\x02\x03",

            "#003FAnd while I may not be as reliable\x01",
            "as Dad...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x4)

    def lambda_53FE():
        OP_6D(-44980, -1970, 39200, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53FE)
    OP_8E(0x101, 0xFFFF5196, 0xFFFFF84E, 0x9574, 0x7D0, 0x0)
    TurnDirection(0x102, 0x101, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #186
        0x101,
        (
            "#000F#4PI can still give you a shoulder\x01",
            "to lean on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        (
            "#013F#3P...\x02\x03",

            "Sorry...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #188
        0x101,
        (
            "#006F#4PIt's times like these when you\x01",
            "should say, 'Thank you' and\x01",
            "not apologize.\x02\x03",

            "#006FYou may be smart, Joshua, but\x01",
            "sometimes you don't seem to\x01",
            "know what's most important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x102,
        (
            "#010F#3PHa ha. You're probably right.\x02\x03",

            "#019FThanks...Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#502F#4PVery good. Now that wasn't too\x01",
            "bad, was it?\x02\x03",

            "#004FOh...right!\x02\x03",

            "#001FAnd in return, how about you play\x01",
            "me a song on your harmonica?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x102,
        (
            "#015F#3PAs you wish...\x02\x03",

            "#010FIs 'The Whereabouts of Light' good\x01",
            "for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#001F#4PYep, that's the one\x01",
            "I wanted to hear.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_569D():
        OP_69(0x102, 0x5DC)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_569D)

    def lambda_56AB():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_56AB)
    OP_8F(0x101, 0xFFFF52F4, 0xFFFFF84E, 0x9524, 0x3E8, 0x0)
    Sleep(500)
    OP_96(0x101, 0xFFFF5452, 0xFFFFF9C0, 0x951A, 0x2BC, 0x1388)
    SetChrChipByIndex(0x101, 9)
    WaitChrThread(0x0, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x102, 8)
    Sleep(1000)
    OP_0D()

    def lambda_570A():

        label("loc_570A")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_570A")

    QueueWorkItem2(0x102, 1, lambda_570A)
    Sleep(500)
    OP_1D(0x46)
    Sleep(5000)
    SetChrPos(0xF, -30770, -3000, 32509, 273)
    SetChrFlags(0xF, 0x40)
    OP_A1(0xF, 0x3)
    OP_72(0x3, 0x4)
    Sleep(100)
    Fade(1000)
    OP_44(0x8, 0xFF)
    SetChrBattleFlags(0x8, 0x20)
    SetChrPos(0x8, -29670, -2900, 32420, 150)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)
    OP_6D(-29670, -1970, 32420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(213000, 0)
    OP_6E(307, 0)
    Sleep(2000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 2)
    Sleep(3000)
    OP_A2(0x3FB)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1510   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_57F4")

    Return()

    # Function_12_4E85 end

    def Function_13_57F5(): pass

    label("Function_13_57F5")

    SetChrFlags(0x8, 0x80)
    EventBegin(0x0)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x102, -45440, -1970, 38220, 90)
    SetChrPos(0x101, -43950, -1600, 38170, 270)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x102, 8)

    def lambda_5838():

        label("loc_5838")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_5838")

    QueueWorkItem2(0x102, 1, lambda_5838)
    OP_6D(-44980, -1970, 39200, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_21()
    OP_44(0x102, 0x1)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        (
            "#008F#4PI wonder why it is...\x02\x03",

            "...that when I hear the sound of your\x01",
            "harmonica in the evening light like\x01",
            "this it makes me want to cry.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x102, 180, 400)
    OP_1D(0x30)
    Sleep(1000)

    ChrTalk(    #194
        0x102,
        (
            "#013F#3P...\x02\x03",

            "So you're still not going to ask?\x01",
            "About my past, I mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#002F#4P...\x02\x03",

            "#506FWe promised, remember?\x02\x03",

            "You were going to tell me when you\x01",
            "felt like it, and I wasn't going to\x01",
            "ask, right?\x02\x03",

            "#006FAnd considering that five years\x01",
            "have passed, it doesn't seem like\x01",
            "such a big deal anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        (
            "#013F#3PYeah...it has been five years,\x01",
            "hasn't it?\x02\x03",

            "How can you just live with me for that\x01",
            "long and not have a million questions?\x02\x03",

            "#015FThat day, your father came home\x01",
            "with this beat-up kid...\x02\x03",

            "Some random stranger who never\x01",
            "says a word about his past...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 200)
    Sleep(500)

    ChrTalk(    #197
        0x102,
        "#012F#3PWhy'd you take him in like that...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)

    def lambda_5BA6():
        OP_96(0xFE, 0xFFFF52F4, 0xFFFFF84E, 0x9524, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BA6)

    ChrTalk(    #198
        0x101,
        "#501F#4PWell...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    def lambda_5BDE():
        OP_6D(-45440, -1970, 38220, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5BDE)
    OP_8E(0x101, 0xFFFF5196, 0xFFFFF84E, 0x9574, 0x3E8, 0x0)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #199
        0x101,
        (
            "#006FIt seemed like the obvious\x01",
            "thing to do.\x02\x03",

            "Besides, you're family now,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        (
            "#006FAnd like I said before, I know you\x01",
            "pretty well.\x02\x03",

            "#007FYou love books, you're a weapons geek,\x01",
            "and you've got a serious knack for just\x01",
            "about anything that comes your way...\x02\x03",

            "You're kind and fair, but you've also\x01",
            "got a way of not letting others inside\x01",
            "by using politeness like a shield...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        "#018FN-Now wait a minute...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #203
        0x101,
        "#001FAnd you're caring...and lonely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#007FOf course, I don't know everything\x01",
            "about your past...\x02\x03",

            "If you want to make comparisons,\x01",
            "I don't know a whole lot about\x01",
            "Dad's past either.\x02\x03",

            "#006FBut it doesn't mean that he and\x01",
            "I aren't family, right?\x02\x03",

            "Being a family for us has more to do\x01",
            "with me knowing his personality, his\x01",
            "habits, the food he likes...\x02\x03",

            "You know, the kinds of things that\x01",
            "only I would know firsthand.\x02\x03",

            "#001FAnd you're no different, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        (
            "#015F...\x02\x03",

            "#011FYou make it nearly impossible to argue with\x01",
            "you...you know that?\x02\x03",

            "It's been like that since the first time we met...\x01",
            "and you gave me that flying kick to the gut as I\x01",
            "was lying in bed...wounded, I might add.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #207
        0x101,
        (
            "#004FUm...\x02\x03",

            "D-Did I really do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        (
            "#019FYeah, injured and all...more\x01",
            "than once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#008FAh ha ha...I'm sure it was just a bit\x01",
            "of childish play...uh...blame Dad for\x01",
            "my lack of social graces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x102,
        (
            "#010FYeah sure, nice excuse.\x02\x03",

            "#015FBut anyway, Estelle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#501FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x102,
        (
            "#012FLet's make sure we solve this\x01",
            "whole airliner mystery.\x02\x03",

            "I don't know if Dad's been captured\x01",
            "or anything...\x02\x03",

            "But let's resolve this with our\x01",
            "own hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#006FSure...\x02\x03",

            "That's EXACTLY what\x01",
            "I intend to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x102,
        (
            "#010FHa ha...how about we head\x01",
            "back to the inn?\x02\x03",

            "I'm sure supper is ready by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#007FGreat idea, I'm starving.\x02\x03",

            "#006FWe need to eat our fill so we're\x01",
            "ready for tonight!\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrPos(0x101, -44940, -2000, 42440, 0)
    SetChrPos(0x102, -44940, -2000, 42440, 0)
    OP_69(0x101, 0x0)
    OP_A2(0x34C)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_1D(0xF)
    EventEnd(0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearMapFlags(0x10000000)
    Return()

    # Function_13_57F5 end

    def Function_14_639D(): pass

    label("Function_14_639D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67BD")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x34D)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #216
        0x101,
        "#004FOh, I almost forgot.\x02",
    )

    CloseMessageWindow()

    def lambda_63EF():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63EF)

    def lambda_63FD():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63FD)
    OP_6D(-30910, -850, 52160, 1500)

    ChrTalk(    #217
        0x101,
        "#000FHere's your book, Joshua...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #218
        0x102,
        "#014FOh, right.\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0x102, 0x384, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #219
        "\x07\x05Estelle held out the book she found on the table.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #220
        0x102,
        (
            "#010FI'm actually done with it...\x02\x03",

            "And at this point, it'd just end up\x01",
            "being bulk weight. I wonder what\x01",
            "I should do with it.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Can I read it?]\x01",                       # 0
            "[How about giving it to someone?]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_65C5"),
        (1, "loc_6736"),
        (SWITCH_DEFAULT, "loc_67BB"),
    )


    label("loc_65C5")


    ChrTalk(    #221
        0x101,
        (
            "#501FIt looks like a pretty difficult book,\x01",
            "but...do you think if I spent some\x01",
            "time with it I'd understand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x102,
        (
            "#010FI'm sure you'd be fine. There's\x01",
            "already a lot of stuff you know\x01",
            "in there anyway.\x02\x03",

            "So do you want to take a stab\x01",
            "at it, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        "#006FSure, I'll give it a shot.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #224
        "\x07\x00Received '\x07\x02Hundred Days War\x07\x00'.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x349)
    Jump("loc_67BB")

    label("loc_6736")

    OP_3F(0x331, 1)

    ChrTalk(    #225
        0x101,
        (
            "#501FHow about giving it to someone?\x01",
            "It'd be kind of a waste to just\x01",
            "chuck it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        "#010FYou're right...I'll do that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_67BB")

    label("loc_67BB")

    EventEnd(0x0)

    label("loc_67BD")

    Return()

    # Function_14_639D end

    def Function_15_67BE(): pass

    label("Function_15_67BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6874")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6816")
    OP_A2(0x3)

    ChrTalk(    #227
        0x101,
        (
            "#000FWait...this way leads back to the\x01",
            "New Ansel Path.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_685B")

    label("loc_6816")


    ChrTalk(    #228
        0x101,
        (
            "#007FIt wouldn't be too smart of me to\x01",
            "just take off by myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685B")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    EventEnd(0x0)
    Jump("loc_69F1")

    label("loc_6874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68F4")
    EventBegin(0x1)

    ChrTalk(    #229
        0x101,
        (
            "#000FWait...this way leads back to the\x01",
            "New Ansel Path.\x02\x03",

            "I wonder where Joshua went?\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    EventEnd(0x0)
    Jump("loc_69F1")

    label("loc_68F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69F1")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_698C")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #230
        0x102,
        (
            "#010FEstelle, where are you going?\x02\x03",

            "It's about time for us to get back\x01",
            "to the inn.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #231
        0x101,
        "#000FOh, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_69D6")

    label("loc_698C")


    ChrTalk(    #232
        0x102,
        (
            "#010FThis heads out onto the road.\x02\x03",

            "We'd better get back to the inn.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69D6")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_69F1")

    Return()

    # Function_15_67BE end

    SaveToFile()

Try(main)
