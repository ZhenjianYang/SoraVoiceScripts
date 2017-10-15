from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0110   ._SN',
        MapName             = 'event',
        Location            = 'E0110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60087",
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
        'Don',                                  # 10
        'Kyle',                                 # 11
        'Sky Bandit Lonnie',                    # 12
        'Comm. Officer Leon',                   # 13
        'Sky Bandit Aaron',                     # 14
        'Sky Bandit Ryan',                      # 15
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
        'ED6_DT27/CH03100 ._CH',             # 00
        'ED6_DT27/CH03760 ._CH',             # 01
        'ED6_DT27/CH03770 ._CH',             # 02
        'ED6_DT07/CH01380 ._CH',             # 03
        'ED6_DT27/CH03101 ._CH',             # 04
        'ED6_DT26/CH20416 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03100P._CP',             # 00
        'ED6_DT27/CH03760P._CP',             # 01
        'ED6_DT27/CH03770P._CP',             # 02
        'ED6_DT07/CH01380P._CP',             # 03
        'ED6_DT27/CH03101P._CP',             # 04
        'ED6_DT26/CH20416P._CP',             # 05
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = 51600,
        TriggerZ            = 0,
        TriggerY            = 74000,
        TriggerRange        = 1000,
        ActorX              = 51600,
        ActorZ              = 1000,
        ActorY              = 74000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_3AD",          # 01, 1
        "Function_2_482",          # 02, 2
        "Function_3_498",          # 03, 3
        "Function_4_FE8",          # 04, 4
        "Function_5_153F",         # 05, 5
        "Function_6_193B",         # 06, 6
        "Function_7_199A",         # 07, 7
        "Function_8_1DB2",         # 08, 8
        "Function_9_2384",         # 09, 9
        "Function_10_24DB",        # 0A, 10
        "Function_11_2772",        # 0B, 11
        "Function_12_299D",        # 0C, 12
        "Function_13_383B",        # 0D, 13
        "Function_14_3F43",        # 0E, 14
        "Function_15_3F7B",        # 0F, 15
        "Function_16_3FB3",        # 10, 16
        "Function_17_4039",        # 11, 17
        "Function_18_40CC",        # 12, 18
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB")
    OP_89(0x0, 49900, 500, 77980, 270)

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_255")
    SetChrPos(0xA, 45810, 0, 6940, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -21870, 650, 4940, 315)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_326")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_2C5")
    SetChrPos(0xA, 45810, 0, 6940, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -21870, 650, 4940, 315)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xC, -22620, 650, 5630, 135)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_326")

    label("loc_2C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2CF")
    Jump("loc_326")

    label("loc_2CF")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xB, 45590, 0, 6950, 0)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    SetChrPos(0xE, 47720, 0, 6300, 45)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)

    label("loc_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_340")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    Event(0, 11)
    Jump("loc_3AC")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_351")
    OP_A3(0x10F0)
    Event(0, 8)
    Jump("loc_3AC")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_368")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_3AC")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_37F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)
    Jump("loc_3AC")

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_390")
    OP_A3(0x10F3)
    Event(0, 12)
    Jump("loc_3AC")

    label("loc_390")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AC")
    Event(0, 7)

    label("loc_3AC")

    Return()

    # Function_0_1DE end

    def Function_1_3AD(): pass

    label("Function_1_3AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CB")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CB")

    OP_22(0x7A, 0x1, 0x3C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3EF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40B")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_402")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40B")

    label("loc_402")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_460")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_460")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_478")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    OP_10(0x6, 0x0)
    Jump("loc_481")

    label("loc_478")

    OP_10(0x0, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x6, 0x1)

    label("loc_481")

    Return()

    # Function_1_3AD end

    def Function_2_482(): pass

    label("Function_2_482")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_497")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_482")

    label("loc_497")

    Return()

    # Function_2_482 end

    def Function_3_498(): pass

    label("Function_3_498")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8ED")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 6)), scpexpr(EXPR_END)), "loc_671")

    ChrTalk(    #0
        0xA,
        (
            "#200FHey, you guys.\x02\x03",

            "That flight control problem's all fixed now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_537")

    ChrTalk(    #1
        0x10B,
        (
            "#210FReally?\x02\x03",

            "Sweet! Great job, Kyle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_558")

    label("loc_537")


    ChrTalk(    #2
        0x101,
        "#1000FReally? That's great!\x02",
    )

    CloseMessageWindow()

    label("loc_558")


    ChrTalk(    #3
        0xA,
        (
            "#200FDon't thank me--thank the professor.\x01",
            "He's the one who told us how to fix it.\x02\x03",

            "He's a hell of a guy, that's for sure.\x01",
            "Didn't even have to look at our ship to\x01",
            "tell us what the problem was.\x02\x03",

            "I can see why people call him one of the\x01",
            "greatest orbal engineers in the world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EA")

    label("loc_671")


    ChrTalk(    #4
        0xA,
        (
            "#200FHey, guys.\x02\x03",

            "That flight control problem's all fixed now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_707")

    ChrTalk(    #5
        0x10B,
        (
            "#210FNice job, Kyle.\x02\x03",

            "Even the pros have got nothing\x01",
            "on you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78D")

    label("loc_707")


    ChrTalk(    #6
        0x101,
        (
            "#1000FColor me impressed. You fixed\x01",
            "something like that on your own?\x02\x03",

            "I guess you don't call yourselves\x01",
            "sky bandits for nothing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78D")


    ChrTalk(    #7
        0xA,
        (
            "#200FAh, the credit's all Professor Russell's.\x01",
            "He's the one who pinpointed the issue.\x02\x03",

            "He didn't even have to look at it! We just told\x01",
            "him what was going on over the radio and he\x01",
            "figured out the problem right then and there.\x02\x03",

            "He's a hell of a guy, that's for sure.\x01",
            "They don't call him one of the greatest orbal\x01",
            "engineers in the world for show.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EA")

    Jump("loc_99C")

    label("loc_8ED")


    ChrTalk(    #8
        0xA,
        (
            "#200FRussell's got a mind like a steel trap.\x02\x03",

            "He doesn't even need to see the problem\x01",
            "to know what's going on. Just tell him what's\x01",
            "happening and he knows how to fix it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C")

    Jump("loc_FE4")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_FE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BD")
    Call(0, 13)
    OP_A2(0x5)
    Return()

    label("loc_9BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A38")

    ChrTalk(    #9
        0xA,
        (
            "#200FOne of the rail terminals requires a\x01",
            "password? That's kinda weird.\x02\x03",

            "Well, why not give my idea a shot?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE4")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")

    ChrTalk(    #10
        0xA,
        "#200FGotta be friggin' kidding me...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A99")

    ChrTalk(    #11
        0x10B,
        "#210FKyle, what's wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_ABA")

    label("loc_A99")


    ChrTalk(    #12
        0x101,
        "#1000FSome kind of trouble?\x02",
    )

    CloseMessageWindow()

    label("loc_ABA")


    ChrTalk(    #13
        0xA,
        (
            "#200FYeah, we're having trouble with the\x01",
            "flight controls.\x02\x03",

            "We could fly if we really needed to,\x01",
            "but it'll be a pain in the ass with no\x01",
            "way to stabilize our altitude.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B92")

    ChrTalk(    #14
        0x10B,
        "#210FWell, that sucks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BDF")

    label("loc_B92")


    ChrTalk(    #15
        0x101,
        (
            "#1000FI'm not sure what all that technobabble\x01",
            "means, but it sounds bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDF")


    ChrTalk(    #16
        0xA,
        (
            "#200FThe ship's instrumentation is completely\x01",
            "unsalvageable; never mind the hull.\x02\x03",

            "Might have to hit up the Arseille crew\x01",
            "and see what they think.\x02\x03",

            "Dunno how much we can accomplish\x01",
            "just talking over transmissions, but it's\x01",
            "not like we got much of a choice here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E25")

    ChrTalk(    #17
        0x101,
        "#1000FHmmm... Tita, could you do anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#060FA little, maybe, but this is the kinda\x01",
            "thing you need a specialist for.\x02\x03",

            "The flight engine's the most complicated\x01",
            "part of an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1000FAnd it's, uh, that messed up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1030FWell, like you said, you don't have\x01",
            "much of a choice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F26")

    label("loc_E25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8C")

    ChrTalk(    #21
        0x10B,
        (
            "#210FYeah, don't give up just yet.\x02\x03",

            "We've gotta take every advantage we\x01",
            "can get.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F26")

    label("loc_E8C")


    ChrTalk(    #22
        0x101,
        (
            "#1000FTalking to the Arseille's worth a shot.\x02\x03",

            "They've got Professor Russell over\x01",
            "there. He might be able to give you\x01",
            "a hint or something, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F26")


    ChrTalk(    #23
        0xA,
        (
            "#200FThat's the idea.\x02\x03",

            "We just have to be patient for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2296)
    Jump("loc_FE4")

    label("loc_F6C")


    ChrTalk(    #24
        0xA,
        (
            "#200FNot much we can do to fix the\x01",
            "flight controls.\x02\x03",

            "We just aren't set up to do repairs\x01",
            "on precision instruments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE4")

    TalkEnd(0xFE)
    Return()

    # Function_3_498 end

    def Function_4_FE8(): pass

    label("Function_4_FE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_12BE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")
    OP_A2(0x1)

    ChrTalk(    #25
        0xB,
        "Your Ladyship! Good work as liaison.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "We've fixed the flight engine, and it's\x01",
            "all thanks to the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "Looks like it was worth helping each\x01",
            "other out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1186")

    label("loc_10B4")


    ChrTalk(    #28
        0xB,
        (
            "We've fixed the flight engine, and it's all\x01",
            "thanks to the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "Good thing they were at least a little useful.\x01",
            "Would've sucked if we had to work together\x01",
            "and they just ended up being dead weight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1186")

    Jump("loc_12BB")

    label("loc_1189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1241")
    OP_A2(0x2)

    ChrTalk(    #30
        0xB,
        (
            "Sounds like we managed to repair\x01",
            "the flight controls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "Guess I'd better hurry with tuning\x01",
            "the instruments, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "Don'll be pissed if I waste too much\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BB")

    label("loc_1241")


    ChrTalk(    #33
        0xB,
        (
            "Sounds like we managed to repair\x01",
            "the flight controls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        (
            "Guess I'd better hurry with tuning\x01",
            "the instruments, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BB")

    Jump("loc_153B")

    label("loc_12BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_14F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1431")
    OP_A2(0x2)

    ChrTalk(    #35
        0xC,
        (
            "This is the Arseille.\x01",
            "Bobcat, please respond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xC,
        (
            "I repeat, this is the Arseille,\x01",
            "Bobcat, pl--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        "Ah, yes, this is the Bobcat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "We read you clearly, over.\x01",
            "Arseille, how's it look on your end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "Arseille to Bobcat, signal is crisp\x01",
            "and clear! Good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xC,
        "Do you need any supplies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "I repeat: Bobcat, are you in need\x01",
            "of supplies, or--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F5")

    label("loc_1431")


    ChrTalk(    #42
        0xB,
        (
            "Er, actually, Arseille, we've got a problem\x01",
            "with our flight control system that we're\x01",
            "unable to repair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "We'd like to request advice from your\x01",
            "ship's engineers. I repeat, we'd like to...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F5")

    Jump("loc_153B")

    label("loc_14F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1502")
    Jump("loc_153B")

    label("loc_1502")


    ChrTalk(    #44
        0xB,
        "Hey, get a move on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        "The boss is on the bridge.\x02",
    )

    CloseMessageWindow()

    label("loc_153B")

    TalkEnd(0xFE)
    Return()

    # Function_4_FE8 end

    def Function_5_153F(): pass

    label("Function_5_153F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_16D8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EF")
    OP_A2(0x3)

    ChrTalk(    #46
        0xD,
        "Your Ladyship, good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "The flight engine is fixed,\x01",
            "so we're good to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "We'll make the Bobcat good\x01",
            "as new. Just you wait!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165C")

    label("loc_15EF")


    ChrTalk(    #49
        0xD,
        (
            "The flight engine is fixed,\x01",
            "so we're good to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xD,
        (
            "We'll make the Bobcat good\x01",
            "as new. Just you wait!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165C")

    Jump("loc_16D5")

    label("loc_165F")


    ChrTalk(    #51
        0xFE,
        (
            "I'm really glad to hear the flight\x01",
            "engine's been fixed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "We should be able to get the\x01",
            "Bobcat in the air now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D5")

    Jump("loc_1937")

    label("loc_16D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_18C7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175C")
    OP_A2(0x3)

    ChrTalk(    #53
        0xD,
        "Your Ladyship!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xD,
        "You guys were amazing back there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        "Your Ladyship, you're our goddess!\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D3")

    label("loc_175C")


    ChrTalk(    #56
        0xD,
        "You guys were amazing back there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "We'll put our noses to it and get the\x01",
            "Bobcat fixed, you just wait and see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D3")

    Jump("loc_18C4")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1851")
    OP_A2(0x4)

    ChrTalk(    #58
        0xD,
        "Hey, thanks for your help back there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        "Those society guys are a weird bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        "Be careful, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18C4")

    label("loc_1851")


    ChrTalk(    #61
        0xD,
        "Those society guys are a weird bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "I mean, I guess we're ones to talk,\x01",
            "but we've got nothing on them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C4")

    Jump("loc_1937")

    label("loc_18C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_18D1")
    Jump("loc_1937")

    label("loc_18D1")


    ChrTalk(    #63
        0xFE,
        (
            "I'm amazed the boss even agreed\x01",
            "to this plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "This sounds bad no matter how\x01",
            "you look at it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1937")

    TalkEnd(0xFE)
    Return()

    # Function_5_153F end

    def Function_6_193B(): pass

    label("Function_6_193B")

    TalkBegin(0xFE)

    ChrTalk(    #65
        0xFE,
        "The Bobcat's in perfect condition.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "In other words, everything else is\x01",
            "on you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_193B end

    def Function_7_199A(): pass

    label("Function_7_199A")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xA, -18850, 3000, 5010, 270)
    SetChrPos(0x9, -22460, 650, 4800, 315)
    SetChrPos(0x8, -19890, 0, 3030, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x102, -15530, 500, 4940, 270)
    SetChrFlags(0x102, 0x80)
    OP_6D(-20530, 650, 5540, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(313000, 0)
    OP_6E(282, 0)
    Call(0, 14)
    OP_79(0x9, 0x1)
    OP_7B()
    FadeToBright(1000, 0)
    OP_0D()
    ClearChrFlags(0x102, 0x80)
    OP_9F(0x102, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_1A5F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A5F)
    OP_8E(0x102, 0xFFFFBB9A, 0x0, 0x12FC, 0x7D0, 0x0)
    OP_8C(0x9, 90, 400)
    Sleep(100)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #67
        0x9,
        "#190FAh, there you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "#215F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        "#1032FWhat's the situation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#490FHeh. Just what you predicted\x01",
            "it would be.\x02\x03",

            "Look at the display.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B31():
        OP_6D(-22030, 650, 5690, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B31)

    def lambda_1B49():
        OP_6C(322000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B49)

    def lambda_1B59():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B59)

    def lambda_1B67():

        label("loc_1B67")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1B67")

    QueueWorkItem2(0x8, 1, lambda_1B67)
    OP_8E(0x102, 0xFFFFAB3C, 0x28A, 0x14DC, 0x7D0, 0x0)
    OP_8C(0x102, 315, 400)
    Sleep(200)
    WaitChrThread(0x102, 0x2)
    OP_44(0x8, 0x1)
    OP_8C(0x102, 315, 400)

    ChrTalk(    #71
        0x9,
        (
            "#198F#6PAltitude of 1560 arge, entering Liberlian\x01",
            "territory from the north-northeast at\x01",
            "2100 selge per hour.\x02\x03",

            "With that kind of altitude and speed,\x01",
            "they aren't normal ships.\x02\x03",

            "#197FLooks like that special radar of yours\x01",
            "is working, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#1035F#7PDon't congratulate me yet.\x01",
            "We don't know who they are.\x02\x03",

            "#1031FIt's possible they're Erebonian\x01",
            "scout ships or something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 400)
    Sleep(300)

    ChrTalk(    #73
        0x102,
        "#1030F#3PKyle, do we have any visual contact yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "#201F...Got them!\x01",
            "Sending the image to your display!\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_199A end

    def Function_8_1DB2(): pass

    label("Function_8_1DB2")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xA, -18850, 3000, 5010, 280)
    SetChrPos(0x9, -22460, 650, 4800, 315)
    SetChrPos(0x8, -19890, 0, 3030, 315)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x102, -21700, 650, 5340, 315)
    OP_6D(-22030, 650, 5690, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(282, 0)
    Call(0, 14)
    OP_79(0x9, 0x1)
    OP_7B()
    OP_74(0x4, 0x5, 0x10)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #75
        0x102,
        (
            "#1032F#7P...Now there's no doubt.\x01",
            "That's our target.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "#200F#4PHeheh. Well, that's the stage set, then.\x02\x03",

            "Now it gets exciting.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)
    Sleep(500)

    ChrTalk(    #77
        0x9,
        (
            "#198F#3PLet's do this, then!\x02\x03",

            "#490FLad, you're ready for this, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #78
        0x102,
        (
            "#1031F#4PAbsolutely.\x02\x03",

            "Once I'm in place, begin immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    def lambda_1FA2():
        OP_8E(0xFE, 0xFFFFBB9A, 0x0, 0x12FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FA2)

    def lambda_1FBD():
        OP_6D(-21030, 500, 5850, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FBD)

    def lambda_1FD5():
        OP_6C(313000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1FD5)

    def lambda_1FE5():

        label("loc_1FE5")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1FE5")

    QueueWorkItem2(0x8, 3, lambda_1FE5)

    ChrTalk(    #79 op#A op#5
        0x8,
        "#216F#12AAh...\x05\x02",
    )

    Sleep(500)
    OP_8C(0xA, 90, 400)
    WaitChrThread(0x102, 0x1)
    OP_44(0x8, 0x3)
    OP_8C(0x8, 90, 400)
    OP_20(0x5DC)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x102)
    Sleep(500)
    OP_1D(0x50)
    Sleep(1500)

    ChrTalk(    #80
        0x102,
        (
            "#1035F#5PDon, Kyle...Josette...\x02\x03",

            "#1031FThank you for everything.\x02\x03",

            "Our relationship may have been based on\x01",
            "a contract, but I'm glad I met you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        "#213F#5PWh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        "#201F#3PWhat'n...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        "#192F#3PHuh?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #84
        0x102,
        (
            "#1031F#2PIt would be a bit more appropriate to say\x01",
            "it once the mission's over with.\x02\x03",

            "But...I may not get the opportunity.\x01",
            "So let me say it now. Thank you.\x02\x03",

            "#1053FBe well, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(500)

    def lambda_21F3():
        OP_6D(-20270, 500, 6030, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_21F3)

    def lambda_220B():
        OP_8E(0xFE, 0xFFFFBFBE, 0xFA, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_220B)
    WaitChrThread(0x102, 0x0)

    def lambda_222B():
        OP_8E(0xFE, 0xFFFFC374, 0x1F4, 0x1338, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_222B)

    def lambda_2246():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2246)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    SetChrFlags(0x102, 0x80)
    Sleep(1000)

    def lambda_2271():
        OP_6D(-22030, 650, 5690, 1800)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2271)
    WaitChrThread(0x102, 0x2)
    Sleep(500)

    ChrTalk(    #85
        0xA,
        "#207F#3PHe just...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        "#197F#3PHeh. Dramatic till the very end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        "#212F#5PGrr...!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 4)

    def lambda_22F3():
        OP_6D(-20270, 500, 6030, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_22F3)
    OP_8E(0x8, 0xFFFFB654, 0x0, 0xB72, 0x1388, 0x0)
    OP_8E(0x8, 0xFFFFB9C4, 0x0, 0x10D6, 0x1388, 0x0)
    OP_8E(0x8, 0xFFFFBFBE, 0xFA, 0x1324, 0x1388, 0x0)

    def lambda_2347():
        OP_8E(0xFE, 0xFFFFC374, 0x1F4, 0x1338, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2347)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x8, 0x80)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1DB2 end

    def Function_9_2384(): pass

    label("Function_9_2384")

    EventBegin(0x0)
    OP_A3(0x10F1)
    OP_24(0x7A, 0x64)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -24400, -1000, 4970, 270)
    SetChrPos(0x9, -22260, 650, 5230, 308)
    SetChrPos(0x8, -18850, 3000, 5010, 280)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_6D(-22890, 0, 6950, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(267, 0)
    Call(0, 14)
    OP_79(0x9, 0x1)
    OP_7B()
    OP_76(0xC, 0x0, 0x1, 0xFFFFFFEC, 0xFFFFFFFC, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #88
        0x8,
        "#415F#7PAlllll RIGHT! It worked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        "#191F#6PO-ho! So it did!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        "#201F#2PTime for us to beat it, then!\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2384 end

    def Function_10_24DB(): pass

    label("Function_10_24DB")

    EventBegin(0x0)
    OP_A3(0x10F2)
    OP_24(0x7A, 0x50)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -24400, -1000, 4970, 270)
    SetChrPos(0x9, -22260, 650, 5230, 308)
    SetChrPos(0x8, -18850, 3000, 5010, 280)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_6D(-22890, 0, 6950, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(267, 0)
    Call(0, 14)
    OP_76(0xC, 0x0, 0x1, 0xFFFFFFF6, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #91
        0x9,
        (
            "#490F#6PHah! They're pulling out as well!\x02\x03",

            "Everything went exactly like he\x01",
            "thought it would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#215F#7P...Yeah.\x02\x03",

            "#413F...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xA, 2)
    Sleep(300)

    ChrTalk(    #93
        0xA,
        (
            "#204F#1PJosette, don't worry.\x02\x03",

            "#200FIt's Joshua Astray we're talking about.\x01",
            "He'll come back safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#215F#7PYeah... Yeah, he will.\x02\x03",

            "#210FHe's got a promise to keep, after all.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_20(0xFA0)
    Sleep(300)
    OP_24(0x7A, 0x46)
    Sleep(300)
    OP_24(0x7A, 0x3C)
    Sleep(300)
    OP_24(0x7A, 0x32)
    Sleep(300)
    OP_24(0x7A, 0x28)
    Sleep(300)
    OP_24(0x7A, 0x1E)
    Sleep(300)
    OP_24(0x7A, 0x14)
    Sleep(300)
    OP_24(0x7A, 0xA)
    Sleep(300)
    OP_23(0x7A)
    OP_0D()
    OP_21()
    OP_AD(0x2400A9, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_24DB end

    def Function_11_2772(): pass

    label("Function_11_2772")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0xA, -24300, -1000, 4970, 270)
    SetChrPos(0x9, -21860, 650, 4770, 270)
    SetChrPos(0x8, -18850, 3000, 5010, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_6D(-24130, 0, 7440, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(322000, 0)
    OP_6E(280, 0)
    SetChrFlags(0xB, 0x80)
    OP_44(0xA, 0xFF)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    Call(0, 15)
    OP_22(0x7A, 0x1, 0x50)
    OP_76(0xB, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFFC, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_6B(3100, 2000)
    OP_0D()

    ChrTalk(    #95
        0x8,
        (
            "#418F#4PKyle, PLEASE!\x02\x03",

            "If we just leave them, Joshua'll...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "#204F#5PNo, Josette.\x02\x03",

            "#207FWe...wouldn't make it in time,\x01",
            "either way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        "#417F#4PNo... No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#198F#2PDamn it all...\x01",
            "At the very end, too!\x02\x03",

            "#196FWhat is the Goddess doing at\x01",
            "a time like this?!\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2772 end

    def Function_12_299D(): pass

    label("Function_12_299D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xA, -24300, -1000, 4970, 270)
    SetChrPos(0x9, -21860, 650, 4770, 315)
    SetChrPos(0x8, -18850, 3000, 5010, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_6D(-24130, 0, 8000, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(322000, 0)
    OP_6E(322, 0)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    Call(0, 15)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS227._CH")
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS180._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    OP_22(0x7C, 0x0, 0x64)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS181._CH")
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, -1, 0, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1000)
    Sleep(1000)
    SetMessageWindowPos(400, 340, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #99
        "\x07\x00Goddess...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    FadeToBright(1000, 0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8F(0x8, 0xFFFFB816, 0xBB8, 0x127A, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #100
        0x8,
        (
            "#216F#4PWhat IS that thing?!\x02\x03",

            "It's huge... RIDICULOUSLY HUGE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "#192F#5PThat thing must be more than\x01",
            "five thousand arge across.\x02\x03",

            "It's like a giant floating island...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "#204F#5PNo, look closely.\x01",
            "The base is artificial.\x02\x03",

            "#206FIt's more a floating city\x01",
            "than an island...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        "#213F#4PA c-city...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        "#198F#5PWell, we can't just sit here...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x4)
    OP_8C(0x9, 270, 400)
    OP_8E(0x9, 0xFFFFA876, 0x28A, 0x1248, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #105
        0x9,
        "#196F#2P#3SAll right, guys! Listen up!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #106
        0x9,
        (
            "#196F#2P#3SWe are getting onto that\x01",
            "flying city-island!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xA, 2)

    ChrTalk(    #107
        0xA,
        "#201F#5PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        "#213F#4PSeriously?!\x02",
    )

    CloseMessageWindow()
    OP_8F(0x9, 0xFFFFAA9C, 0x28A, 0x12A2, 0x7D0, 0x0)
    OP_8C(0x9, 135, 400)
    Sleep(500)

    ChrTalk(    #109
        0x9,
        (
            "#490F#5POf course I'm serious!\x01",
            "I've never been more serious!\x02\x03",

            "#198FIf those society fools have brought\x01",
            "that thing back, then think!\x02\x03",

            "#191FIt must be full of incredible treasure!\x01",
            "Enough to pay our debts ten times over!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "#203F#5PY-You've got to be kidding me...\x02\x03",

            "#201FWe can't just go waltzing\x01",
            "into something that huge!\x02\x03",

            "Josette, back me up, here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#413F#4PUmmm... Hmm...\x02\x03",

            "#215FHonestly, at this point...I bet there\x01",
            "are things on that city I want, too.\x01",
            "Like, beyond treasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        "#203F#5POh, Aidios, save me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "#415F#4PK-Kyle does have a point, though!\x01",
            "Things have been weird all day,\x01",
            "so we should probably be careful.\x02\x03",

            "I mean, for starters, the radio's\x01",
            "been silent for ages!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "#197F#5PThat IS true. Guild and army transmissions\x01",
            "are one thing, but even the civilian\x01",
            "channels are dead. Which is--\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_20(0x7D0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(-24130, 0, 8000, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(322000, 0)
    OP_6E(322, 0)
    OP_0D()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xA, 0)
    OP_8C(0x9, 270, 500)

    ChrTalk(    #115
        0x9,
        "#192F#5PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        "#201F#5PWh--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        "#213F#4PA wave of light?\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_82(0x80, 0x0)
    OP_0D()
    Fade(500)
    OP_22(0xE1, 0x0, 0x64)
    OP_23(0x7A)
    OP_71(0x5, 0x4)
    Sleep(100)
    OP_71(0x6, 0x4)
    Sleep(100)
    OP_71(0x7, 0x4)
    Sleep(100)
    OP_71(0x8, 0x4)
    Sleep(100)
    OP_71(0x9, 0x4)
    OP_74(0x4, 0x5, 0x0)
    OP_0D()
    Sleep(500)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x8,
        "#216F#4PGyah!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x51)
    Sleep(500)
    OP_8C(0x9, 315, 400)

    ChrTalk(    #119
        0x9,
        "#192F#5PWhat happened?! Report!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, -14000, 500, 4660, 270)
    OP_4A(0xB, 255)

    ChrTalk(    #120
        0xB,
        "#1PBOSS! BIG PROBLEM!\x02",
    )

    CloseMessageWindow()

    def lambda_3425():
        OP_6D(-22710, 0, 7190, 1500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3425)

    def lambda_343D():
        OP_67(0, 4640, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_343D)

    def lambda_3455():
        OP_6B(2920, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3455)
    ClearChrFlags(0xB, 0x80)

    def lambda_346A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_346A)

    def lambda_347C():
        OP_8E(0xB, 0xFFFFC374, 0x1F4, 0x1306, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_347C)
    WaitChrThread(0xB, 0x1)
    ClearChrFlags(0xB, 0x4)

    def lambda_34A1():
        OP_8E(0xB, 0xFFFFBB9A, 0x0, 0x12FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_34A1)

    def lambda_34BC():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_34BC)
    Sleep(50)

    def lambda_34CF():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34CF)
    Sleep(50)
    WaitChrThread(0xB, 0x1)
    Sleep(500)
    WaitChrThread(0x9, 0x0)

    ChrTalk(    #121
        0xB,
        (
            "#2PThe generators and flight engines\x01",
            "have cut out! ALL OF THEM!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #122
        0x9,
        "#196F#6PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        "#216F#6PW-W-Wait, that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xA,
        (
            "#206F#5PWe're really in trouble now.\x02\x03",

            "The flight field from the\x01",
            "engines is dissipating.\x02\x03",

            "The Bobcat's not answering\x01",
            "her helm at all, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_3647():
        OP_6D(-24130, 0, 7440, 1200)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3647)

    def lambda_365F():
        OP_67(0, 5440, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_365F)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0xA, 400)
    TurnDirection(0x8, 0xA, 400)
    WaitChrThread(0x9, 0x0)

    ChrTalk(    #125
        0x9,
        "#196F#5PYou're kidding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        "#214F#4PYou mean we can't do anything?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "#204F#5P...\x02\x03",

            "#207FThere's only one thing\x01",
            "we can do at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        "#192F#1PWhat?!\x02",
    )


    ChrTalk(    #129
        0x8,
        "#213F#4PWhat?!\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(100)
    SetChrSubChip(0xA, 2)
    Sleep(300)

    ChrTalk(    #130
        0xA,
        (
            "#203F#5PPray to Aidios that it's not our\x01",
            "time to be called to Heaven...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x7D0)
    OP_22(0xEC, 0x0, 0x64)
    OP_D0(5000, 0)
    Sleep(1000)
    OP_22(0x13B, 0x0, 0x64)

    def lambda_37F2():
        OP_6D(-18330, 15000, 5500, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_37F2)

    def lambda_380A():
        OP_D0(25000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_380A)
    Sleep(1000)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_299D end

    def Function_13_383B(): pass

    label("Function_13_383B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3860")
    Call(0, 16)
    Call(0, 17)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_3860")

    Fade(500)
    OP_6D(45440, 0, 6250, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 45620, 0, 5160, 0)
    SetChrPos(0x102, 46440, 0, 5370, 0)
    SetChrPos(0xF8, 44470, 0, 5520, 45)
    SetChrPos(0xF9, 47260, 0, 5750, 315)
    OP_8C(0xA, 180, 0)
    OP_4A(0xA, 0)
    OP_0D()

    ChrTalk(    #131
        0xA,
        (
            "#200FOh, yeah. In all the commotion,\x01",
            "I almost forgot.\x02\x03",

            "Does the word 'Orpheus' mean anything\x01",
            "to you guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1000FWhat? Uh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39A5")

    ChrTalk(    #133
        0x10B,
        "#210FWait, Orpheus...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A5D")

    label("loc_39A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39C9")

    ChrTalk(    #134
        0x105,
        "#040FOrpheus?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A5D")

    label("loc_39C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39F0")

    ChrTalk(    #135
        0x104,
        "#030FOrpheus...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A5D")

    label("loc_39F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A18")

    ChrTalk(    #136
        0x109,
        "#1060FOrpheus...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A5D")

    label("loc_3A18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A3C")

    ChrTalk(    #137
        0x107,
        "#060FOrpheus?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A5D")

    label("loc_3A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A5D")

    ChrTalk(    #138
        0x106,
        "#050FOrpheus?\x02",
    )

    CloseMessageWindow()

    label("loc_3A5D")


    ChrTalk(    #139
        0x102,
        "#1030FWhy do you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xA,
        (
            "#200FIt came up a few times in the conversations\x01",
            "the guards had.\x02\x03",

            "Seemed kind of meaningful, so it stuck out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B58")

    ChrTalk(    #141
        0x10B,
        "#210FOh, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1000FHmmm... That is kinda curious.\x02\x03",

            "(Wait... Maybe it's the...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B9F")

    label("loc_3B58")


    ChrTalk(    #143
        0x101,
        (
            "#1000FHmmm... That is kinda curious.\x02\x03",

            "(Wait... Maybe it's the...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B9F")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Name of the Factory District\x01",      # 0
            "Proper Name for the Gospels\x01",       # 1
            "Password for that Terminal\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C3C"),
        (1, "loc_3CD8"),
        (2, "loc_3D6C"),
        (SWITCH_DEFAULT, "loc_3DD1"),
    )


    label("loc_3C3C")


    ChrTalk(    #144
        0x102,
        (
            "#1030FNo, the district's name is 'Factoria,'\x01",
            "I believe.\x02\x03",

            "Relatedly, though... I think it may be\x01",
            "the password to that terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1000FOh, that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DD1")

    label("loc_3CD8")


    ChrTalk(    #146
        0x102,
        (
            "#1030FNo, the Gospels seem to have\x01",
            "been called just that, even here.\x02\x03",

            "I think it may be the password\x01",
            "to that terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1000FOh, that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DD1")

    label("loc_3D6C")


    ChrTalk(    #148
        0x102,
        (
            "#1030FYes. The train terminal in the\x01",
            "factory district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#1000FYou think so, too, Joshua?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DD1")

    label("loc_3DD1")


    ChrTalk(    #150
        0xA,
        "#200FI think I'm missing something here.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #151
        (
            "\x07\x05Estelle explained about the password lock on the substratum\x01",
            "gate at one of the train stations.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #152
        0xA,
        (
            "#200FAh, I see. Yeah, that does seem\x01",
            "a little too coincidental.\x02\x03",

            "Worth a shot, at least, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1000FI think so!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F16")

    ChrTalk(    #154
        0x10B,
        "#210FThanks, Kyle!\x02",
    )

    CloseMessageWindow()

    label("loc_3F16")


    ChrTalk(    #155
        0x102,
        "#1030FLet's go try it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)
    OP_4B(0xA, 0)
    OP_A2(0x222D)
    EventEnd(0x0)
    Return()

    # Function_13_383B end

    def Function_14_3F43(): pass

    label("Function_14_3F43")

    OP_71(0x2, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0xB, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)
    Return()

    # Function_14_3F43 end

    def Function_15_3F7B(): pass

    label("Function_15_3F7B")

    OP_71(0x2, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x9, 0x4)
    Return()

    # Function_15_3F7B end

    def Function_16_3FB3(): pass

    label("Function_16_3FB3")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_402C"),
        (1, "loc_4032"),
        (SWITCH_DEFAULT, "loc_4038"),
    )


    label("loc_402C")

    OP_A2(0x1200)
    Jump("loc_4038")

    label("loc_4032")

    OP_A2(0x1201)
    Jump("loc_4038")

    label("loc_4038")

    Return()

    # Function_16_3FB3 end

    def Function_17_4039(): pass

    label("Function_17_4039")

    FadeToDark(0, 0, -1)
    OP_6D(-182260, 0, -191970, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_17_4039 end

    def Function_18_40CC(): pass

    label("Function_18_40CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4132")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #156
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_42ED")

    label("loc_4132")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #157
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D2")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x32)
    OP_73(0xA)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_42D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42EC")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_42EC")

    Return()

    label("loc_42ED")

    Return()

    # Function_18_40CC end

    SaveToFile()

Try(main)
