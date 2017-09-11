from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2310   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2310.x',
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
        'Deen',                                 # 9
        'Rais',                                 # 10
        'Rocco',                                # 11
        'Boy',                                  # 12
        'Boy',                                  # 13
        'Boy',                                  # 14
        'Boy',                                  # 15
        'Boy',                                  # 16
        'Boy',                                  # 17
        'Steward Gilbert',                      # 18
        'Carna',                                # 19
        'Amelia',                               # 20
        'Zack',                                 # 21
        'Solomon',                              # 22
        'Elder Serge',                          # 23
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
        'ED6_DT07/CH00374 ._CH',             # 00
        'ED6_DT07/CH02420 ._CH',             # 01
        'ED6_DT07/CH01240 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH00374P._CP',             # 00
        'ED6_DT07/CH02420P._CP',             # 01
        'ED6_DT07/CH01240P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
    )

    DeclNpc(
        X                   = -31270,
        Z                   = 0,
        Y                   = 42780,
        Direction           = 90,
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
        X                   = -30310,
        Z                   = 0,
        Y                   = 42270,
        Direction           = 90,
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
        X                   = -28770,
        Z                   = 0,
        Y                   = 42770,
        Direction           = 90,
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
        X                   = -31020,
        Z                   = 0,
        Y                   = 44700,
        Direction           = 90,
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
        X                   = -30070,
        Z                   = 0,
        Y                   = 44130,
        Direction           = 90,
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
        X                   = -29310,
        Z                   = 0,
        Y                   = 43790,
        Direction           = 90,
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
        X                   = -31330,
        Z                   = 0,
        Y                   = 43790,
        Direction           = 90,
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
        X                   = -30780,
        Z                   = 0,
        Y                   = 43810,
        Direction           = 90,
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
        X                   = -30050,
        Z                   = 0,
        Y                   = 43240,
        Direction           = 90,
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
        X                   = -26650,
        Z                   = 0,
        Y                   = 44050,
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
        X                   = -30050,
        Z                   = 0,
        Y                   = 39240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -200,
        Z                   = 0,
        Y                   = 8850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -25570,
        Z                   = 0,
        Y                   = 2300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -27510,
        Z                   = 0,
        Y                   = 8670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_2C2",          # 00, 0
        "Function_1_420",          # 01, 1
        "Function_2_442",          # 02, 2
        "Function_3_458",          # 03, 3
        "Function_4_12BE",         # 04, 4
        "Function_5_1D3E",         # 05, 5
        "Function_6_24F9",         # 06, 6
        "Function_7_3053",         # 07, 7
        "Function_8_30AE",         # 08, 8
    )


    def Function_0_2C2(): pass

    label("Function_0_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2FF")
    SetChrPos(0x14, -26670, 0, 39530, 90)
    SetChrPos(0x16, -30150, 0, 3860, 270)
    SetChrPos(0x15, -29310, 0, 43880, 0)
    Jump("loc_3E4")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_313")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    Jump("loc_3E4")

    label("loc_313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_31D")
    Jump("loc_3E4")

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_33B")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_3E4")

    label("loc_33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_359")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_3E4")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_396")
    SetChrPos(0x14, -26670, 0, 39530, 90)
    SetChrPos(0x16, -30150, 0, 3860, 270)
    SetChrPos(0x15, -29310, 0, 43880, 0)
    Jump("loc_3E4")

    label("loc_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrPos(0x14, -26670, 0, 39530, 90)
    SetChrPos(0x16, -30150, 0, 3860, 270)
    SetChrPos(0x15, -29310, 0, 43880, 0)
    Jump("loc_3E4")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_3E4")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3E4")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_411")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_411")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_41F")
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_41F")

    Return()

    # Function_0_2C2 end

    def Function_1_420(): pass

    label("Function_1_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_438")
    OP_B1("t2310_y")
    Jump("loc_441")

    label("loc_438")

    OP_B1("t2310_n")

    label("loc_441")

    Return()

    # Function_1_420 end

    def Function_2_442(): pass

    label("Function_2_442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_457")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_442")

    label("loc_457")

    Return()

    # Function_2_442 end

    def Function_3_458(): pass

    label("Function_3_458")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4C7")

    ChrTalk(    #0
        0xFE,
        (
            "Now, where'd Zack run off to\x01",
            "this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I was hoping to get him to go\x01",
            "to Ruan for me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535")
    OP_A2(0x1)

    ChrTalk(    #2
        0xFE,
        (
            "The crooks were holed up in the\x01",
            "Varenne Lighthouse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "I hope Mr. Vogt is okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_555")

    label("loc_535")


    ChrTalk(    #4
        0xFE,
        "I hope Mr. Vogt is okay...\x02",
    )

    CloseMessageWindow()

    label("loc_555")

    Jump("loc_12BA")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1")
    OP_A2(0x1)

    ChrTalk(    #5
        0xFE,
        (
            "I heard those kids were all crying\x01",
            "when they came back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "That really bothers me.\x01",
            "I wonder what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_611")

    label("loc_5E1")


    ChrTalk(    #7
        0xFE,
        (
            "Also, I wonder where Zack's\x01",
            "gone off to...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611")

    Jump("loc_12BA")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_C23")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AFF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8A")
    OP_28(0x1F, 0x1, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_777")

    ChrTalk(    #8
        0xFE,
        "Oh...the bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "My uncle hasn't come home yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#000FNo, it's all right.\x02\x03",

            "He's probably on his way to\x01",
            "Ruan right now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #11
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#010FYour uncle ran into some monsters\x01",
            "and was attacked while he was up\x01",
            "on the Krone Trail.\x02\x03",

            "Don't worry, he didn't get hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_992")

    label("loc_777")


    ChrTalk(    #14
        0xFE,
        (
            "Whew... I swear, when I get my\x01",
            "hands on my uncle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Why would he even go to the\x01",
            "Krone Trail on his own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#000FCome to think of it...\x02\x03",

            "Could he have been going there\x01",
            "to gather herbs or something?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #17
        0xFE,
        (
            "Yes, he might have said\x01",
            "something like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#000FThen he's just fine.\x02\x03",

            "He's on his way to Ruan\x01",
            "as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#010FYour uncle ran into some monsters\x01",
            "and was attacked while he was up\x01",
            "on the Krone Trail.\x02\x03",

            "Don't worry, though. We were there\x01",
            "in the nick of time, and he's fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_992")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #22
        0xFE,
        "Oh, thank goodness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I'm very sorry to have been such\x01",
            "a burden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I just wish he would've stopped by\x01",
            "the house before he left, so we could\x01",
            "talk things through as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "He's a stubborn old man, very set\x01",
            "in his ways.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC")

    label("loc_A8A")


    ChrTalk(    #26
        0xFE,
        (
            "I'm very sorry to have been such\x01",
            "a burden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "He's a stubborn old man, that Orvid.\x01",
            "Very set in his ways.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFC")

    Jump("loc_C20")

    label("loc_AFF")


    ChrTalk(    #28
        0xFE,
        (
            "We used to have three people living\x01",
            "under this roof, including Zack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Uncle Orvid moved out years ago,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "He does pop back in from wherever\x01",
            "he goes, on occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I wish Zack would get along a little\x01",
            "better with him, though. Maybe he'd\x01",
            "come home more often, then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C20")

    Jump("loc_12BA")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_D12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCD")
    OP_A2(0x1)

    ChrTalk(    #32
        0xFE,
        (
            "The fire at the orphanage\x01",
            "was arson?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "That's terrible...how could\x01",
            "someone do such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I have to go and help out at\x01",
            "Carla's later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0F")

    label("loc_CCD")


    ChrTalk(    #35
        0xFE,
        (
            "The fire at the orphanage\x01",
            "was arson?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "That's terrible...\x02",
    )

    CloseMessageWindow()

    label("loc_D0F")

    Jump("loc_12BA")

    label("loc_D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_E4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD4")
    OP_A2(0x1)

    ChrTalk(    #37
        0xFE,
        (
            "Zack tore out of here last night\x01",
            "when he found out about the fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I suppose he's still trying to help\x01",
            "out over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "He really is a very dependable person.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E48")

    label("loc_DD4")


    ChrTalk(    #40
        0xFE,
        (
            "Zack tore out of here last night\x01",
            "when he found out about the fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "He really is a very dependable person.\x02",
    )

    CloseMessageWindow()

    label("loc_E48")

    Jump("loc_12BA")

    label("loc_E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19")
    OP_A2(0x1)

    ChrTalk(    #42
        0xFE,
        (
            "*sigh* All this worrying about\x01",
            "my brother is going to be the\x01",
            "death of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "But Zack's always worried about\x01",
            "the family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "It's as if he's incapable of thinking\x01",
            "of himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9B")

    label("loc_F19")


    ChrTalk(    #45
        0xFE,
        (
            "*sigh* All this worrying about\x01",
            "my brother is going to be the\x01",
            "death of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "But Zack's always worried about\x01",
            "the family...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9B")

    Jump("loc_12BA")

    label("loc_F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_10FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107C")
    OP_A2(0x1)

    ChrTalk(    #47
        0xFE,
        (
            "I don't know what he intends to\x01",
            "do in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "If he doesn't get a job, no woman\x01",
            "is ever going to want to marry him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "He's been a source of constant\x01",
            "worry, ever since he was little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FA")

    label("loc_107C")


    ChrTalk(    #50
        0xFE,
        (
            "I don't know what he intends to\x01",
            "do in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "He's been a source of constant\x01",
            "worry, ever since he was little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FA")

    Jump("loc_12BA")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_116E")

    ChrTalk(    #52
        0xFE,
        "A little boy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "The only child in the village\x01",
            "is Lucia, so he's definitely\x01",
            "not from here...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_116E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_12BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1237")
    OP_A2(0x1)

    ChrTalk(    #54
        0xFE,
        (
            "Zack was fired from his job in\x01",
            "Ruan, so he came back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I have to wonder if he ever puts\x01",
            "any thought into his future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "His big sister is always\x01",
            "worried about him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_1237")


    ChrTalk(    #57
        0xFE,
        (
            "Zack was fired from his job in\x01",
            "Ruan, so he came back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I have to wonder if he ever puts\x01",
            "any thought into his future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BA")

    TalkEnd(0x13)
    Return()

    # Function_3_458 end

    def Function_4_12BE(): pass

    label("Function_4_12BE")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AE")
    OP_A2(0x0)

    ChrTalk(    #59
        0xFE,
        (
            "I'm in shock that the mayor\x01",
            "was involved in those crimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Well, at least the matron will\x01",
            "get some kind of reparations\x01",
            "if proof can be established.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "If the orphanage gets rebuilt,\x01",
            "I'd be glad to help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143F")

    label("loc_13AE")


    ChrTalk(    #62
        0xFE,
        (
            "At least the matron will get\x01",
            "some kind of reparations if\x01",
            "proof can be established.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "If the orphanage gets rebuilt,\x01",
            "I'd be glad to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143F")

    Jump("loc_1D3A")

    label("loc_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_15AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1533")
    OP_A2(0x0)

    ChrTalk(    #64
        0xFE,
        (
            "Were the arsonists really holed\x01",
            "up in the lighthouse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I'm guessing that you caught\x01",
            "them. I hope you gave them\x01",
            "a beating to remember!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Nice work! It's good to see you\x01",
            "bracers upholding the cause\x01",
            "of justice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_1533")


    ChrTalk(    #67
        0xFE,
        (
            "I heard that you caught\x01",
            "the arsonists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Nice work! It's good to see you\x01",
            "bracers upholding the cause\x01",
            "of justice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AC")

    Jump("loc_1D3A")

    label("loc_15AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1824")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_16B1")

    ChrTalk(    #69
        0xFE,
        (
            "You're the ones who helped\x01",
            "my uncle, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Thank you for taking the time.\x01",
            "I know you're busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Good luck with your investigation\x01",
            "into the orphanage case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Whoever's responsible needs to\x01",
            "be made to pay...in teeth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1821")

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A4")
    OP_A2(0x0)

    ChrTalk(    #73
        0xFE,
        (
            "We're finally done with the first\x01",
            "phase of cleaning up the site\x01",
            "of the fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "But more importantly, someone\x01",
            "did this on purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "They have to pay for what they\x01",
            "did...and the only currency I'll\x01",
            "accept is black eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1821")

    label("loc_17A4")


    ChrTalk(    #76
        0xFE,
        (
            "We're finally done with the first\x01",
            "phase of cleaning up the site\x01",
            "of the fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "They have to pay for what\x01",
            "they did...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1821")

    Jump("loc_1D3A")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1922")
    OP_A2(0x0)

    ChrTalk(    #78
        0xFE,
        "Ruan certainly is changing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "The entire town used to be\x01",
            "built around trade and fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Nowadays, though, it's been\x01",
            "turning into a big tourist trap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Rumor has it that there's been\x01",
            "some civil unrest there lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1971")

    label("loc_1922")


    ChrTalk(    #82
        0xFE,
        (
            "Rumor has it that there's some\x01",
            "civil unrest going on in Ruan,\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1971")

    Jump("loc_1D3A")

    label("loc_1974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A77")
    OP_A2(0x0)

    ChrTalk(    #83
        0xFE,
        (
            "Headed to the Mercia Orphanage,\x01",
            "are you? You're good kids. I go\x01",
            "there myself, from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Solomon and I sometimes go\x01",
            "to help out with some of the\x01",
            "manual labor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Matron Theresa doesn't have\x01",
            "any men around to help out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1A")

    label("loc_1A77")


    ChrTalk(    #86
        0xFE,
        (
            "Headed to the Mercia Orphanage,\x01",
            "are you? You're good kids. I go\x01",
            "there myself, from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Matron Theresa doesn't have\x01",
            "any men around to help out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1A")

    Jump("loc_1D3A")

    label("loc_1B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_1B9C")

    ChrTalk(    #88
        0xFE,
        "A little boy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I've been in and around this house all\x01",
            "day, and I've seen no little boys, I'm\x01",
            "afraid. Sorry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D3A")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1D3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C97")
    OP_A2(0x0)

    ChrTalk(    #90
        0xFE,
        (
            "I used to work at the harbor in\x01",
            "Ruan, but I came back to the\x01",
            "village of my birth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "I'll probably wind up settling\x01",
            "down right where I was born\x01",
            "and raised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "The only downside is that my\x01",
            "oh-so-delightful sister is here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D3A")

    label("loc_1C97")


    ChrTalk(    #93
        0xFE,
        (
            "I used to work at the harbor in\x01",
            "Ruan, but I came back to the\x01",
            "village of my birth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I'll probably wind up settling\x01",
            "down right where I was born\x01",
            "and raised.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3A")

    TalkEnd(0x14)
    Return()

    # Function_4_12BE end

    def Function_5_1D3E(): pass

    label("Function_5_1D3E")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D8F")

    ChrTalk(    #95
        0xFE,
        (
            "I can hear the kids' voices\x01",
            "from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "Aidios be praised.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1E21")

    ChrTalk(    #97
        0xFE,
        (
            "I'm just glad that the arsonists\x01",
            "have been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I'm impressed with you bracers.\x01",
            "It's a good thing we had you to\x01",
            "depend on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F11")
    OP_A2(0x2)

    ChrTalk(    #99
        0xFE,
        (
            "Matron Theresa and the kids\x01",
            "were mugged...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "If it was the same people that set the\x01",
            "fire, what in the world can they hope\x01",
            "to gain besides the wrath of Aidios?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Those kids have done nothing\x01",
            "to deserve this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBB")

    label("loc_1F11")


    ChrTalk(    #102
        0xFE,
        (
            "If it was the same people that set the\x01",
            "fire, what in the world can they hope\x01",
            "to gain besides the wrath of Aidios?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Those kids have done nothing\x01",
            "to deserve this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBB")

    Jump("loc_24F5")

    label("loc_1FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_20E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2074")
    OP_A2(0x2)

    ChrTalk(    #104
        0xFE,
        (
            "There's nothing left of the\x01",
            "orphanage but rubble and\x01",
            "ashes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "That fire must have been\x01",
            "burning super-hot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "There were so many memories\x01",
            "made there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_2074")


    ChrTalk(    #107
        0xFE,
        (
            "There's nothing left of the\x01",
            "orphanage but rubble and\x01",
            "ashes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "There were so many memories\x01",
            "made there...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E4")

    Jump("loc_24F5")

    label("loc_20E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2194")
    OP_A2(0x2)

    ChrTalk(    #109
        0xFE,
        (
            "Zack and I are bringing some food\x01",
            "over to the orphanage today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "It should be enough for all\x01",
            "of the kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "I'd better start getting set up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21FE")

    label("loc_2194")


    ChrTalk(    #112
        0xFE,
        (
            "Zack and I are bringing some food\x01",
            "over to the orphanage today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "I'd better start getting set up.\x02",
    )

    CloseMessageWindow()

    label("loc_21FE")

    Jump("loc_24F5")

    label("loc_2201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2360")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EB")
    OP_A2(0x2)

    ChrTalk(    #114
        0xFE,
        (
            "Everyone in the village tries to\x01",
            "help the Mercia Orphanage out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Matron Theresa's already gone\x01",
            "through so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Ever since Zack quit his job\x01",
            "and returned to the village,\x01",
            "he's been going there a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235D")

    label("loc_22EB")


    ChrTalk(    #117
        0xFE,
        (
            "Everyone in town tries to help\x01",
            "the Mercia Orphanage out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Matron Theresa's already gone\x01",
            "through so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235D")

    Jump("loc_24F5")

    label("loc_2360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_23A0")

    ChrTalk(    #119
        0xFE,
        "A boy in a cap?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "Sorry...I haven't seen him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_23A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_24F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2487")
    OP_A2(0x2)

    ChrTalk(    #121
        0xFE,
        "Oh, are you travelers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "If you're looking for a place\x01",
            "to eat, I'd suggest you try\x01",
            "the White Magnolia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "They've got good food and\x01",
            "you get a fair amount for\x01",
            "your money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "It's worth checking out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_2487")


    ChrTalk(    #125
        0xFE,
        (
            "If you're looking for a place\x01",
            "to eat, I'd suggest you try\x01",
            "the White Magnolia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "It's right next door.\x02",
    )

    CloseMessageWindow()

    label("loc_24F5")

    TalkEnd(0x15)
    Return()

    # Function_5_1D3E end

    def Function_6_24F9(): pass

    label("Function_6_24F9")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_25B1")

    ChrTalk(    #127
        0xFE,
        (
            "It's hard to believe that Mayor\x01",
            "Dalmore was capable of such\x01",
            "vile acts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Whether one can believe it or\x01",
            "not, what puzzles me most is\x01",
            "why he would do such things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_25B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_26AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2655")
    OP_A2(0x3)

    ChrTalk(    #129
        0xFE,
        (
            "Ahh, the bracers. You have\x01",
            "apprehended the criminals,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "If there is anything we can do\x01",
            "for you, please don't hesitate\x01",
            "to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AC")

    label("loc_2655")


    ChrTalk(    #131
        0xFE,
        "It is beyond all reason...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "What could drive a man to\x01",
            "commit such atrocities?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AC")

    Jump("loc_304F")

    label("loc_26AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_27C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2755")
    OP_A2(0x3)

    ChrTalk(    #133
        0xFE,
        "I heard about what happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "For such violence to be incurred\x01",
            "not just once, but twice over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "A case like this pains\x01",
            "me greatly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C4")

    label("loc_2755")


    ChrTalk(    #136
        0xFE,
        (
            "For such violence to be incurred\x01",
            "not just once, but twice over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "A case like this pains\x01",
            "me greatly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C4")

    Jump("loc_304F")

    label("loc_27C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_28E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2885")
    OP_A2(0x3)

    ChrTalk(    #138
        0xFE,
        (
            "It seems that the orphaned \x01",
            "children are recovering their\x01",
            "spirit, little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "They've settled in enough for\x01",
            "me to hear them laughing,\x01",
            "from time to time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DE")

    label("loc_2885")


    ChrTalk(    #140
        0xFE,
        (
            "It seems that the orphaned \x01",
            "children are recovering their\x01",
            "spirit, little by little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DE")

    Jump("loc_304F")

    label("loc_28E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B9")
    OP_A2(0x3)

    ChrTalk(    #141
        0xFE,
        (
            "Rex offered them a room at\x01",
            "the White Magnolia, which\x01",
            "was of great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "In times of need, we must\x01",
            "pull together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "We will do whatever we can\x01",
            "to help Matron Theresa and\x01",
            "the orphans.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2F")

    label("loc_29B9")


    ChrTalk(    #144
        0xFE,
        (
            "In times of need, we must\x01",
            "pull together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "We will do whatever we can\x01",
            "to help Matron Theresa and\x01",
            "the orphans.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2F")

    Jump("loc_304F")

    label("loc_2A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_2C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B70")
    OP_A2(0x3)

    ChrTalk(    #146
        0xFE,
        (
            "Last night I saw the eastern sky turn\x01",
            "red, and the stars were hidden from\x01",
            "view by the rising smoke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I sent young men from the village\x01",
            "to combat the blaze...but alas,\x01",
            "we couldn't save the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "At least, there is some small\x01",
            "comfort to be found in the\x01",
            "fact that no one was hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C40")

    label("loc_2B70")


    ChrTalk(    #149
        0xFE,
        (
            "Last night I saw the eastern sky turn\x01",
            "red, and the stars were hidden from\x01",
            "view by the rising smoke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "I sent young men from the village\x01",
            "to combat the blaze...but alas,\x01",
            "we couldn't save the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C40")

    Jump("loc_304F")

    label("loc_2C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2F")
    OP_A2(0x3)

    ChrTalk(    #151
        0xFE,
        (
            "The Gull Seaside Way leads \x01",
            "to Ruan. Some call it the\x01",
            "Sea Breeze Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "The view is impressive, and\x01",
            "the breeze from over the\x01",
            "water is very pleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I make a point of taking a\x01",
            "walk out there each day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCE")

    label("loc_2D2F")


    ChrTalk(    #154
        0xFE,
        (
            "The Gull Seaside Way leads \x01",
            "to Ruan. Some call it the\x01",
            "Sea Breeze Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "The view is impressive, and\x01",
            "the breeze from over the\x01",
            "water is quite pleasant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCE")

    Jump("loc_304F")

    label("loc_2DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2E8B")

    ChrTalk(    #156
        0xFE,
        (
            "Matron Theresa occasionally\x01",
            "brings the children to Manoria\x01",
            "from the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "They're all very close...as though\x01",
            "they were bound by blood,\x01",
            "rather than circumstance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_2EC4")

    ChrTalk(    #158
        0xFE,
        "A young boy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "He hasn't come here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_304F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC6")
    OP_A2(0x3)

    ChrTalk(    #160
        0xFE,
        (
            "Ah, more travelers.\x01",
            "Welcome to Manoria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "At one time, this village was\x01",
            "quite renowned for its inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "But with the advent of airships,\x01",
            "we've seen far less traffic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "Nowadays, we survive only\x01",
            "because of the famous flowers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2FC6")


    ChrTalk(    #164
        0xFE,
        (
            "With the advent of airships,\x01",
            "we see far less traffic than\x01",
            "we used to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Nowadays, we survive only\x01",
            "because of the famous flowers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304F")

    TalkEnd(0x16)
    Return()

    # Function_6_24F9 end

    def Function_7_3053(): pass

    label("Function_7_3053")

    TalkBegin(0x12)

    ChrTalk(    #166
        0x12,
        (
            "I'll keep an eye on these fools.\x02\x03",

            "You guys go to Ruan and report\x01",
            "back to Jean.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_7_3053 end

    def Function_8_30AE(): pass

    label("Function_8_30AE")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-29840, 0, 41310, 0)
    RemoveParty(0x5, 0xFF)
    SetChrPos(0x101, -29970, 0, 37680, 0)
    SetChrPos(0x102, -30850, 0, 37060, 0)
    SetChrPos(0x105, -29450, 0, 36780, 0)
    OP_8C(0x12, 180, 0)

    ChrTalk(    #167
        0x12,
        (
            "Now then... I'll keep an eye on\x01",
            "things here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x12,
        (
            "Could you return to Ruan and\x01",
            "report back to Jean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#000FThat's fine with me, but are\x01",
            "you sure you'll be okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x12,
        (
            "C'mon, I just got a whiff of\x01",
            "sleeping powder is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x12,
        (
            "It's pretty pathetic, though.\x01",
            "I can't believe I let those\x01",
            "idiots get the better of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        (
            "#010FDon't beat yourself up over it.\x02\x03",

            "You still managed to defeat\x01",
            "four attackers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x105,
        (
            "#040FThe children are safe thanks\x01",
            "to you.\x02\x03",

            "I can't thank you enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x12,
        (
            "Ha ha... Well, I guess there's\x01",
            "that, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x12,
        (
            "Still, will Agate be okay facing\x01",
            "them on his own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x12,
        (
            "I know he's tough and all,\x01",
            "but it still worries me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#000FY-Yeah... If they somehow\x01",
            "manage to get the drop on\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        (
            "#010FFor now, we just have to trust\x01",
            "that he knows what he's doing. \x02\x03",

            "He's been after those guys\x01",
            "for a while now.\x02\x03",

            "He knows how they work, so I think\x01",
            "they'll have a tough time taking\x01",
            "him on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#000FYeah, I guess you're right!\x02\x03",

            "We'll just have to focus on\x01",
            "what WE can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x12,
        (
            "You're right.\x01",
            "You're exactly right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x12,
        (
            "I'll hang on to the donated money until the\x01",
            "matron wakes up. If those guys want it, they'll\x01",
            "have to pry it from my cold, dead fingers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x12,
        (
            "You can count on me. I'll be\x01",
            "fine, so you go on ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x105,
        "#040FAll right...be careful.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #184
        0x101,
        "#000FLet's go, guys!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_8_30AE end

    SaveToFile()

Try(main)
