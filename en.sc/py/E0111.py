from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0111   ._SN',
        MapName             = 'Event',
        Location            = 'E0111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        'ED6_DT07/CH02110 ._CH',             # 01
        'ED6_DT07/CH02120 ._CH',             # 02
        'ED6_DT07/CH01380 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03100P._CP',             # 00
        'ED6_DT07/CH02110P._CP',             # 01
        'ED6_DT07/CH02120P._CP',             # 02
        'ED6_DT07/CH01380P._CP',             # 03
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
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AE",          # 00, 0
        "Function_1_2B6",          # 01, 1
        "Function_2_370",          # 02, 2
        "Function_3_386",          # 03, 3
        "Function_4_F12",          # 04, 4
        "Function_5_146B",         # 05, 5
        "Function_6_1814",         # 06, 6
        "Function_7_1B0C",         # 07, 7
        "Function_8_2319",         # 08, 8
        "Function_9_239F",         # 09, 9
        "Function_10_2432",        # 0A, 10
    )


    def Function_0_1AE(): pass

    label("Function_0_1AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD")
    OP_89(0x0, 49900, 500, 77980, 270)
    OP_30(0x1)

    label("loc_1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_227")
    SetChrPos(0xA, 45810, 0, 6940, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -21870, 650, 4940, 315)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xD, 46020, 0, 77750, 0)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_294")

    label("loc_227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_294")
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

    label("loc_294")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B5")
    Event(0, 6)

    label("loc_2B5")

    Return()

    # Function_0_1AE end

    def Function_1_2B6(): pass

    label("Function_1_2B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D4")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_33A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_364")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    OP_D0(5000, 0)
    OP_51(0xA, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36F")

    label("loc_364")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)
    OP_71(0x1, 0x4)

    label("loc_36F")

    Return()

    # Function_1_2B6 end

    def Function_2_370(): pass

    label("Function_2_370")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_370")

    label("loc_385")

    Return()

    # Function_2_370 end

    def Function_3_386(): pass

    label("Function_3_386")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_8AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FB")
    OP_A2(0x22CA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 6)), scpexpr(EXPR_END)), "loc_571")

    ChrTalk(    #0
        0xA,
        (
            "#200FHey, you guys.\x02\x03",

            "That flight control problem's all fixed now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_431")

    ChrTalk(    #1
        0x10B,
        (
            "#213FReally?\x02\x03",

            "#211FSweet! Great job, Kyle.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10B, 400)
    Jump("loc_459")

    label("loc_431")


    ChrTalk(    #2
        0x101,
        "#1011FReally? That's great!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    label("loc_459")


    ChrTalk(    #3
        0xA,
        (
            "#200FDon't thank me--thank the professor.\x01",
            "He's the one who told us how to fix it.\x02\x03",

            "He's a hell of a guy, that's for sure.\x01",
            "Didn't even have to look at our ship to\x01",
            "tell us what the problem was.\x02\x03",

            "They don't call him one of the greatest\x01",
            "orbal engineers in the world for show.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F8")

    label("loc_571")


    ChrTalk(    #4
        0xA,
        (
            "#200FHey, guys.\x02\x03",

            "That flight control problem's all fixed now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60E")

    ChrTalk(    #5
        0x10B,
        (
            "#211FNice job, Kyle.\x02\x03",

            "Even the pros have got nothing\x01",
            "on you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10B, 400)
    Jump("loc_69B")

    label("loc_60E")


    ChrTalk(    #6
        0x101,
        (
            "#1011FColor me impressed. You fixed\x01",
            "something like that on your own?\x02\x03",

            "I guess you don't call yourselves\x01",
            "sky bandits for nothing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    label("loc_69B")


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

    label("loc_7F8")

    Jump("loc_8AA")

    label("loc_7FB")


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

    label("loc_8AA")

    Jump("loc_F0E")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CB")
    Call(0, 7)
    OP_A2(0x5)
    Return()

    label("loc_8CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_946")

    ChrTalk(    #9
        0xA,
        (
            "#200FOne of the rail terminals requires a\x01",
            "password? That's kinda weird.\x02\x03",

            "Well, why not give my idea a shot?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0E")

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E96")

    ChrTalk(    #10
        0xA,
        "#203FGotta be friggin' kidding me...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AE")

    ChrTalk(    #11
        0x10B,
        "#213FKyle, what's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10B, 400)
    Jump("loc_9D6")

    label("loc_9AE")


    ChrTalk(    #12
        0x101,
        "#1002FSome kind of trouble?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    label("loc_9D6")


    ChrTalk(    #13
        0xA,
        (
            "#207FYeah, we're having trouble with the\x01",
            "flight controls.\x02\x03",

            "We could fly if we really needed to,\x01",
            "but it'll be a pain in the ass with no\x01",
            "way to stabilize our altitude.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AAE")

    ChrTalk(    #14
        0x10B,
        "#215FWell, that sucks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFB")

    label("loc_AAE")


    ChrTalk(    #15
        0x101,
        (
            "#1019FI'm not sure what all that technobabble\x01",
            "means, but it sounds bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFB")


    ChrTalk(    #16
        0xA,
        (
            "#206FThe ship's instrumentation is completely\x01",
            "unsalvageable; never mind the hull.\x02\x03",

            "Might have to hit up the Arseille crew\x01",
            "and see what they think.\x02\x03",

            "Dunno how much we can accomplish\x01",
            "just talking over transmissions, but it's\x01",
            "not like we got much of a choice here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D4F")

    ChrTalk(    #17
        0x101,
        "#1015FHmmm... Tita, could you do anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#561FA little, maybe, but this is the kinda\x01",
            "thing you need a specialist for.\x02\x03",

            "The flight engine's the most complicated\x01",
            "part of an airship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #19
        0x101,
        "#1004FAnd it's, uh, that messed up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1043FWell, like you said, you don't have\x01",
            "much of a choice.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)
    Jump("loc_E50")

    label("loc_D4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB6")

    ChrTalk(    #21
        0x10B,
        (
            "#210FYeah, don't give up just yet.\x02\x03",

            "We've gotta take every advantage we\x01",
            "can get.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E50")

    label("loc_DB6")


    ChrTalk(    #22
        0x101,
        (
            "#1011FTalking to the Arseille's worth a shot.\x02\x03",

            "They've got Professor Russell over\x01",
            "there. He might be able to give you\x01",
            "a hint or something, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E50")


    ChrTalk(    #23
        0xA,
        (
            "#200FThat's the idea.\x02\x03",

            "We just have to be patient for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2296)
    Jump("loc_F0E")

    label("loc_E96")


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

    label("loc_F0E")

    TalkEnd(0xFE)
    Return()

    # Function_3_386 end

    def Function_4_F12(): pass

    label("Function_4_F12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_11EA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")
    OP_A2(0x1)

    ChrTalk(    #25
        0xB,
        "Your ladyship! Good work as liaison.\x02",
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
    Jump("loc_10B2")

    label("loc_FE0")


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

    label("loc_10B2")

    Jump("loc_11E7")

    label("loc_10B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116D")
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
    Jump("loc_11E7")

    label("loc_116D")


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

    label("loc_11E7")

    Jump("loc_1467")

    label("loc_11EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1399")
    OP_A2(0x2)

    ChrTalk(    #35
        0xC,
        (
            "\x07\x05#2P#1SThis is the Arseille.\x01",
            "Bobcat, please respond.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xC,
        (
            "\x07\x05#2P#1SI repeat, this is the Arseille,\x01",
            "Bobcat, pl--\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        "\x07\x00#1PAh, yes, this is the Bobcat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "\x07\x00#1PWe read you clearly, over.\x01",
            "Arseille, how's it look on your end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "\x07\x05#2P#1SArseille to Bobcat, signal is crisp\x01",
            "and clear! Good!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xC,
        "\x07\x05#2P#1SDo you need any supplies?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "\x07\x05#2P#1SI repeat: Bobcat, are you in need\x01",
            "of supplies, or--\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1467")

    label("loc_1399")


    ChrTalk(    #42
        0xB,
        (
            "\x07\x00#1PEr, actually, Arseille, we've got a problem\x01",
            "with our flight control system that we're\x01",
            "unable to repair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "\x07\x00#1PWe'd like to request advice from your\x01",
            "ship's engineers. I repeat, we'd like to...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1467")

    TalkEnd(0xFE)
    Return()

    # Function_4_F12 end

    def Function_5_146B(): pass

    label("Function_5_146B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1614")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_159B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1524")
    OP_A2(0x3)
    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #44
        0xD,
        "Your ladyship, good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "The flight engine is fixed,\x01",
            "so we're good to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        (
            "We'll make the Bobcat good\x01",
            "as new. Just you wait!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1598")

    label("loc_1524")

    TurnDirection(0xD, 0x10B, 0)

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

    label("loc_1598")

    Jump("loc_1611")

    label("loc_159B")


    ChrTalk(    #49
        0xFE,
        (
            "I'm really glad to hear the flight\x01",
            "engine's been fixed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "We should be able to get the\x01",
            "Bobcat in the air now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1611")

    Jump("loc_1810")

    label("loc_1614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1810")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A1")
    TurnDirection(0xD, 0x10B, 0)
    OP_A2(0x3)

    ChrTalk(    #51
        0xD,
        "Your ladyship!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        "You guys were amazing back there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xD,
        "Your ladyship, you're our goddess!\x02",
    )

    CloseMessageWindow()
    Jump("loc_171F")

    label("loc_16A1")

    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #54
        0xD,
        "You guys were amazing back there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "We'll put our noses to it and get the\x01",
            "Bobcat fixed, you just wait and see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171F")

    Jump("loc_1810")

    label("loc_1722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179D")
    OP_A2(0x4)

    ChrTalk(    #56
        0xD,
        "Hey, thanks for your help back there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        "Those society guys are a weird bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        "Be careful, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1810")

    label("loc_179D")


    ChrTalk(    #59
        0xD,
        "Those society guys are a weird bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "I mean, I guess we're ones to talk,\x01",
            "but we've got nothing on them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1810")

    TalkEnd(0xFE)
    Return()

    # Function_5_146B end

    def Function_6_1814(): pass

    label("Function_6_1814")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x12A, -25710, -500, 6350, 158)
    SetChrPos(0x129, -26570, -500, 5830, 143)
    SetChrPos(0x146, -26910, -500, 4600, 90)
    SetChrPos(0x102, -25290, -500, 3650, 0)
    OP_6D(-25995, -500, 5000, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #61
        0x12A,
        (
            "#203F#4PNo good. We won't be able to\x01",
            "start it up without the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x129,
        "#197FDamn it. We're so close, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1033F#6PUnfortunately, it would take too long to\x01",
            "try and hot-wire the controls.\x02\x03",

            "#1030FI think it would be faster to simply\x01",
            "find the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x146,
        (
            "#214F#6PSo we need to find that guard\x01",
            "captain guy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1031F#6PThat would be my suggestion.\x02\x03",

            "He should have an office somewhere in this\x01",
            "facility. Let's check there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -23370, 0, 3020, 90)
    SetChrPos(0x1, -23370, 0, 3020, 90)
    SetChrPos(0x2, -23370, 0, 3020, 90)
    SetChrPos(0x3, -23370, 0, 3020, 90)
    OP_6D(-23370, 0, 3020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    Sleep(500)
    OP_A2(0x1805)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_6_1814 end

    def Function_7_1B0C(): pass

    label("Function_7_1B0C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B31")
    Call(0, 8)
    Call(0, 9)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_1B31")

    Fade(500)
    OP_6D(44790, 100, 7060, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 45590, 0, 5520, 0)
    SetChrPos(0x102, 46620, 0, 5450, 0)
    SetChrPos(0xF8, 45580, 0, 4260, 0)
    SetChrPos(0xF9, 47010, 0, 4130, 0)
    OP_8C(0xA, 180, 0)
    OP_4A(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0xA,
        (
            "#200F#4POh, yeah. In all the commotion,\x01",
            "I almost forgot.\x02\x03",

            "Does the word 'Orpheus' mean anything\x01",
            "to you guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1004F#5PWhat? Uh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C84")

    ChrTalk(    #68
        0x10B,
        "#213F#5PWait, Orpheus...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D46")

    label("loc_1C84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAC")

    ChrTalk(    #69
        0x105,
        "#1164F#5POrpheus?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D46")

    label("loc_1CAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD3")

    ChrTalk(    #70
        0x104,
        "#030F#5POrpheus?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D46")

    label("loc_1CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFB")

    ChrTalk(    #71
        0x109,
        "#1060F#5POrpheus?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D46")

    label("loc_1CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D22")

    ChrTalk(    #72
        0x107,
        "#064F#5POrpheus?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D46")

    label("loc_1D22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D46")

    ChrTalk(    #73
        0x106,
        "#555F#5POrpheus.\x02",
    )

    CloseMessageWindow()

    label("loc_1D46")


    ChrTalk(    #74
        0x102,
        "#1044F#5PWhy do you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#206F#4PIt came up a few times in the conversations\x01",
            "the guards had.\x02\x03",

            "Seemed kind of meaningful, so it stuck out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E53")

    ChrTalk(    #76
        0x10B,
        "#210F#5POh, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1015F#5PHmmm... That is kinda curious.\x02\x03",

            "#1004F(Wait... Maybe it's the...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EA3")

    label("loc_1E53")


    ChrTalk(    #78
        0x101,
        (
            "#1015F#5PHmmm... That is kinda curious.\x02\x03",

            "#1004F(Wait... Maybe it's the...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA3")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #79
        "\x18\x07\x05What could the mystery word be?\x02",
    )


    Menu(
        0,
        -1,
        150,
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
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F85"),
        (1, "loc_2040"),
        (2, "loc_20F3"),
        (SWITCH_DEFAULT, "loc_2171"),
    )


    label("loc_1F85")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #80
        0x102,
        (
            "#1035F#2PNo, the district's name is 'Factoria,'\x01",
            "I believe.\x02\x03",

            "#1040FRelatedly, though... I think it may be\x01",
            "the password to that terminal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #81
        0x101,
        "#1018F#5POh, that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2171")

    label("loc_2040")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #82
        0x102,
        (
            "#1035F#2PNo, the Gospels seem to have\x01",
            "been called just that, even here.\x02\x03",

            "#1040FI think it may be the password\x01",
            "to that terminal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #83
        0x101,
        "#1018F#5POh, that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2171")

    label("loc_20F3")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #84
        0x102,
        (
            "#1040F#2PYes. The train terminal in the\x01",
            "factory district.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #85
        0x101,
        "#1018F#5PYou think so, too, Joshua?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2171")

    label("loc_2171")


    ChrTalk(    #86
        0xA,
        "#206F#4PI think I'm missing something here.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)
    OP_8C(0x101, 0, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #87
        (
            "\x07\x05Estelle explained about the password lock on the substratum\x01",
            "gate at one of the train stations.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #88
        0xA,
        (
            "#200F#4PAh, I see. Yeah, that does seem\x01",
            "a little too coincidental.\x02\x03",

            "Worth a shot, at least, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1006F#5PI think so!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22E3")

    ChrTalk(    #90
        0x10B,
        "#211F#5PThanks, Kyle!\x02",
    )

    CloseMessageWindow()

    label("loc_22E3")


    ChrTalk(    #91
        0x102,
        "#1040F#5PLet's go try it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)
    OP_4B(0xA, 0)
    OP_A2(0x222D)
    OP_28(0x9E, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_7_1B0C end

    def Function_8_2319(): pass

    label("Function_8_2319")

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
        (0, "loc_2392"),
        (1, "loc_2398"),
        (SWITCH_DEFAULT, "loc_239E"),
    )


    label("loc_2392")

    OP_A2(0x1200)
    Jump("loc_239E")

    label("loc_2398")

    OP_A2(0x1201)
    Jump("loc_239E")

    label("loc_239E")

    Return()

    # Function_8_2319 end

    def Function_9_239F(): pass

    label("Function_9_239F")

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

    # Function_9_239F end

    def Function_10_2432(): pass

    label("Function_10_2432")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2498")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #92
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_2653")

    label("loc_2498")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #93
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2638")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 51600, 1000, 74000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x32)
    OP_73(0x0)
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
    OP_6F(0x0, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2638")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2652")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2652")

    Return()

    label("loc_2653")

    Return()

    # Function_10_2432 end

    SaveToFile()

Try(main)
