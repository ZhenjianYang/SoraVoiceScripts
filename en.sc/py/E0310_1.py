from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0310_1 ._SN',
        MapName             = 'Event',
        Location            = 'E0310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0310   ._SN',
            'ED6_DT21/E0310_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_1828",         # 02, 2
        "Function_3_35E6",         # 03, 3
        "Function_4_4DEA",         # 04, 4
        "Function_5_5DFC",         # 05, 5
        "Function_6_684C",         # 06, 6
        "Function_7_69A0",         # 07, 7
        "Function_8_69C0",         # 08, 8
        "Function_9_7460",         # 09, 9
        "Function_10_799A",        # 0A, 10
        "Function_11_7B85",        # 0B, 11
        "Function_12_8477",        # 0C, 12
        "Function_13_988F",        # 0D, 13
        "Function_14_ACCD",        # 0E, 14
        "Function_15_B193",        # 0F, 15
        "Function_16_B1CD",        # 10, 16
        "Function_17_C0F3",        # 11, 17
        "Function_18_C9FC",        # 12, 18
        "Function_19_CA56",        # 13, 19
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1BB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124")

    ChrTalk(    #0
        0xFE,
        (
            "Starboard flight engine...\x01",
            "Circuits connecting fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Running simulation at 50% output.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1B5")

    label("loc_124")


    ChrTalk(    #2
        0xFE,
        (
            "We're stress testing our circuits between\x01",
            "50% and 70% output.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "If we see a problem with the outrigger,\x01",
            "we'll stop the test immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5")

    TalkEnd(0xFE)
    Jump("loc_1827")

    label("loc_1BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1C5")
    Jump("loc_1827")

    label("loc_1C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_1CF")
    Jump("loc_1827")

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_5AC")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4")

    ChrTalk(    #4
        0xFE,
        (
            "Your Highness!\x01",
            "Thanks for all your hard work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "We've just checked all ship functionality...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "...and it's just as Professor Russell said.\x01",
            "The damage is lighter than we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "We should be able to get the Arseille\x01",
            "flying again on our own.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_389")

    label("loc_2F4")


    ChrTalk(    #8
        0xFE,
        (
            "It's just as Professor Russell said.\x01",
            "The damage is lighter than we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "We should be able to get the Arseille\x01",
            "flying again on our own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389")

    Jump("loc_5A6")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE")

    ChrTalk(    #10
        0xFE,
        (
            "We've completed a full set of system\x01",
            "checks now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "It's as Professor Russell said.\x01",
            "The damage isn't nearly as bad as we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "The ship answers her helm as well as she\x01",
            "can on the ground, and the flight engines\x01",
            "are intact...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "If we put our noses to the grindstone,\x01",
            "we should get this fine lady back in the\x01",
            "air on our own!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_5A6")

    label("loc_4EE")


    ChrTalk(    #14
        0xFE,
        (
            "It's as Professor Russell said.\x01",
            "The damage isn't nearly as bad as we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "If we put our noses to the grindstone,\x01",
            "we should get this fine lady back in the\x01",
            "air on our own!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6")

    TalkEnd(0xFE)
    Jump("loc_1827")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D9")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64B")
    Jump("loc_68D")

    label("loc_64B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_667")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68D")

    label("loc_667")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_683")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68D")

    label("loc_683")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EB")

    ChrTalk(    #16
        0xFE,
        "So our mission for now is done, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_715")

    label("loc_6EB")


    ChrTalk(    #17
        0xFE,
        "So our mission for now is done, huh?\x02",
    )

    CloseMessageWindow()

    label("loc_715")

    SetChrSubChip(0xFE, 0)

    ChrTalk(    #18
        0xFE,
        (
            "Phew! Nice work, Arseille.\x01",
            "Can't imagine it was easy just hovering\x01",
            "around, now, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Don't worry, sweetheart. We'll be back in\x01",
            "Grancel soon. Hang tight until then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_826")

    label("loc_7D9")

    TalkBegin(0xFE)

    ChrTalk(    #20
        0xFE,
        (
            "Come on, Arseille.\x01",
            "Just a bit more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "We'll be back home soon.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_826")

    Jump("loc_1827")

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_A76")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C0")
    Jump("loc_902")

    label("loc_8C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8DC")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_902")

    label("loc_8DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_902")

    label("loc_8F8")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_902")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A01")

    ChrTalk(    #22
        0xFE,
        (
            "Mmm? Who're you?\x01",
            "Sorry, but please don't distract me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "This wind is really strong.\x01",
            "Keeping us in position is difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Don't they realize how hard it is to\x01",
            "get a ship like this to hover?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_A6B")

    label("loc_A01")


    ChrTalk(    #25
        0xFE,
        (
            "Blast it... Thanks to the wind,\x01",
            "I can't get the ship to settle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "This is why I hate the seaside.\x02",
    )

    CloseMessageWindow()

    label("loc_A6B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_1827")

    label("loc_A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B9A")
    TalkBegin(0xFE)
    OP_4A(0xF, 255)

    ChrTalk(    #27
        0xE,
        (
            "So this tower's top is engulfed in those\x01",
            "weird, black barriers, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xF,
        (
            "The Professor's looking into it...\x01",
            "Still got nothin' worthwhile to report, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xF,
        "Getting close would be...dangerous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xE,
        "Oh, I agree. I'm keeping our distance.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    OP_A2(0x0)
    OP_4B(0xF, 255)
    TalkEnd(0xFE)
    Jump("loc_D13")

    label("loc_B9A")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C2A")
    Jump("loc_C6C")

    label("loc_C2A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C46")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C6C")

    label("loc_C46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C62")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C6C")

    label("loc_C62")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C6C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #31
        0xE,
        (
            "So this tower's top is engulfed in those\x01",
            "weird, black barriers, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        "Seriously, what the heck ARE those things?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_D13")

    Jump("loc_1827")

    label("loc_D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_102A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBB")
    TalkBegin(0xFE)
    OP_4A(0xF, 255)

    ChrTalk(    #33
        0xF,
        (
            "The orbal field around the tower is strange...\x01",
            "Don't get too close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xF,
        (
            "And the wind... Gotta be careful not to\x01",
            "get blown off course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        (
            "We're fine. We've got plenty of space\x01",
            "between us and the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        (
            "Still, what IS that black,\x01",
            "wall-like thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        "Is that causing those orbal field anomalies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xF,
        "I don't know...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xF,
        (
            "Just be careful with the ship,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    OP_A2(0x0)
    OP_4B(0xF, 255)
    TalkEnd(0xFE)
    Jump("loc_1027")

    label("loc_EBB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F4B")
    Jump("loc_F8D")

    label("loc_F4B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F67")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F8D")

    label("loc_F67")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F83")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F8D")

    label("loc_F83")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F8D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #40
        0xE,
        "Hey, I always play it safe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xE,
        (
            "I'll make sure there's plenty of room\x01",
            "between us and whatever that is.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_1027")

    Jump("loc_1827")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_11B3")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10C1")
    Jump("loc_1103")

    label("loc_10C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10DD")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1103")

    label("loc_10DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F9")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1103")

    label("loc_10F9")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1103")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #42
        0xFE,
        "Phew! We managed to take it down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "That was some piloting, eh? And yep!\x01",
            "That was aaall me. Please, hold your applause.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Jump("loc_1827")

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_1827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1408")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1252")
    Jump("loc_1294")

    label("loc_1252")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_126E")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1294")

    label("loc_126E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_128A")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1294")

    label("loc_128A")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1294")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #44
        0xFE,
        "Oh, yeah. You're those bracers, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I'm Lux, the Arseille's helmsman.\x01",
            "I'm in charge of piloting the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Sorry, but it looks like you guys aren't\x01",
            "gonna get a chance to show off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "A dragon? Please.\x01",
            "Even a dragon's nothing compared to the Arseille!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "You guys just sit back and enjoy the show.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x1A6A)
    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Jump("loc_1827")

    label("loc_1408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15B5")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_149F")
    Jump("loc_14E1")

    label("loc_149F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14BB")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14E1")

    label("loc_14BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14D7")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14E1")

    label("loc_14D7")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14E1")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #49
        0xFE,
        "You guys just sit back and enjoy the show.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Also, don't mind Echo right over there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "She may not be too friendly,\x01",
            "but she's a good gal at heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x1)
    OP_A2(0x2)
    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Jump("loc_1827")

    label("loc_15B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_171B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_164C")
    Jump("loc_168E")

    label("loc_164C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1668")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_168E")

    label("loc_1668")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1684")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_168E")

    label("loc_1684")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_168E")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #52
        0xFE,
        "You guys just sit back and enjoy the show.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "Also, don't mind Echo right over there.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Jump("loc_1827")

    label("loc_171B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B5")
    TalkBegin(0xFE)

    ChrTalk(    #54
        0xFE,
        (
            "Tests look good for ammo storage releases\x01",
            "on numbers one and three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Testing two and four next.\x01",
            "Connecting orbal circuits...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    TalkEnd(0xFE)
    Jump("loc_1827")

    label("loc_17B5")

    TalkBegin(0xFE)

    ChrTalk(    #56
        0xFE,
        (
            "Tests look good for ammo storage releases\x01",
            "on numbers one and three.\x01",
            "Prepare to test two and four next.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1827")

    Return()

    # Function_1_AB end

    def Function_2_1828(): pass

    label("Function_2_1828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1CAF")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18BF")
    Jump("loc_1901")

    label("loc_18BF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18DB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1901")

    label("loc_18DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18F7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1901")

    label("loc_18F7")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1901")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A3")

    ChrTalk(    #57
        0xFE,
        "Ah, captain!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "We're about to begin testing the\x01",
            "flight engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Captain...best of luck out there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA4")

    label("loc_19A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A98")

    ChrTalk(    #60
        0xFE,
        (
            "We're about to begin testing the\x01",
            "flight engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "If this works, all that remains is waiting\x01",
            "for Her Highness to return to the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I hope you have the best of luck...\x01",
            "Let me pray for you now, at the end.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1B0D")

    label("loc_1A98")

    SetChrSubChip(0xFE, 0)

    ChrTalk(    #63
        0xFE,
        (
            "Control system orbal voltage nominal...\x01",
            "All backup systems are green.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Preparations for test complete.\x02",
    )

    CloseMessageWindow()

    label("loc_1B0D")

    Jump("loc_1CA4")

    label("loc_1B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2F")

    ChrTalk(    #65
        0xFE,
        (
            "We're about to begin testing the\x01",
            "flight engine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "But we still need to recover the outrigger,\x01",
            "and you need to explore that central tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "There's still a lot of hard work ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I hope you have the best of luck...\x01",
            "Let me pray for you now, at the end.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1CA4")

    label("loc_1C2F")

    SetChrSubChip(0xFE, 0)

    ChrTalk(    #69
        0xFE,
        (
            "Control system orbal voltage nominal...\x01",
            "All backup systems are green.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "Preparations for test complete.\x02",
    )

    CloseMessageWindow()

    label("loc_1CA4")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_1CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1DF3")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D79")

    ChrTalk(    #71
        0xFE,
        "The lights are finally back on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Now we just need to repair the flight\x01",
            "systems and re-tune the controls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Maybe we can get the Arseille back\x01",
            "in the air somehow...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1DED")

    label("loc_1D79")


    ChrTalk(    #74
        0xFE,
        "The lights are finally back on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Now we just need to repair the flight\x01",
            "systems and re-tune the controls.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DED")

    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_1DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_232E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E8A")
    Jump("loc_1ECC")

    label("loc_1E8A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1EA6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1ECC")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EC2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1ECC")

    label("loc_1EC2")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1ECC")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2193")

    ChrTalk(    #76
        0xFE,
        (
            "I heard from the captain...\x01",
            "So you're the bandit girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Just don't get in the way of my work.\x01",
            "That's all I have to say to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10B,
        (
            "#211FHa-HA! Well, aren't YOU ignorant?\x02\x03",

            "You haven't yet realized how fantastically\x01",
            "useful I am!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Really? Well, that's nice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "...So would you mind getting lost?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10B,
        "#213FWha-?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "You're fantastically in the way of\x01",
            "my work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Didn't I just tell you not to do that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10B,
        "#216FWhaaaaaaaaaaaat...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1016F(Wh-Whoaaa, whoa. Calm down, keep it cool.)\x02\x03",

            "(Are you gonna get in a fight with\x01",
            "someone you just met?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        "#1052F(Sorry, Josette. I think you've lost this one.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10B,
        "#215F(Nnnnnngh...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x229F)
    Jump("loc_2323")

    label("loc_2193")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_223B")

    ChrTalk(    #88
        0xFE,
        "Stop getting in the way of my work...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "As long as you can do that,\x01",
            "I don't care what you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10B,
        "#216F(I kinda think I hate this woman...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2323")

    label("loc_223B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D3")

    ChrTalk(    #91
        0xFE,
        (
            "The bandits seem to be in the\x01",
            "same situation we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "We'll do what we can to assist them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "Those are...orders, after all.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2323")

    label("loc_22D3")


    ChrTalk(    #94
        0xFE,
        "We'll do what we can to assist them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "Those are...orders, after all.\x02",
    )

    CloseMessageWindow()

    label("loc_2323")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_232E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_257F")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23C5")
    Jump("loc_2407")

    label("loc_23C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23E1")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2407")

    label("loc_23E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23FD")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2407")

    label("loc_23FD")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2407")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2502")

    ChrTalk(    #96
        0xFE,
        (
            "There've been strange readings on our\x01",
            "various instruments since our landing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Extremely powerful orbal energy readings,\x01",
            "completely outside of common sense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "...Just what is this place?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2574")

    label("loc_2502")


    ChrTalk(    #99
        0xFE,
        (
            "There've been strange readings on our\x01",
            "various instruments since our landing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "Just what is this place?\x02",
    )

    CloseMessageWindow()

    label("loc_2574")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_257F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2842")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2616")
    Jump("loc_2658")

    label("loc_2616")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2632")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2658")

    label("loc_2632")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_264E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2658")

    label("loc_264E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2658")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277B")

    ChrTalk(    #101
        0xFE,
        (
            "Disruptions in the orbal fields are\x01",
            "growing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "There's no change in the tower yet,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271E")

    ChrTalk(    #103
        0xFE,
        "Princess...please, be careful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2739")

    label("loc_271E")


    ChrTalk(    #104
        0xFE,
        "Be careful, everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_2739")


    ChrTalk(    #105
        0xFE,
        (
            "These phenomena may be a sign of\x01",
            "something even worse.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2837")

    label("loc_277B")


    ChrTalk(    #106
        0xFE,
        (
            "Disruptions in the orbal fields are\x01",
            "growing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "This...could be a sign of something\x01",
            "worse to come.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281C")

    ChrTalk(    #108
        0xFE,
        "Princess...please, be careful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2837")

    label("loc_281C")


    ChrTalk(    #109
        0xFE,
        "Be careful, everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_2837")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_2AF9")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28D9")
    Jump("loc_291B")

    label("loc_28D9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28F5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_291B")

    label("loc_28F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2911")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_291B")

    label("loc_2911")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_291B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A52")

    ChrTalk(    #110
        0xFE,
        "Great work, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "We still haven't figured out what the\x01",
            "source of the orbal field anomaly is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "If we could just figure out what it is,\x01",
            "we could do something about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "I'm sorry...but I think we'll be\x01",
            "relying on you for a while longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2AEE")

    label("loc_2A52")


    ChrTalk(    #114
        0xFE,
        (
            "We still haven't figured out what the\x01",
            "source of the orbal field anomaly is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I'm sorry...but I think we'll be\x01",
            "relying on you for a while longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AEE")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_2AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_2C49")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BEF")

    ChrTalk(    #116
        0xE,
        (
            "So this tower's top is engulfed in\x01",
            "those black barriers too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xF,
        (
            "The professor's looking into it.\x01",
            "Still no answer, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xF,
        "Getting close would be dangerous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xE,
        "Oh, I agree. I'm keeping our distance.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    OP_A2(0x3)
    Jump("loc_2C43")

    label("loc_2BEF")


    ChrTalk(    #120
        0xF,
        (
            "The orbal field around the tower is\x01",
            "still odd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xF,
        "We can't get any closer.\x02",
    )

    CloseMessageWindow()

    label("loc_2C43")

    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_2C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_2E50")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DE5")

    ChrTalk(    #122
        0xF,
        (
            "The orbal field around the tower is\x01",
            "strange... Don't get too close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xF,
        (
            "And the wind... Be careful not to get\x01",
            "blown off course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xE,
        (
            "We're fine. We've got plenty of space\x01",
            "between us and the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xE,
        (
            "Still, what the hell IS that black\x01",
            "wall-like thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xE,
        "Is that causing those orbal field anomalies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xF,
        "I don't know...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xF,
        (
            "Just be careful with the ship,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    OP_A2(0x3)
    Jump("loc_2E4A")

    label("loc_2DE5")


    ChrTalk(    #129
        0xF,
        (
            "It's too much of a risk to get\x01",
            "any closer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xF,
        (
            "A scout ship is approaching from\x01",
            "the surface.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4A")

    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_2E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_3099")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EE7")
    Jump("loc_2F29")

    label("loc_2EE7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F03")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F29")

    label("loc_2F03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F1F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F29")

    label("loc_2F1F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F29")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3020")

    ChrTalk(    #131
        0xFE,
        "...Why don't you go check on the dragon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Confirming a victory is an important\x01",
            "duty for any soldier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "...Or would you rather be shot in the back\x01",
            "by an enemy you thought was defeated?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_308E")

    label("loc_3020")


    ChrTalk(    #134
        0xFE,
        "...Why don't you go check on the dragon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Confirming a victory is an important\x01",
            "duty for any soldier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308E")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_3099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_35E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3239")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3138")
    Jump("loc_317A")

    label("loc_3138")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3154")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_317A")

    label("loc_3154")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3170")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_317A")

    label("loc_3170")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_317A")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #136
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "You guys are here to observe the operation, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Well, I've just got one thing to say\x01",
            "to you: don't get in our way.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x1A6B)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_3239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3390")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32D0")
    Jump("loc_3312")

    label("loc_32D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32EC")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3312")

    label("loc_32EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3308")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3312")

    label("loc_3308")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3312")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #139
        0xFE,
        "We're finished talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "...Why don't you return to your post?\x02",
    )

    CloseMessageWindow()
    OP_A3(0x4)
    OP_A2(0x5)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_3390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_34CA")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3427")
    Jump("loc_3469")

    label("loc_3427")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3443")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3469")

    label("loc_3443")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_345F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3469")

    label("loc_345F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3469")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #141
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "...Do you have nothing else to do?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_34CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357D")
    TalkBegin(0xFE)

    ChrTalk(    #143
        0xFE,
        "No orbal responses in local airspace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I repeat...no orbal responses in local\x01",
            "airspace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "All patrol ships are to continue on\x01",
            "current patrols...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    TalkEnd(0xFE)
    Jump("loc_35E5")

    label("loc_357D")

    TalkBegin(0xFE)

    ChrTalk(    #146
        0xFE,
        (
            "No orbal responses in local airspace...\x01",
            "All patrol ships are to continue on\x01",
            "current patrols.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_35E5")

    Return()

    # Function_2_1828 end

    def Function_3_35E6(): pass

    label("Function_3_35E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_383D")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_367D")
    Jump("loc_36BF")

    label("loc_367D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3699")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36BF")

    label("loc_3699")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36B5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36BF")

    label("loc_36B5")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36BF")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37BA")

    ChrTalk(    #147
        0xFE,
        (
            "It seems like the Bobcat's repairs are\x01",
            "going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Apparently Professor Russell's advice didn't\x01",
            "just repair their flight systems, but improved\x01",
            "them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "Even the bandits were admiring him!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3832")

    label("loc_37BA")


    ChrTalk(    #150
        0xFE,
        (
            "It seems like the Bobcat's repairs are\x01",
            "going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "Sounds like the professor's advice\x01",
            "really helped them out!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3832")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_383D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_3A53")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E2")

    ChrTalk(    #152
        0x10,
        (
            "\x07\x00#1PThis is the Arseille.\x01",
            "Bobcat, please respond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x10,
        (
            "\x07\x00#1PI repeat, this is the Arseille,\x01",
            "Bobcat, pl--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x1B,
        "\x07\x05#2P#1SAh, yeah, this is the Bobcat.\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x1B,
        (
            "\x07\x05#2P#1SWe read you clearly, over.\x01",
            "Arseille, how's it look on your end?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x10,
        (
            "\x07\x00#1PArseille to Bobcat, signal is crisp\x01",
            "and clear! Good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x10,
        "\x07\x00#1PDo you need any supplies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10,
        (
            "\x07\x00#1PI repeat: Bobcat, are you in need of\x01",
            "supplies, or...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3A4D")

    label("loc_39E2")


    ChrTalk(    #159
        0x10,
        "\x07\x00#1PBobcat, do you need any supplies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10,
        (
            "\x07\x00#1PI repeat: Bobcat, are you in need of\x01",
            "supplies, or...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A4D")

    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_3A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_3E8A")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AEA")
    Jump("loc_3B2C")

    label("loc_3AEA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B06")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B2C")

    label("loc_3B06")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B22")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B2C")

    label("loc_3B22")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B2C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CCC")

    ChrTalk(    #161
        0xFE,
        "So you're the bandit lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Do the comm systems on your vessel\x01",
            "still work, by chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10B,
        (
            "#210FThey should be okay, I think.\x02\x03",

            "The bridge didn't take a lot of damage,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "All right, then, I'll get ready to hail them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Gotta think ahead in case your brothers\x01",
            "return safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x10B,
        (
            "#211FAh, yeah! Thanks!\x01",
            "Can't wait to hear from you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x22CF)
    Jump("loc_3E7F")

    label("loc_3CCC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D48")

    ChrTalk(    #167
        0xFE,
        (
            "I'll make sure we can hail the bandit\x01",
            "ship when the time comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "I hope your brothers are safe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E7F")

    label("loc_3D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFB")

    ChrTalk(    #169
        0xFE,
        (
            "If the bandits are here, then their ship\x01",
            "should be here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I might be able to raise them\x01",
            "on the radio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "I'll give it a shot if I can find the time.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3E7F")

    label("loc_3DFB")


    ChrTalk(    #172
        0xFE,
        (
            "If the bandits are here, then their ship\x01",
            "should be here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "If this works out, we may be able to\x01",
            "communicate via radio.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E7F")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_3E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4079")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FEE")

    ChrTalk(    #174
        0xFE,
        (
            "Communications equipment checks out.\x01",
            "Everything is working normally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "What makes me curious are these occasional\x01",
            "transmissions we keep receiving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "They're encrypted, so I can't tell what\x01",
            "they're saying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "...but I'm pretty sure they're Ouroboros\x01",
            "transmissions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "Looks like they're investigating the\x01",
            "city, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_4073")

    label("loc_3FEE")


    ChrTalk(    #179
        0xFE,
        (
            "These occasional transmissions we catch\x01",
            "seem to be Ouroboros comm chatter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Looks like they're investigating the\x01",
            "city, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4073")

    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_4079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_449A")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4110")
    Jump("loc_4152")

    label("loc_4110")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_412C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4152")

    label("loc_412C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4148")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4152")

    label("loc_4148")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4152")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435B")

    ChrTalk(    #181
        0xFE,
        (
            "It seems like the attacks on the cities\x01",
            "are starting to flag a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427C")

    ChrTalk(    #182
        0xFE,
        (
            "If we can take this last tower,\x01",
            "that should settle things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "I wish you the best of luck...from myself and\x01",
            "from the entire crew. We'll be praying for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4355")

    label("loc_427C")


    ChrTalk(    #184
        0xFE,
        (
            "If we can take this last tower,\x01",
            "that should settle things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "Though, I can't help but feel things\x01",
            "aren't really settled either way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "I suppose it's because we don't know,\x01",
            "really, what the enemy's after.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4355")

    OP_A2(0x6)
    Jump("loc_448F")

    label("loc_435B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43F4")

    ChrTalk(    #187
        0xFE,
        (
            "This is the last tower, but it just\x01",
            "doesn't feel right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "I suppose it's because we don't know,\x01",
            "really, what the enemy's after.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448F")

    label("loc_43F4")


    ChrTalk(    #189
        0xFE,
        (
            "We're finally at the last tower, but\x01",
            "somehow it just doesn't feel right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "I suppose it's because we don't know,\x01",
            "really, what the enemy's after.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448F")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_449A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_4613")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4552")

    ChrTalk(    #191
        0xFE,
        (
            "Ruan Rearguard, Manoria station, this is the\x01",
            "Arseille. Ruan Rearguard, report your situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "I repeat, this is the Arseille.\x01",
            "Ruan Rearguard, report.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_460D")

    label("loc_4552")


    ChrTalk(    #193
        0xFE,
        (
            "Ruan Rearguard, this is the Arseille.\x01",
            "Patrol ships are en route to reinforce\x01",
            "your position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "Reinforcements will be arriving shortly.\x01",
            "Repeat, they will be in Manoria airspace...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460D")

    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_4613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_4758")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46BF")

    ChrTalk(    #195
        0xFE,
        (
            "Sounds like there's some terrible fighting\x01",
            "still going on in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "If we hear anything new, I'll let you know\x01",
            "the second it comes in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4752")

    label("loc_46BF")


    ChrTalk(    #197
        0xFE,
        (
            "Sounds like there's some terrible fighting\x01",
            "still going on in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "If we hear anything new, I'll let you know\x01",
            "the second it comes in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4752")

    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_4758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_48F1")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4808")

    ChrTalk(    #199
        0xFE,
        (
            "Headquarters, this is the Arseille.\x01",
            "Repeat, Arseille to headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "We have arrived at the designated\x01",
            "coordinates. Repeat, we have arrived.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_48EB")

    label("loc_4808")


    ChrTalk(    #201
        0xFE,
        (
            "We've confirmed a suspicious silhouette at the\x01",
            "designated coordinates. We have determined\x01",
            "that a direct landing is impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "...and will be dispatching an investigation\x01",
            "team from the ground. Repeat, we will be...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48EB")

    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_48F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_4A61")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4988")
    Jump("loc_49CA")

    label("loc_4988")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_49A4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49CA")

    label("loc_49A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49C0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49CA")

    label("loc_49C0")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49CA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #203
        0xFE,
        "The dragon's totally asleep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "Even if it were to take to the skies again,\x01",
            "it poses no danger.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4DE9")

    label("loc_4A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_4DE9")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AF8")
    Jump("loc_4B3A")

    label("loc_4AF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B14")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B3A")

    label("loc_4B14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B30")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B3A")

    label("loc_4B30")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B3A")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C45")

    ChrTalk(    #205
        0xFE,
        (
            "Ah, hello!\x01",
            "You're the observers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I'm Leon, the Arseille's Communications\x01",
            "Officer. I run the switchboard and radio\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "Probably won't be a very long acquaintance,\x01",
            "but it's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_A2(0x1A6C)
    Jump("loc_4DE1")

    label("loc_4C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4CB8")

    ChrTalk(    #208
        0xFE,
        (
            "Probably won't be a very long acquaintance,\x01",
            "but it's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "Let's both do our best.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DE1")

    label("loc_4CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D70")

    ChrTalk(    #210
        0xFE,
        (
            "Arseille to Colbo-One.\x01",
            "Arseille to Colbo-One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "No response in local airspace...\x01",
            "Repeat, no local response.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "Your ship is to continue patrolling...\x01",
            "Repeat...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_4DE1")

    label("loc_4D70")


    ChrTalk(    #213
        0xFE,
        "Arseille to Cruise-Two, come in, Cruise-Two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "Arseille to Cruise-Two.\x01",
            "Report your current status, over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE1")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_4DE9")

    Return()

    # Function_3_35E6 end

    def Function_4_4DEA(): pass

    label("Function_4_4DEA")

    TalkBegin(0xFE)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_4FFF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E79")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #215
        0xFE,
        "We await your return to the ship!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        "May Aidios' blessings be with you!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jump("loc_4FFC")

    label("loc_4E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F58")

    ChrTalk(    #217
        0xFE,
        "Everyone, thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "We're about to recover and start repairs\x01",
            "on the left outrigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "There's still a possibility the society\x01",
            "might attack, so we can't let our guard\x01",
            "down yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_4FFC")

    label("loc_4F58")


    ChrTalk(    #220
        0xFE,
        (
            "We're about to recover and start repairs\x01",
            "on the left outrigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "There's still a possibility the society\x01",
            "might attack, so we can't let our guard\x01",
            "down yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FFC")

    Jump("loc_5DF8")

    label("loc_4FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_520C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_518F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50CD")

    ChrTalk(    #222
        0xFE,
        (
            "I hear the one who's in the Amberl\x01",
            "Tower is just a little girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "I truly cannot fathom the minds of the\x01",
            "society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "Your Highness, please take the greatest\x01",
            "care.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_518C")

    label("loc_50CD")


    ChrTalk(    #225
        0xFE,
        (
            "She may be a child, but she is no doubt\x01",
            "still a ruthless servant of the society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "I know you hardly need the likes of me\x01",
            "to worry about you, but please stay on\x01",
            "guard, Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_518C")

    Jump("loc_5209")

    label("loc_518F")


    ChrTalk(    #227
        0xFE,
        (
            "I hear the one who's in the Amberl\x01",
            "Tower is just a little girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "I truly cannot fathom the minds of the\x01",
            "society.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5209")

    Jump("loc_5DF8")

    label("loc_520C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_55C4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53EE")

    ChrTalk(    #229
        0xFE,
        (
            "Oh! Your Highness, will you be\x01",
            "departing for the tower as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "Please, be sure to act with the\x01",
            "greatest care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "If the worst happened, I would not be\x01",
            "surprised to see Captain Schwarz climb\x01",
            "the tower herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x105,
        (
            "#045FThat's...a good point.\x02\x03",

            "Still, I don't think you need to worry.\x01",
            "I will be with everyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "I see...\x01",
            "As you wish then, Your Highness.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x101, 400)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #234
        0xFE,
        (
            "Bracers!\x01",
            "Please, take care of Her Highness.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0x1E40)
    Jump("loc_5495")

    label("loc_53EE")


    ChrTalk(    #235
        0xFE,
        (
            "Your Highness, please be sure to act\x01",
            "with the greatest care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "If the worst happened, I would not be\x01",
            "surprised to see Captain Schwarz climb\x01",
            "the tower herself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5495")

    Jump("loc_55C1")

    label("loc_5498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5542")

    ChrTalk(    #237
        0xFE,
        (
            "Did you hear a woman made it to\x01",
            "the top of Carnelia Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "Wow, she must be incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "Though, I bet our Captain Schwarz could\x01",
            "do the same.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_55C1")

    label("loc_5542")


    ChrTalk(    #240
        0xFE,
        (
            "Climbing one of the towers herself...\x01",
            "What an incredible woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Though, I bet our Captain Schwarz could\x01",
            "do the same.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55C1")

    Jump("loc_5DF8")

    label("loc_55C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_5951")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5772")

    ChrTalk(    #242
        0xFE,
        (
            "The black barrier which surrounds the roof,\x01",
            "and the strange...space...within. Hmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "The Tetracyclic Towers were more than\x01",
            "they appeared, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "Your Highness, please be careful.\x01",
            "We don't know what might happen from\x01",
            "here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x105,
        (
            "#040FI know, thank you.\x02\x03",

            "Please, take care of things while\x01",
            "I am away.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #246
        0xFE,
        (
            "Yes, Your Highness!\x01",
            "We wish you the best of luck.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xA)
    Jump("loc_57C3")

    label("loc_5772")

    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #247
        0xFE,
        (
            "Leave the ship to us.\x01",
            "Your Highness, please be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_57C3")

    Jump("loc_594E")

    label("loc_57C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58B3")

    ChrTalk(    #248
        0xFE,
        (
            "The black wall which surrounds the roof,\x01",
            "and the strange...space...within. Hmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "The Tetracyclic Towers were more than\x01",
            "they appeared, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "Perhaps they have some special function\x01",
            "we can't even imagine.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_594E")

    label("loc_58B3")


    ChrTalk(    #251
        0xFE,
        (
            "The black wall which surrounds the roof,\x01",
            "and the strange...space...within. Hmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "The Tetracyclic Towers were more than\x01",
            "they appeared, it seems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_594E")

    Jump("loc_5DF8")

    label("loc_5951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_5C03")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D4")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #253
        0xFE,
        "Keep up the good work, friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "The ship is currently problem-free!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xA)
    Jump("loc_5A1F")

    label("loc_59D4")

    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #255
        0xFE,
        (
            "Greetings, everyone!\x01",
            "The ship's status is normal!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_5A1F")

    Jump("loc_5C00")

    label("loc_5A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B6B")

    ChrTalk(    #256
        0xFE,
        (
            "Everyone, thank you for your hard work.\x01",
            "Have you gotten a grasp of the interior\x01",
            "of the ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "The lift to use when departing is in\x01",
            "the cargo bay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "If you follow those stairs down to the\x01",
            "bottom and head aft, you'll find the\x01",
            "cargo bay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "Our workshop is nearby.\x01",
            "You may wish to stop in there as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_5C00")

    label("loc_5B6B")


    ChrTalk(    #260
        0xFE,
        (
            "The lift to use when departing is in\x01",
            "the cargo bay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "If you follow those stairs down to the\x01",
            "bottom and head aft, you'll find the\x01",
            "cargo bay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C00")

    Jump("loc_5DF8")

    label("loc_5C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_5C74")

    ChrTalk(    #262
        0xFE,
        "Please, hurry, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "The dragon's splashed down in the water\x01",
            "directly ahead of the ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DF8")

    label("loc_5C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_5DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D65")

    ChrTalk(    #264
        0xFE,
        "Hello, bracers. Welcome aboard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "Just above here is the bridge, and just\x01",
            "below us is the conference room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "The Arseille is a pretty large ship.\x01",
            "People tend to get lost at first when\x01",
            "they're assigned to her.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_5DF8")

    label("loc_5D65")


    ChrTalk(    #267
        0xFE,
        (
            "Just above here is the bridge,\x01",
            "and just below us is the conference room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "The hatches to the left and right lead\x01",
            "out onto the outer deck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DF8")

    TalkEnd(0xFE)
    Return()

    # Function_4_4DEA end

    def Function_5_5DFC(): pass

    label("Function_5_5DFC")

    TalkBegin(0xFE)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_60A6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EFD")

    ChrTalk(    #269
        0xFE,
        (
            "One more tower until we complete\x01",
            "Her Highness' command...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "We all pray that Your Highness returns\x01",
            "with a smile on her face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x105,
        "#040FThank you. Take care in my absence.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #272
        0xFE,
        "Ma'am!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xC)
    Jump("loc_5F7B")

    label("loc_5EFD")

    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #273
        0xFE,
        (
            "We of the Royal Guard will pray for\x01",
            "Her Highness' luck in battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "We await your smiling return.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_5F7B")

    Jump("loc_60A3")

    label("loc_5F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_603F")

    ChrTalk(    #275
        0xFE,
        (
            "Everyone, good work.\x01",
            "We're finally at the last tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "Still, be sure not to let your guard down\x01",
            "until you complete Her Highness' command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        "We pray for your victory.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_60A3")

    label("loc_603F")


    ChrTalk(    #278
        0xFE,
        (
            "This is the last tower, but be sure\x01",
            "not to let your guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "We pray for your victory.\x02",
    )

    CloseMessageWindow()

    label("loc_60A3")

    Jump("loc_6848")

    label("loc_60A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_6286")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_613A")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #280
        0xFE,
        (
            "We shall do our best to assist the defense\x01",
            "brigades in their battles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "Your Highness, take care.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jump("loc_6283")

    label("loc_613A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_620A")

    ChrTalk(    #282
        0xFE,
        (
            "We've gotten word that society forces are\x01",
            "acting in Ruan, as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "They seem to have men everywhere\x01",
            "in the kingdom!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "We need to strengthen our patrols in the\x01",
            "future, it seems...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_6283")

    label("loc_620A")


    ChrTalk(    #285
        0xFE,
        (
            "Ouroboros seems to have men across the\x01",
            "entire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "We need to patrol more often in the\x01",
            "future, it seems...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6283")

    Jump("loc_6848")

    label("loc_6286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_6547")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6349")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #287
        0xFE,
        "Good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "We shall protect the ship while you are\x01",
            "away, Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "Please focus on completing your mission\x01",
            "without worry.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xC)
    Jump("loc_63DB")

    label("loc_6349")

    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #290
        0xFE,
        (
            "We shall protect the ship while you are\x01",
            "away, Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "Please focus on completing your mission\x01",
            "without worry.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    label("loc_63DB")

    Jump("loc_6544")

    label("loc_63DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64AD")

    ChrTalk(    #292
        0xFE,
        "The situation in Zeiss sounds hellish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "The Zeiss Guard is managing to keep it\x01",
            "together, though...somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "I'm sure if the worst happens, there'll\x01",
            "be reinforcements from Leiston.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_6544")

    label("loc_64AD")


    ChrTalk(    #295
        0xFE,
        (
            "Zeiss sounds like Gehenna, but they're\x01",
            "holding it together, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "I'm sure if the worst happens, there'll\x01",
            "be reinforcements from Leiston.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6544")

    Jump("loc_6848")

    label("loc_6547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_6848")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_672F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6680")

    ChrTalk(    #297
        0xFE,
        (
            "Princess Klaudia stepped out onto the\x01",
            "deck a moment ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "She seemed...distracted and unwell,\x01",
            "compared to her usual self.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "I suppose Her Highness carries the weight of\x01",
            "Liberl's troubles on her slender shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "I wish there was something we could do...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_672C")

    label("loc_6680")


    ChrTalk(    #301
        0xFE,
        (
            "Her Highness seemed...distracted and\x01",
            "unwell, compared to her usual self.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "I suppose Her Highness carries the weight of\x01",
            "Liberl's troubles on her slender shoulders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_672C")

    Jump("loc_6848")

    label("loc_672F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D1")

    ChrTalk(    #303
        0xFE,
        (
            "Bracers. Please do your utmost to protect\x01",
            "Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x105, 400)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #304
        0xFE,
        (
            "And Your Highness...please, take care\x01",
            "of yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_A2(0xD)
    Jump("loc_6848")

    label("loc_67D1")


    ChrTalk(    #305
        0xFE,
        (
            "Please do your utmost to protect\x01",
            "Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x105, 400)

    ChrTalk(    #306
        0xFE,
        (
            "And Your Highness...please, take care of\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6848")

    TalkEnd(0xFE)
    Return()

    # Function_5_5DFC end

    def Function_6_684C(): pass

    label("Function_6_684C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68BF")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #307
        0xFE,
        "Princess...please stay safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "The crew is praying for your victory!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jump("loc_699C")

    label("loc_68BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692E")
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #309
        0xFE,
        "Captain...please stay safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        "The crew is praying for your victory.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Jump("loc_699C")

    label("loc_692E")

    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #311
        0xFE,
        "Good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "Everyone's assembling on the bridge in\x01",
            "preparation for the flight engine test.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_699C")

    TalkEnd(0xFE)
    Return()

    # Function_6_684C end

    def Function_7_69A0(): pass

    label("Function_7_69A0")

    TalkBegin(0xFE)

    ChrTalk(    #313
        0xFE,
        "#160F◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_69A0 end

    def Function_8_69C0(): pass

    label("Function_8_69C0")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_6F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A43")
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #314
        0x15,
        (
            "#270FAh, Ms. Bright.\x02\x03",

            "How are your explorations going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#1011FActually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 19)
    Return()

    label("loc_6A43")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6AA6"),
        (1, "loc_6EED"),
        (2, "loc_6F27"),
        (SWITCH_DEFAULT, "loc_6F2A"),
    )


    label("loc_6AA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C3B")

    ChrTalk(    #316
        0x15,
        (
            "#270FI will be honest, I didn't think we would\x01",
            "get this far in the repairs so quickly.\x02\x03",

            "Liberl continues to impress. The standard\x01",
            "of your engineers is quite high.\x02\x03",

            "And I understand that a number of your\x01",
            "engineering staff have received training\x01",
            "from Professor Russell.\x02\x03",

            "#272FAs a soldier who worries about the\x01",
            "technological state of his country...\x01",
            "I must admit, I'm envious.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_6CEC")

    label("loc_6C3B")


    ChrTalk(    #317
        0x15,
        (
            "#277FI understand that a number of your\x01",
            "engineering staff have received training\x01",
            "from Professor Russell.\x02\x03",

            "I almost wish I could take two or three\x01",
            "with me back to Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CEC")

    Jump("loc_6EEA")

    label("loc_6CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E21")

    ChrTalk(    #318
        0x15,
        (
            "#272FGetting this much repair work done\x01",
            "in such a short time...\x02\x03",

            "#270FLiberl continues to impress. The standard\x01",
            "of your engineers is quite high.\x02\x03",

            "And I understand that a number of your\x01",
            "engineering staff have received training\x01",
            "from Professor Russell.\x02\x03",

            "I'm a little envious, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_6EEA")

    label("loc_6E21")


    ChrTalk(    #319
        0x15,
        (
            "#276FI understand that a number of your\x01",
            "engineering staff have received training\x01",
            "from Professor Russell.\x02\x03",

            "I've half a mind to throw a few over my\x01",
            "shoulder and carry them back to Erebonia\x01",
            "with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EEA")

    Jump("loc_6F2A")

    label("loc_6EED")


    ChrTalk(    #320
        0x15,
        "#277FHm? Do you wish for me to accompany you?\x02",
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_6F2A")

    label("loc_6F27")

    Jump("loc_6F2A")

    label("loc_6F2A")

    Jump("loc_745C")

    label("loc_6F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_6F37")
    Jump("loc_745C")

    label("loc_6F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_6F41")
    Jump("loc_745C")

    label("loc_6F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_745C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7072")

    ChrTalk(    #321
        0x15,
        (
            "#270FOur first order of business should be\x01",
            "restoring internal lights and securing\x01",
            "the hallways.\x02\x03",

            "We cannot move personnel and material\x01",
            "around otherwise, after all.\x02\x03",

            "It would be wise to make sure the interior\x01",
            "is in as good a shape as possible before\x01",
            "starting the 'real' repairs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_745C")

    label("loc_7072")


    ChrTalk(    #322
        0x15,
        (
            "#270FOur first order of business should be\x01",
            "restoring internal lights and securing\x01",
            "the hallways.\x02\x03",

            "Without that, we cannot move personnel\x01",
            "through the ship effectively...\x02\x03",

            "We should get as much ready as we can\x01",
            "before beginning the 'real' repairs.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_745C")
    TurnDirection(0x15, 0x104, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73EA")

    ChrTalk(    #323
        0x15,
        (
            "#272FForgive me, Ms. Bright, but I must ask\x01",
            "that you watch over that moron.\x02\x03",

            "In truth, he would simply get in the way\x01",
            "of repairs if we had him aboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x104,
        (
            "#032FOr so you claim, but you really wish\x01",
            "to be alone with Captain Schwarz,\x01",
            "do you not?\x02\x03",

            "How could you allow yourself to be\x01",
            "distracted by the allure of a woman,\x01",
            "even though you have me?!\x02\x03",

            "#039FAAAAHH! You CHEAT!\x01",
            "You merely wanted me for my body,\x01",
            "didn't you?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #325
        0x15,
        (
            "#274F...\x02\x03",

            "...My point is illustrated, I hope,\x01",
            "Ms. Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x101,
        "#1002FYeah. Completely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x102,
        (
            "#1035FWe'll do our best to make sure he doesn't\x01",
            "get into too much trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22AD)
    Jump("loc_745C")

    label("loc_73EA")

    TurnDirection(0x15, 0x104, 400)
    Sleep(400)

    ChrTalk(    #328
        0x15,
        (
            "#272FWell, then...please try not to get that\x01",
            "idiot blown up too badly. A little is fine,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_745C")

    TalkEnd(0xFE)
    Return()

    # Function_8_69C0 end

    def Function_9_7460(): pass

    label("Function_9_7460")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_7996")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_764D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75BF")

    ChrTalk(    #329
        0x16,
        (
            "#140FPhew! Seems like the repairs are comin'\x01",
            "along pretty well.\x02\x03",

            "Now if we can just stop Ouroboros dead in\x01",
            "their tracks, it'll be a no-strings-attached\x01",
            "happy ending.\x02\x03",

            "#141FNow don't you worry, we noble reporters\x01",
            "will be doin' our jobs too.\x02\x03",

            "You just focus on givin' us something\x01",
            "great to write about!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_764A")

    label("loc_75BF")


    ChrTalk(    #330
        0x16,
        (
            "#141FNow don't you worry, we noble reporters\x01",
            "will be doin' our jobs too.\x02\x03",

            "You just focus on givin' us something\x01",
            "great to write about!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_764A")

    Jump("loc_7996")

    label("loc_764D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78B3")

    ChrTalk(    #331
        0x16,
        (
            "#140FI was worried for a while, but it seems\x01",
            "like repairs are goin' okay.\x02\x03",

            "Professor Russell pretty much hauled our\x01",
            "bacon out of the fire.\x02\x03",

            "#141FNow if we can just stop Ouroboros dead in\x01",
            "their tracks, it'll be a no-strings-attached\x01",
            "happy ending.\x02\x03",

            "I'll make sure we get the front page\x01",
            "of a special edition for this one.\x02\x03",

            "You guys just focus on giving us the\x01",
            "biggest, most slam-bang action story\x01",
            "of the century!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78AD")
    TurnDirection(0x16, 0x10F, 400)

    ChrTalk(    #332
        0x16,
        (
            "#147FHey, we'd love to have you appear in our\x01",
            "special edition as well, Captain Schwarz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x10F,
        "#176F...I'm afraid I must refuse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x16,
        "#145F(Bah, still no luck.)\x02",
    )

    CloseMessageWindow()

    label("loc_78AD")

    OP_A2(0xF)
    Jump("loc_7996")

    label("loc_78B3")


    ChrTalk(    #335
        0x16,
        (
            "#141FIf we can stop Ouroboros' plans, we'll\x01",
            "have a no-strings-attached happy ending\x01",
            "on our hands.\x02\x03",

            "I'll make sure we get the front page of a\x01",
            "special edition for this one, so make sure\x01",
            "to give us a flashy action story, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7996")

    TalkEnd(0xFE)
    Return()

    # Function_9_7460 end

    def Function_10_799A(): pass

    label("Function_10_799A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_7B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B1F")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #336
        0x17,
        (
            "#150FYoo-hoooo! Hi, Estelle, everybody!\x02\x03",

            "It sounds like you're heading someplace\x01",
            "scary...\x02\x03",

            "Everyone! Come back safe, okay?\x02\x03",

            "I'll take a souvenir photo of your\x01",
            "victory when you do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        "#1008FA...souvenir photo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x102,
        "#1054FSounds more like we're on a vacation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x17,
        (
            "#151FHeehee! It's a great idea, right?\x02\x03",

            "I want us aaaaall to remember why we\x01",
            "came here!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_7B81")

    label("loc_7B1F")


    ChrTalk(    #340
        0x17,
        (
            "#150FI'm gonna take a photo of eeeeeveryone\x01",
            "at the end!\x02\x03",

            "So...make sure you come back, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B81")

    TalkEnd(0xFE)
    Return()

    # Function_10_799A end

    def Function_11_7B85(): pass

    label("Function_11_7B85")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7BEB"),
        (1, "loc_8434"),
        (2, "loc_846D"),
        (SWITCH_DEFAULT, "loc_8470"),
    )


    label("loc_7BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EED")
    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #341
        0x8,
        (
            "#021FOho! That's a familiar face.\x02\x03",

            "#021FI never had imagined we'd meet\x01",
            "again in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x10B,
        (
            "#214FThat is totally MY line!\x02\x03",

            "Sheesh, what is it with you and that whip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x8,
        (
            "#027FOh, I was just playing with you\x01",
            "back then.\x02\x03",

            "#525FIf you like, I could be a bit...\x01",
            "rougher next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x10B,
        (
            "#216FNgaaah, why does it sound like you aren't\x01",
            "actually joking?...\x02\x03",

            "#416FA-Anyway, given where we are, I'm\x01",
            "willing to bury the hatchet. And the whip.\x01",
            "(Please, bury the whip.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x8,
        (
            "#020FAs much as a little part of me would\x01",
            "enjoy it, whipping each other only serves\x01",
            "Ouroboros' interests, yes?\x02\x03",

            "I'm perfectly willing to consider the\x01",
            "hatchet six arge under.\x02\x03",

            "I'll be looking forward to seeing what\x01",
            "you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x10B,
        "#210FHeh. Just you wait!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)
    OP_A2(0x22A0)
    Jump("loc_8431")

    label("loc_7EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F7F")
    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #347
        0x8,
        (
            "#020FI agree. Given where we are, the past is\x01",
            "water under the bridge.\x02\x03",

            "Let's stand together against the society.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8431")

    label("loc_7F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_808E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8028")

    ChrTalk(    #348
        0x8,
        (
            "#020FWell, the lights are back on, at least.\x02\x03",

            "Hopefully, that'll get the repairs done\x01",
            "faster.\x02\x03",

            "Now I need to find something else to\x01",
            "help with.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_808B")

    label("loc_8028")


    ChrTalk(    #349
        0x8,
        (
            "#020FWell, the lights are back on, at least.\x02\x03",

            "Hopefully, that'll get the repairs done\x01",
            "faster.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_808B")

    Jump("loc_8431")

    label("loc_808E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_8431")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C4")

    ChrTalk(    #350
        0x101,
        "#1011FSchera, are you helping with repairs?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #351
        0x8,
        (
            "#020FMm-hmm. Professor Russell asked me to\x01",
            "inspect the light fixtures.\x02\x03",

            "We'll be switching back to normal lighting\x01",
            "soon, so...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8248")

    ChrTalk(    #352
        0x107,
        (
            "#561FSchera, I'm sorry.\x02\x03",

            "That's something I should be doing,\x01",
            "but Estelle needs my help...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #353
        0x8,
        (
            "#021FAww! Don't worry about it, Tita.\x02\x03",

            "#525FYou just focus on helping Estelle with\x01",
            "exploring, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x107,
        "#560FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_83BE")

    label("loc_8248")


    ChrTalk(    #355
        0x101,
        (
            "#1018FOh, so we'll be able to SEE again.\x01",
            "That's great!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x102,
        "#1040FSounds like repairs are going well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x8,
        (
            "#021FEveryone's working hard, that's for\x01",
            "certain.\x02\x03",

            "#525FI need to keep the pace up myself,\x01",
            "to make sure I can keep acting cool\x01",
            "and older-sisterly in front of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#1006FYou're doing fine, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x102,
        (
            "#1040FWe'll proceed with our investigations\x01",
            "with haste.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83BE")

    OP_A2(0x22C4)
    Jump("loc_8431")

    label("loc_83C4")


    ChrTalk(    #360
        0x8,
        (
            "#020FIt should be a bit brighter in here soon.\x02\x03",

            "Repair work is going quite well,\x01",
            "all things considered.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8431")

    Jump("loc_8473")

    label("loc_8434")


    ChrTalk(    #361
        0x8,
        "#020FShall I join the traveling party, then?\x02",
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_8473")

    label("loc_846D")

    Jump("loc_8473")

    label("loc_8470")

    Jump("loc_8473")

    label("loc_8473")

    TalkEnd(0xFE)
    Return()

    # Function_11_7B85 end

    def Function_12_8477(): pass

    label("Function_12_8477")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_22(0x7A, 0x1, 0x50)
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_6D(20, 2000, 97320, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    OP_BB(0x4, 0x1, 0x1D)
    OP_BD()
    SetChrChipByIndex(0xA, 20)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x15, 1630, 250, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetChrPos(0x101, -1840, 2000, 91330, 0)
    SetChrPos(0x102, -750, 2000, 91300, 0)
    SetChrPos(0xB, -190, 2000, 89100, 0)
    SetChrPos(0x14, -2650, 2000, 88000, 0)
    SetChrPos(0x16, -1580, 2000, 87900, 0)
    SetChrPos(0x17, -1170, 2000, 87000, 0)
    SetChrPos(0x13, -2790, 2000, 90230, 0)
    SetChrPos(0x9, -650, 2000, 90170, 0)
    SetChrPos(0x8, -1850, 2000, 89910, 0)
    SetChrPos(0x12, -3280, 2000, 88660, 0)
    SetChrPos(0xA, -2130, 2000, 92320, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)

    def lambda_86DD():

        label("loc_86DD")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_86DD")

    QueueWorkItem2(0x101, 3, lambda_86DD)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #362
        0xC,
        (
            "#176F#2PThat's the stabilizer wings stored.\x02\x03",

            "#178FHelm, accelerate to full speed and\x01",
            "set course for the floating city over\x01",
            "the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xE,
        "#5PYes, ma'am.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x15, 5)
    Sleep(300)

    ChrTalk(    #364
        0x15,
        (
            "#270F#5PWhat shall we do if the enemy\x01",
            "attempts to intercept us?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(200)

    ChrTalk(    #365
        0xC,
        (
            "#176F#2PA good question.\x02\x03",

            "#170FWe may need to engage them\x01",
            "depending on the ferocity of the\x01",
            "attack, but I want to prioritize landfall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x15,
        (
            "#272F#5PUnderstood.\x02\x03",

            "#275FAlso, don't worry about mincing words.\x02\x03",

            "Regardless of our ranks, aboard this\x01",
            "ship, I am your gunnery officer.\x01",
            "I am yours to command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xC,
        "#171F#2PUnderstood.\x02",
    )

    CloseMessageWindow()

    def lambda_8972():
        OP_6D(-650, 2000, 93400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8972)

    def lambda_898A():
        OP_67(0, 5790, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_898A)
    Sleep(100)
    SetChrSubChip(0x15, 3)
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(200)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #368
        0x101,
        (
            "#1004F#2PHuh, I didn't know Mueller could\x01",
            "man an orbalship gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x9,
        (
            "#031FHe trained in the Imperial Army's\x01",
            "most advanced armored division.\x02\x03",

            "Despite his burly, sword-swinging\x01",
            "appearance, he is quite capable as\x01",
            "a gunner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x15,
        (
            "#276F#3P...I'm sorry my appearance doesn't\x01",
            "match my skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        "#1006F#2POh, no, no! That's cool, actually!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #372
        0x101,
        (
            "#1004F#5PAnd, uh, when did you get a chance to\x01",
            "change, Olivi--er, Prince Olivert?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B71():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B71)
    Sleep(50)

    def lambda_8B84():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8B84)
    Sleep(50)

    def lambda_8B97():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8B97)

    def lambda_8BA5():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8BA5)

    def lambda_8BB3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8BB3)
    Sleep(50)

    def lambda_8BC6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8BC6)

    def lambda_8BD4():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8BD4)
    Sleep(400)

    ChrTalk(    #373
        0x102,
        (
            "#1040F#6PI thought you were coming aboard\x01",
            "as a representative of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x9,
        (
            "#031F#2PHa-ha-ha! That, my friends,\x01",
            "was but a front!\x02\x03",

            "#030FHowever, once this is over,\x01",
            "my search for love, freedom, and\x01",
            "finery shall be at an end.\x02\x03",

            "Until then, at least, I wish to dress\x01",
            "and be addressed as I please. To you,\x01",
            "I shall always be Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xB,
        "#071F#2PHaha. Dressing up for the funeral, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x8,
        (
            "#025F#5P*sigh* What would the people\x01",
            "of Erebonia say if they knew...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x9,
        "#035F#2PI cannot say I care in the slightest.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    Sleep(300)

    ChrTalk(    #378
        0x9,
        (
            "#037F#5PHow about it, my good reporters?\x01",
            "Would you care for a scandalous tell-all\x01",
            "interview with an Erebonian prince?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x16,
        "#143FHang on, you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x17,
        (
            "#151FOooooh, I better get lotsa pictures,\x01",
            "then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x15,
        (
            "#274F#3PPlease, I beg you, do not take any of\x01",
            "the nonsense coming from his mouth\x01",
            "seriously.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #382
        0x101,
        (
            "#1016F#5PEr, that aside...\x02\x03",

            "#1015FHow come you two are\x01",
            "coming along, Nial?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F95():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8F95)

    def lambda_8FA3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8FA3)
    Sleep(50)

    def lambda_8FB6():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8FB6)

    def lambda_8FC4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8FC4)

    def lambda_8FD2():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8FD2)
    Sleep(100)

    ChrTalk(    #383
        0xA,
        (
            "#1382F#5PWait, if I may guess: Grandmother wished\x01",
            "for you to ride along as you did during\x01",
            "the incident with the dragon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x16,
        (
            "#141FGot it in one, Your Highness.\x02\x03",

            "Her Majesty put in a good word\x01",
            "for us with Brigadier General Bright.\x02\x03",

            "He allowed us to come along\x01",
            "as war correspondents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x17,
        (
            "#151FI got loooots of pictures of\x01",
            "you being amazing at the gate,\x01",
            "Princess Klaudia. ♪\x02\x03",

            "I'll show you them when they're\x01",
            "developed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xA,
        "#1165F#5PW-Well! Thank you, Dorothy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x12,
        (
            "#551F#5PHow does she\x01",
            "manage to suck the seriousness\x01",
            "out of the room every time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x13,
        "#067F#5PHeehee!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 400)
    Sleep(300)

    ChrTalk(    #389
        0x13,
        (
            "#560F#2POh, yeah! Grandpa, is our\x01",
            "Zero Field Generator okay?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_926D():
        OP_6D(-1680, 2000, 94250, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_926D)

    def lambda_9285():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9285)

    def lambda_9293():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9293)
    Sleep(50)

    def lambda_92A6():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_92A6)

    def lambda_92B4():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_92B4)
    Sleep(50)

    def lambda_92C7():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_92C7)

    def lambda_92D5():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92D5)

    def lambda_92E3():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_92E3)
    Sleep(50)

    def lambda_92F6():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92F6)

    def lambda_9304():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9304)

    def lambda_9312():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9312)
    Sleep(500)
    SetChrSubChip(0x11, 1)
    Sleep(200)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #390
        0x11,
        (
            "#100F#5PYes, it's working fine for the moment.\x02\x03",

            "Assuming nothing happens, it should get\x01",
            "us to that flying city easily enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x14,
        (
            "#1064F#2PEr, one sec.\x02\x03",

            "So if something DOES happen...\x01",
            "all we got is prayers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x11,
        (
            "#104F#5POh, yes. Without the generator, we crash, no\x01",
            "question. The impact would surely kill us all\x01",
            "instantly. Or the subsequent explosion would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x101,
        (
            "#1019F#2PProfessor, you really know how to\x01",
            "calm a girl's fears. Thanks.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(100)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(700)
    SetChrSubChip(0xF, 1)
    Sleep(200)
    SetChrSubChip(0x11, 0)
    Sleep(100)
    SetChrSubChip(0x11, 2)

    ChrTalk(    #394
        0xF,
        "#2PRadar contact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xF,
        "#2PFive ships on an intercept course.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x77)
    Sleep(500)

    def lambda_95E0():
        OP_6D(20, 2000, 97320, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95E0)

    def lambda_95F8():
        OP_67(0, 5160, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_95F8)
    SetChrSubChip(0x15, 4)

    def lambda_9615():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9615)

    def lambda_9623():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9623)
    Sleep(50)

    def lambda_9636():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9636)

    def lambda_9644():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9644)
    Sleep(50)

    def lambda_9657():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9657)

    def lambda_9665():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9665)
    Sleep(50)

    def lambda_9678():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9678)

    def lambda_9686():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9686)
    Sleep(50)

    def lambda_9699():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9699)

    def lambda_96A7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_96A7)
    Sleep(50)

    def lambda_96BA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_96BA)
    SetChrSubChip(0xF, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #396
        0x15,
        "#270F#2PHere they come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x102,
        (
            "#1042FThose look like the high-speed interceptors\x01",
            "that were docked on the Glorious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x11,
        (
            "#102F#5PNot really bothering with stealth at\x01",
            "this point, are they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0xC,
        (
            "#177F#2PArm the main gun and maintain full speed!\x02\x03",

            "#177FTarget only the ships that obstruct our\x01",
            "course! We will focus on breaking through!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #400
        0xE,
        "#1K#4PYes, ma'am!\x02",
    )


    ChrTalk(    #401
        0xF,
        "#1K#1PYes, ma'am.\x02",
    )


    ChrTalk(    #402
        0x10,
        "#1K#5PYes, ma'am!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()
    SetMapFlags(0x2000000)
    OP_A2(0x10FF)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0810   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_12_8477 end

    def Function_13_988F(): pass

    label("Function_13_988F")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_76(0x7, 0x0, 0x1, 0xFFFFFFE2, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x1, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFF9, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_22(0x7A, 0x1, 0x50)
    OP_6D(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    SetChrChipByIndex(0xA, 20)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x15, 1630, 200, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetChrPos(0x101, -1840, 2000, 91330, 0)
    SetChrPos(0x102, -750, 2000, 91300, 0)
    SetChrPos(0xB, -190, 2000, 89100, 0)
    SetChrPos(0x14, -2650, 2000, 88000, 0)
    SetChrPos(0x16, -1580, 2000, 87900, 0)
    SetChrPos(0x17, -1170, 2000, 87000, 0)
    SetChrPos(0x13, -2790, 2000, 90230, 0)
    SetChrPos(0x9, -650, 2000, 90170, 0)
    SetChrPos(0x8, -1850, 2000, 89910, 0)
    SetChrPos(0x12, -3280, 2000, 88660, 0)
    SetChrPos(0xA, -2130, 2000, 92320, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)

    def lambda_9B16():

        label("loc_9B16")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_9B16")

    QueueWorkItem2(0x101, 3, lambda_9B16)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #403
        0xF,
        "#2PBogeys one, two, and five disabled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xF,
        "#2PThree and four are disengaging.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x101,
        "#1018F#2PWe did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0xB,
        "#070F#2PFantastic!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x9,
        (
            "#035F#2PGoodness me. So this is what the\x01",
            "future of aerial warfare looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x15,
        (
            "#277F#6PMmm... The main gun is incredible.\x02\x03",

            "It has quite a bit of power, but virtually\x01",
            "no recoil, even for an orbal weapon.\x01",
            "It's fantastically accurate.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x11, 2)
    Sleep(200)

    ChrTalk(    #409
        0x11,
        (
            "#101F#5PHaha! Of course it is!\x02\x03",

            "#100FTo be honest, I would have liked\x01",
            "to mount some point-defense guns\x01",
            "with radar tracking as well, but...\x02\x03",

            "#104FWell, one project at a time,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(700)
    SetChrSubChip(0xF, 1)
    Sleep(200)
    Sleep(100)

    ChrTalk(    #410
        0xF,
        "#2PRadar conta--oh, Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xF,
        (
            "#2PContact is two-hundred-fifty arge in\x01",
            "length! Approaching at eight o'clock!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x11, 0)

    ChrTalk(    #412
        0x101,
        "#1020F#2PThat could only be...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x14,
        "#1063F#2PAnd here comes the Glorious.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(300)

    ChrTalk(    #414
        0xC,
        (
            "#178F#6PJoshua.\x02\x03",

            "Do you know ANYTHING about\x01",
            "the performance or armament of\x01",
            "that thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x102,
        (
            "#1035FThe Arseille can easily outmaneuver\x01",
            "and outrun it.\x02\x03",

            "#1042FBut it has gigantic main cannons, and\x01",
            "large batteries of point-defense guns.\x02\x03",

            "There's no way we can attack\x01",
            "it directly and live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xC,
        "#176F#6PBlast it...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #417
        0xC,
        (
            "#177F#4PTurn to four o'clock, and FLANK speed!\x02\x03",

            "Lux, get us over the city and avoid\x01",
            "fire from that monster's guns!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xE,
        "#5PAye, aye!\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x3, 0x1, 0xF)
    OP_20(0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT43.dat", 0x0, 0x1)

    label("loc_A119")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A133")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_A130")
    Jump("loc_A133")

    label("loc_A130")

    Jump("loc_A119")

    label("loc_A133")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_6D(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    OP_82(0x0, 0x0)
    OP_20(0x7D0)
    Sleep(1000)
    OP_22(0x7A, 0x1, 0x50)
    FadeToBright(1000, 0)
    OP_0D()
    OP_21()
    Sleep(500)

    ChrTalk(    #419
        0xF,
        (
            "#2PI...think we're out of the Glorious'\x01",
            "firing range.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xA,
        "#1167F#2PWhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x13,
        "#562F#2PThat was scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x8,
        (
            "#025F#2PI think about half the nerves\x01",
            "in my body are now shot, yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x101,
        (
            "#1007F#2PYeeeeah, my heart's about to burst\x01",
            "from my chest.\x02\x03",

            "#1006FStill, there's not much else the enemy\x01",
            "can do to us at this point, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x102,
        "#1042F#2PNo, we shouldn't let our guard down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x12,
        (
            "#057F#2PYeah, the society has a bad\x01",
            "tendency of ignoring stuff like\x01",
            "'common goddamn sense.'\x02\x03",

            "We need to watch out until\x01",
            "the second we land.\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(700)
    SetChrSubChip(0xF, 1)
    Sleep(300)

    ChrTalk(    #426
        0xF,
        (
            "#2PThere's an opening in the clouds ahead!\x02\x03",

            "We are entering the floating\x01",
            "island's airspace!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xC, 0x3, 0x1, 0xF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xF, 0)
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT44.dat", 0x83, 0x1)

    label("loc_A4DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A4F9")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_A4F6")
    Jump("loc_A4F9")

    label("loc_A4F6")

    Jump("loc_A4DF")

    label("loc_A4F9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_6D(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    OP_D2(0x6007C, 0x60081, 0x1D)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x17, 29)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x15, 4)
    OP_82(0x0, 0x0)
    OP_22(0x7A, 0x1, 0x50)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #427
        0xE,
        (
            "#5PWe're now over the flying city, ma'am.\x01",
            "Wow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x101,
        "#1020F#2PHoly Stregas...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xA,
        "#1162F#2PThis is...the jewel of ancient Zemuria.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x14,
        "#1063F#2PEven more mind-blowing than I'd imagined.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x11,
        (
            "#102F#5PHmmmm... Look at that enormous\x01",
            "tower-like structure.\x02\x03",

            "I'd put good money on that being\x01",
            "an important part of the island.\x02\x03",

            "If we're going to land, I'd put down\x01",
            "near that, Captain.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 1)
    Sleep(300)

    ChrTalk(    #432
        0xC,
        (
            "#176F#4PGood idea, Professor.\x02\x03",

            "#178FEcho, anything on radar?\x01",
            "The Glorious?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xF, 1)
    Sleep(300)

    ChrTalk(    #433
        0xF,
        "#2POne moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xF,
        "#2PNo enemy contacts within 50 selge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xF,
        (
            "#2PWe seem to have left the Glorious\x01",
            "in our dust, ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xC,
        "#176F#4PGood.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #437
        0xC,
        (
            "#170F#4PLux, slow to one-third and begin landing.\x01",
            "Put us down near that tower.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0)

    ChrTalk(    #438
        0xE,
        "#5PAye, ma'am.\x02",
    )

    CloseMessageWindow()

    def lambda_A889():
        OP_6D(-420, 2000, 92420, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A889)

    def lambda_A8A1():
        OP_67(0, 5790, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A8A1)
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    WaitChrThread(0x101, 0x1)
    OP_63(0x17)
    Fade(250)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x17, 23)
    OP_0D()
    Sleep(500)

    ChrTalk(    #439
        0x17,
        "#153F#2PHuuuh?\x02",
    )

    CloseMessageWindow()

    def lambda_A901():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A901)

    def lambda_A90F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A90F)
    Sleep(50)

    def lambda_A922():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A922)

    def lambda_A930():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A930)
    Sleep(50)

    def lambda_A943():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A943)

    def lambda_A951():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A951)

    def lambda_A95F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A95F)
    Sleep(50)

    def lambda_A972():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A972)

    def lambda_A980():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A980)
    Sleep(50)

    def lambda_A993():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A993)

    def lambda_A9A1():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A9A1)
    Sleep(400)

    ChrTalk(    #440
        0x101,
        "#1004F#5PDorothy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x16,
        (
            "#142F#5PIf you're out of photo-quartz\x01",
            "already, girl, I swear...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x17,
        (
            "#154F#2POhhh, no, I have plenty of that!\x02\x03",

            "But isn't there something weird\x01",
            "over there?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #443
        0x16,
        "#144F#5PWhat the--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x101,
        "#1020F#5POh, no WAY!\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_ABA3():
        OP_6D(20, 2000, 97320, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABA3)

    def lambda_ABBB():
        OP_67(0, 5160, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ABBB)

    def lambda_ABD3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_ABD3)

    def lambda_ABE1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABE1)

    def lambda_ABEF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_ABEF)
    Sleep(50)

    def lambda_AC02():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AC02)

    def lambda_AC10():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AC10)
    Sleep(50)

    def lambda_AC23():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AC23)
    Sleep(50)

    def lambda_AC36():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AC36)
    Sleep(50)

    def lambda_AC49():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_AC49)
    Sleep(50)

    def lambda_AC5C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AC5C)

    def lambda_AC6A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AC6A)
    SetChrSubChip(0x15, 4)
    SetChrSubChip(0x11, 2)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_21()

    ChrTalk(    #445
        0xC,
        "#173F#2PWhat in the world...?!\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x3, 0x1, 0xF)
    FadeToDark(1200, 0, -1)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0810   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_13_988F end

    def Function_14_ACCD(): pass

    label("Function_14_ACCD")

    EventBegin(0x0)
    OP_D2(0x270009, 0x27000D, 0x1D)
    OP_D2(0x270019, 0x27001D, 0x1E)
    OP_D2(0x70025, 0x7002D, 0x1F)
    OP_D2(0x70035, 0x7003D, 0x20)
    OP_D2(0x70055, 0x7005D, 0x21)
    OP_D2(0x70065, 0x7006D, 0x22)
    OP_D2(0x70075, 0x7007D, 0x23)
    OP_D2(0x270089, 0x27008D, 0x24)
    OP_D2(0x2703A1, 0x2703A5, 0x25)
    OP_D2(0x600AC, 0x600B1, 0x26)
    OP_D2(0x600F2, 0x600F7, 0x27)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_22(0x7A, 0x1, 0x50)
    OP_6D(-340, 2000, 93880, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xA, 20)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x15, 1630, 200, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetChrPos(0xC, -1090, 2000, 93560, 0)
    SetChrPos(0x101, -1840, 2000, 91330, 0)
    SetChrPos(0x102, -750, 2000, 91300, 0)
    SetChrPos(0xB, -190, 2000, 89100, 0)
    SetChrPos(0x14, -2650, 2000, 88000, 0)
    SetChrPos(0x16, -1580, 2000, 87900, 0)
    SetChrPos(0x17, -1170, 2000, 87000, 0)
    SetChrPos(0x13, -2790, 2000, 90230, 0)
    SetChrPos(0x9, -760, 2000, 90170, 0)
    SetChrPos(0x8, -1790, 2000, 89910, 0)
    SetChrPos(0x12, -3280, 2000, 88660, 0)
    SetChrPos(0xA, -2130, 2000, 92320, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_44(0xC, 0x0)
    OP_4A(0xA, 255)
    SetChrChipByIndex(0x101, 29)
    SetChrChipByIndex(0x102, 30)
    SetChrChipByIndex(0x8, 31)
    SetChrChipByIndex(0x9, 32)
    SetChrChipByIndex(0x12, 33)
    SetChrChipByIndex(0x13, 34)
    SetChrChipByIndex(0xB, 35)
    SetChrChipByIndex(0x14, 36)
    SetChrChipByIndex(0xA, 37)
    SetChrChipByIndex(0x16, 38)
    SetChrChipByIndex(0x17, 39)
    OP_22(0x85, 0x0, 0x64)

    def lambda_AF5A():

        label("loc_AF5A")

        OP_7C(0x64, 0x0, 0x3E8, 0xBB8)
        OP_48()
        Jump("loc_AF5A")

    QueueWorkItem2(0x101, 3, lambda_AF5A)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #446
        0x101,
        "#1000F#4PGyaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x102,
        "#1030F...It's him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x11,
        (
            "#100F#2PBlast it all! The left wing is shot!\x02\x03",

            "We're losing the flight field!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0xE,
        "#1PGh, the helm is...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 4)
    Sleep(200)

    ChrTalk(    #450
        0x15,
        "#270FLet me help!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrPos(0x15, 580, 0, 97840, 270)
    SetChrSubChip(0x15, 0)
    SetChrChipByIndex(0x15, 24)
    OP_0D()
    OP_8E(0x15, 0xFFFFF8A8, 0x0, 0x17F2A, 0x1388, 0x0)
    OP_8E(0x15, 0xFFFFF934, 0x0, 0x182E0, 0x1388, 0x0)
    Sleep(1000)

    ChrTalk(    #451
        0xC,
        (
            "#170F#4PAll right...\x02\x03",

            "ALL HANDS, BRACE FOR IMPACT!\x02\x03",

            "Lux, Major!\x01",
            "Land us in one piece!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_23(0x85)
    OP_23(0x7A)
    OP_0D()
    OP_44(0x101, 0x3)
    Sleep(2000)
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT45.dat", 0x0, 0x1)

    label("loc_B121")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B13B")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_B138")
    Jump("loc_B13B")

    label("loc_B138")

    Jump("loc_B121")

    label("loc_B13B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_AD(0x2400AC, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_22(0x85, 0x0, 0x64)
    Sleep(3000)
    OP_23(0x85)
    OP_A2(0x10FF)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_ACCD end

    def Function_15_B193(): pass

    label("Function_15_B193")

    OP_24(0x7A, 0x46)
    Sleep(200)
    OP_24(0x7A, 0x3C)
    Sleep(200)
    OP_24(0x7A, 0x32)
    Sleep(200)
    OP_24(0x7A, 0x28)
    Sleep(200)
    OP_24(0x7A, 0x1E)
    Sleep(200)
    OP_24(0x7A, 0x14)
    Sleep(200)
    OP_23(0x7A)
    Return()

    # Function_15_B193 end

    def Function_16_B1CD(): pass

    label("Function_16_B1CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x7A)
    OP_D2(0x270009, 0x27000D, 0x5)
    OP_D2(0x70065, 0x7006D, 0x6)
    OP_D2(0x26015F, 0x260164, 0x1D)
    OP_D2(0x270019, 0x27001D, 0x1E)
    OP_D2(0x70025, 0x7002D, 0x1F)
    OP_D2(0x70035, 0x7003D, 0x20)
    OP_D2(0x2703A1, 0x2703A5, 0x21)
    OP_D2(0x70055, 0x7005D, 0x22)
    OP_D2(0x26001F, 0x260024, 0x23)
    OP_D2(0x70075, 0x7007D, 0x24)
    OP_D2(0x270089, 0x27008D, 0x25)
    OP_D2(0x600AC, 0x600B1, 0x26)
    OP_D2(0x2600AA, 0x2600AF, 0x27)
    OP_D2(0x600CC, 0x600D1, 0x28)
    OP_D2(0x60035, 0x6003A, 0x29)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 29)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 30)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 32)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 33)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 34)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 35)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 36)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x14, 37)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x16, 38)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x17, 39)
    SetChrFlags(0x11, 0x2)
    SetChrSubChip(0x11, 24)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x15, 0x2)
    SetChrSubChip(0x15, 24)
    SetChrChipByIndex(0x15, 19)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xC, 4)
    SetChrFlags(0xE, 0x2)
    SetChrSubChip(0xE, 24)
    SetChrChipByIndex(0xE, 10)
    SetChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 24)
    SetChrChipByIndex(0xF, 8)
    SetChrFlags(0x10, 0x2)
    SetChrSubChip(0x10, 24)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(790, 2000, 90690, 0)
    OP_67(0, 6200, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0xC, 0x0)
    OP_4A(0xA, 255)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x40)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x16, 1300, 2000, 88300, 90)
    SetChrPos(0x17, 2000, 1900, 87630, 180)
    SetChrPos(0xC, -1960, 2000, 93000, 180)
    SetChrPos(0xA, -2110, 2000, 92110, 0)
    SetChrPos(0x9, 0, 2000, 88300, 0)
    SetChrPos(0x8, -1200, 2000, 88440, 45)
    SetChrPos(0x13, -2800, 2000, 89500, 90)
    SetChrPos(0x12, -2600, 2000, 88360, 0)
    SetChrPos(0xB, -2100, 2000, 86560, 0)
    SetChrPos(0x101, -300, 1500, 90550, 270)
    SetChrPos(0x102, -400, 2000, 91290, 180)
    SetChrPos(0x14, 600, 2000, 90100, 270)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x800)
    ClearChrFlags(0x101, 0x1)
    SetChrSubChip(0x101, 4)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x15, 1630, 200, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetMessageWindowPos(150, 100, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(    #452
        (
            "\x07\x00...telle...\x02\x03",

            "Es...le...ake...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 120, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(    #453
        "\x07\x00...u okay...elle...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 200, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #454
        "\x07\x00#1003FNnnn...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0x101, 7)
    Sleep(500)

    ChrTalk(    #455
        0x101,
        "#1004F#6POoh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x14,
        "#1062F#4PAh, good, you're awake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x102,
        "#1043F#3PAre you all right? Are you hurt?\x02",
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xBB8)
    SetChrSubChip(0x101, 5)
    Sleep(700)

    ChrTalk(    #458
        0x101,
        "#1013F#4PNo, I...think I'm fine...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrPos(0x101, -340, 2000, 90400, 270)
    SetChrFlags(0x101, 0x1)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    OP_8C(0x101, 270, 0)
    OP_0D()
    Sleep(300)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(250)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 45, 400)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    OP_0D()
    Fade(250)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x14, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #459
        0x101,
        (
            "#1025F#6PBanged my elbow, but...yeah, I'm okay.\x02\x03",

            "#1003FBut everyone else...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B732():
        OP_6D(-230, 2000, 89260, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B732)

    def lambda_B74A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B74A)
    Sleep(100)

    def lambda_B75D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B75D)
    Sleep(100)

    def lambda_B770():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B770)
    WaitChrThread(0x101, 0x1)
    OP_9E(0x12, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_0D()
    Sleep(300)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #460
        0x12,
        "#552F#5PI'm...not dead, at least. Ugh...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x13, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(250)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 6)
    OP_8C(0x13, 90, 0)
    OP_0D()
    Sleep(300)
    OP_9E(0x13, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(250)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 16)
    OP_8C(0x13, 90, 0)
    OP_0D()

    ChrTalk(    #461
        0x13,
        "#562F#1POwwwwww...\x02",
    )

    CloseMessageWindow()
    OP_9E(0xA, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 20)
    TurnDirection(0x13, 0x101, 400)
    OP_0D()
    OP_8C(0xA, 180, 400)
    Sleep(200)
    OP_8C(0xC, 180, 400)

    ChrTalk(    #462
        0xA,
        "#1381FI'm... I'm fine.\x02",
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xBB8)
    Fade(250)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    Sleep(300)
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(    #463
        0x9,
        (
            "#034FWell...that was thrilling,\x01",
            "if nothing else.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x4)
    OP_0D()
    Sleep(300)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #464
        0x8,
        (
            "#025F#6PYou remember the other half of my nerves?\x01",
            "They're all quite gone now, thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xB, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    ClearChrFlags(0xB, 0x4)
    OP_0D()
    Sleep(500)

    ChrTalk(    #465
        0xB,
        (
            "#572F#2PThat's the closest I've ever brushed\x01",
            "shoulders with death, I think...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0xFFFFFED4, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #466
        0x17,
        (
            "#151F#6P...Eheeheeeee...\x02\x03",

            "Nooo, nooo, I can't eat that muuuuch...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x96, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #467
        0x16,
        (
            "#145F#6PFor the... Guess I oughtta be grateful\x01",
            "she ain't hurt...\x02\x03",

            "#144FDOROTHY! Wake up, naptime's over!\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x17, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(500)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x17, 23)
    SetChrPos(0x17, 2430, 2000, 87860, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(    #468
        0x17,
        "#153F#4P*yaaaawn* ...Nial...?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x16, 22)
    TurnDirection(0x16, 0x17, 0)
    OP_0D()
    Sleep(300)

    def lambda_BB86():
        OP_6D(-1070, 2000, 94550, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BB86)

    def lambda_BB9E():
        OP_67(0, 6250, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB9E)

    def lambda_BBB6():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BBB6)
    OP_8C(0xC, 0, 200)
    OP_8E(0xC, 0xFFFFF880, 0x7D0, 0x170AC, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #469
        0xC,
        "#178F#7PMajor Vander, how about you?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x15, 0x2)
    SetChrSubChip(0x15, 2)
    SetChrChipByIndex(0x15, 19)
    OP_0D()
    Sleep(300)

    ChrTalk(    #470
        0x15,
        "#272F#6P...As well as can be expected.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_9E(0x11, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    ClearChrFlags(0x11, 0x2)
    SetChrSubChip(0x11, 1)
    OP_0D()
    Sleep(300)

    ChrTalk(    #471
        0x11,
        "#102F#5PNothing...SEEMS broken over here.\x02",
    )

    CloseMessageWindow()
    OP_9E(0xF, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    ClearChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 8)
    OP_0D()
    SetChrSubChip(0xF, 1)
    Sleep(300)

    ChrTalk(    #472
        0xF,
        "#2PI'm...unhurt, ma'am.\x02",
    )

    CloseMessageWindow()
    OP_9E(0xE, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    ClearChrFlags(0xE, 0x2)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 10)
    OP_0D()
    SetChrSubChip(0xE, 1)
    Sleep(300)

    ChrTalk(    #473
        0xE,
        "#5PThink I'm okay...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x10, 0xF, 0x0, 0x1F4, 0xBB8)
    Fade(250)
    ClearChrFlags(0x10, 0x2)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 9)
    OP_0D()
    SetChrSubChip(0x10, 2)
    Sleep(300)

    ChrTalk(    #474
        0x10,
        "#6PI thought we were goners!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #475
        0xC,
        (
            "#176F#7PA real miracle.\x02\x03",

            "#175FOr perhaps...he simply let us live.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #476
        0x101,
        "#1020F#5PThat's right!\x02",
    )

    CloseMessageWindow()

    def lambda_BE2A():
        OP_6D(130, 2000, 91180, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE2A)

    def lambda_BE42():
        OP_67(0, 5740, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE42)

    def lambda_BE5A():
        OP_6B(3300, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BE5A)

    def lambda_BE6A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BE6A)
    Sleep(50)

    def lambda_BE7D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE7D)
    Sleep(50)

    def lambda_BE90():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BE90)
    Sleep(50)

    def lambda_BEA3():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_BEA3)
    Sleep(50)

    def lambda_BEB6():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_BEB6)
    Sleep(50)
    OP_8C(0xC, 180, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #477
        0x101,
        "#1020F#7PThe one riding that thing, that was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0x102,
        (
            "#1035F#6PYes.\x02\x03",

            "#1042FIt was Loewe. No doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x12,
        "#057F#5PSon of a...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xB,
        (
            "#074F#2PIn that case, I'm certain he\x01",
            "stayed his hand.\x02\x03",

            "#072FIf he really wished to, he could\x01",
            "have torn us to pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x101,
        "#1007F#7PKiiiinda not sure how to feel about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x102,
        "#1043F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #483
        0xA,
        "#1163F#6PAt... At any rate, where are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0xC,
        (
            "#176F#6PIt looks to be somewhere on\x01",
            "the periphery of the island.\x02\x03",

            "#178FWe should step out and take\x01",
            "stock of our situation.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5900   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_16_B1CD end

    def Function_17_C0F3(): pass

    label("Function_17_C0F3")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_22(0x7A, 0x1, 0x50)
    OP_6F(0xC, 0)
    OP_6D(1350, 2000, 100510, 0)
    OP_67(0, 5430, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0x15, 19)
    SetChrChipByIndex(0xA, 20)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x15, 1630, 200, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xA, -2130, 2000, 92320, 0)
    SetChrPos(0x13, -1810, 2000, 91450, 0)
    SetChrPos(0x8, -420, 2000, 91880, 0)
    SetChrPos(0x12, -2780, 2000, 90100, 0)
    SetChrPos(0x9, 90, 2000, 90050, 0)
    SetChrPos(0x14, -1020, 2000, 90470, 0)
    SetChrPos(0xB, -2200, 2000, 88980, 0)
    SetChrPos(0x16, -990, 2000, 88600, 0)
    SetChrPos(0x17, 100, 2000, 88430, 0)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 9)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_44(0xC, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x17, 0x0)
    OP_44(0x10, 0x0)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x15, 255)
    SetChrSubChip(0x15, 1)
    SetChrSubChip(0x10, 1)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0xF, 2)
    OP_76(0x7, 0x0, 0x1, 0xFFFFFFF7, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x1, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)

    def lambda_C304():
        OP_6D(670, 2000, 94500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C304)

    def lambda_C31C():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C31C)

    def lambda_C334():
        OP_6B(3420, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C334)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #485
        0x8,
        "#023F#5PIt... It can't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x14,
        "#1067F#5PWe didn't make it in time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x12,
        "#055F#5PNo frickin' way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0x13,
        "#065F#5PNo... Nooo...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x13, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #489
        0x13,
        "#069F#5P#3SNOOOOOOOOOOOOOOO!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #490
        0xA,
        (
            "#1166F#5PJULIA! PLEASE!\x02\x03",

            "It looks like the escape tunnels lead to\x01",
            "the northwestern edge of the island!\x02\x03",

            "Take the Arseille there at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0xC,
        (
            "#175F#2PForgive me, Your Highness...\x02\x03",

            "Even on your orders...I cannot do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x15,
        (
            "#272F#6PThe Arseille doesn't have full\x01",
            "engine power back.\x02\x03",

            "If we get close to the city, especially\x01",
            "under it, we could not escape the\x01",
            "island's collapse.\x02\x03",

            "#276FIs that about right, Professor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0x11,
        "#102F#5P...You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0xA,
        "#1169F#5PNo... No, no no no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x9,
        (
            "#034F#5PHow terrible...\x02\x03",

            "It feels like I should say something,\x01",
            "but...what do you say to such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0xB,
        "#572F#5PThere are no words, I think.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0x16,
        (
            "#145F#5PThose two... Damn it!\x02\x03",

            "They were just getting started...\x01",
            "and now they're done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x17,
        "#156F#2POooooh, Esteeeeelle... Joshuaaaa...\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #499
        0x17,
        "#153FHuuuuh?\x02",
    )

    CloseMessageWindow()

    def lambda_C75D():
        OP_6D(890, 2000, 93900, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C75D)

    def lambda_C775():
        OP_67(0, 5800, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C775)

    def lambda_C78D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C78D)
    Sleep(50)

    def lambda_C7A0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C7A0)
    Sleep(50)

    def lambda_C7B3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C7B3)
    Sleep(50)

    def lambda_C7C6():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C7C6)
    Sleep(50)

    def lambda_C7D9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C7D9)
    Sleep(50)

    def lambda_C7EC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C7EC)
    Sleep(50)

    def lambda_C7FF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C7FF)
    Sleep(50)
    OP_8C(0x16, 90, 400)
    Sleep(500)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #500
        0x16,
        (
            "#142F#5PCome ON, Dorothy...\x02\x03",

            "Try and show a little decorum\x01",
            "at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0x17,
        (
            "#150F#2PBut, um!\x02\x03",

            "#151FI just noticed that Sieg is flying\x01",
            "around looking awfully happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0x16,
        "#143F#5PHuh?\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #503
        0xC,
        "#173F#2POh...\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_C91B():
        OP_6D(1350, 2000, 100510, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C91B)

    def lambda_C933():
        OP_67(0, 4000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C933)

    def lambda_C94B():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C94B)

    def lambda_C95B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C95B)
    Sleep(50)

    def lambda_C96E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C96E)
    Sleep(50)

    def lambda_C981():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C981)
    Sleep(50)

    def lambda_C994():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C994)
    Sleep(50)

    def lambda_C9A7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C9A7)
    Sleep(50)

    def lambda_C9BA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C9BA)
    Sleep(50)

    def lambda_C9CD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C9CD)
    Sleep(50)
    OP_8C(0x16, 0, 400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10FC)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_C0F3 end

    def Function_18_C9FC(): pass

    label("Function_18_C9FC")

    SetChrChipByIndex(0x18, 30)
    SetChrChipByIndex(0x19, 30)
    SetChrChipByIndex(0x1A, 30)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrSubChip(0x1A, 0)
    OP_4A(0x18, 0)
    OP_4A(0x19, 0)
    OP_4A(0x1A, 0)
    Sleep(2000)
    SetChrChipByIndex(0x18, 27)
    SetChrChipByIndex(0x19, 27)
    SetChrChipByIndex(0x1A, 27)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrSubChip(0x1A, 0)
    OP_4B(0x18, 0)
    OP_4B(0x19, 0)
    OP_4B(0x1A, 0)
    Return()

    # Function_18_C9FC end

    def Function_19_CA56(): pass

    label("Function_19_CA56")

    EventBegin(0x0)
    OP_4A(0xC, 255)
    OP_4A(0x15, 255)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0xA, 0)
    SetChrPos(0xC, -1810, 2000, 90510, 180)
    SetChrPos(0x15, -580, 2000, 90700, 180)
    SetChrPos(0x101, -2080, 2000, 88160, 0)
    SetChrPos(0x102, -820, 2000, 88110, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAF3")
    SetChrPos(0xF8, -3320, 2000, 88590, 90)
    SetChrPos(0xF9, -1560, 2000, 86680, 0)
    Jump("loc_CB58")

    label("loc_CAF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB25")
    SetChrPos(0xF8, -1560, 2000, 86680, 0)
    SetChrPos(0xF9, -3320, 2000, 88590, 90)
    Jump("loc_CB58")

    label("loc_CB25")

    SetChrPos(0xF8, -2300, 2000, 86650, 0)
    SetChrPos(0xF9, -680, 2000, 86590, 0)
    SetChrPos(0xA, -3320, 2000, 88590, 90)

    label("loc_CB58")

    OP_6D(30, 1650, 90010, 0)
    OP_67(0, 4500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(258, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #504
        0xC,
        "#176F#3PHmm. I see.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC21")

    ChrTalk(    #505
        0x102,
        (
            "#1042F#4PYes, we're just about ready to begin\x01",
            "our investigation of the Axis Pillar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC6E")

    label("loc_CC21")


    ChrTalk(    #506
        0x102,
        (
            "#1042F#4PYes, we've been investigating inside\x01",
            "the Axis Pillar a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC6E")


    ChrTalk(    #507
        0x15,
        (
            "#272F#6PSo we were right, that tower is the central\x01",
            "administrative facility for the entire city.\x02\x03",

            "#270FIt must be where the Aureole is stored...\x01",
            "and the enemy must be there as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xC,
        (
            "#176F#3PVery well, then.\x02\x03",

            "#178FI will join your investigation,\x01",
            "if you'll have me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDA7")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CDE5")

    label("loc_CDA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDCE")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CDE5")

    label("loc_CDCE")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CDE5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE11")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CE4F")

    label("loc_CE11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE38")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CE4F")

    label("loc_CE38")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CE4F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE89")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CEC7")

    label("loc_CE89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEB0")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CEC7")

    label("loc_CEB0")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CEC7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEF3")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CF31")

    label("loc_CEF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF1A")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CF31")

    label("loc_CF1A")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CF31")

    Jump("loc_D01F")

    label("loc_CF34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF5B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CF99")

    label("loc_CF5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF82")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CF99")

    label("loc_CF82")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CF99")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFC5")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D003")

    label("loc_CFC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFEC")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D003")

    label("loc_CFEC")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D003")

    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D01F")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D03C")
    OP_8C(0x105, 45, 400)
    Jump("loc_D043")

    label("loc_D03C")

    OP_8C(0xA, 45, 400)

    label("loc_D043")


    ChrTalk(    #509
        0x101,
        "#1004F#6PEr, what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0xC,
        (
            "#170F#3PI want to get a picture of the\x01",
            "situation with my own eyes.\x02\x03",

            "#176FBesides...it sounds like the Axis Pillar\x01",
            "allows them to manipulate city functions\x01",
            "as they wish.\x02\x03",

            "#178FAs skilled as you've all become, I think\x01",
            "you could use all the help you can get\x01",
            "against that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1BB")

    ChrTalk(    #511
        0x105,
        (
            "#1164F#5PBut, Julia, what about the\x01",
            "Arseille's repairs?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1F8")

    label("loc_D1BB")


    ChrTalk(    #512
        0xA,
        (
            "#1164F#5PBut, Julia, what about the\x01",
            "Arseille's repairs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1F8")

    OP_8C(0xC, 215, 400)

    ChrTalk(    #513
        0xC,
        (
            "#171F#3PDon't worry, Your Highness. Most of\x01",
            "the serious work is complete.\x02\x03",

            "#170FI've already ordered the flight engine test.\x02\x03",

            "With that, the professor and the crew can\x01",
            "manage what little remains, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0x101,
        (
            "#1011F#6PWell, okay...\x02\x03",

            "#1006FI sure won't say no to the extra help!\x01",
            "Glad to have you, Julia!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x15)
    Sleep(300)

    ChrTalk(    #515
        0x15,
        (
            "#270F#6POn that note, then, allow me to\x01",
            "accompany you as well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3BE")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D3FC")

    label("loc_D3BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E5")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D3FC")

    label("loc_D3E5")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D3FC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D428")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D466")

    label("loc_D428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D44F")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D466")

    label("loc_D44F")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D466")

    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D567")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4BC")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D4FA")

    label("loc_D4BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4E3")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D4FA")

    label("loc_D4E3")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D4FA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D526")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D564")

    label("loc_D526")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D54D")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D564")

    label("loc_D54D")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D564")

    Jump("loc_D652")

    label("loc_D567")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D58E")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D5CC")

    label("loc_D58E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5B5")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D5CC")

    label("loc_D5B5")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D5CC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5F8")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D636")

    label("loc_D5F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D636")

    label("loc_D61F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D636")

    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D652")

    Sleep(500)
    OP_8C(0xC, 90, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D67C")

    ChrTalk(    #516
        0x104,
        "#33F#2POh?\x02",
    )

    CloseMessageWindow()

    label("loc_D67C")


    ChrTalk(    #517
        0xC,
        "#173F#3PMajor Vander?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0x15,
        (
            "#272F#6PThe perimeter here is as secure\x01",
            "as we can reasonably make it.\x02\x03",

            "Realistically, there's very little left\x01",
            "for me to do here.\x02\x03",

            "#277FA soldier should go where his skills\x01",
            "are most needed. Don't you agree?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D874")

    ChrTalk(    #519
        0x104,
        (
            "#31F#2PHmmm... I see.\x02\x03",

            "#37FYou'd feel a bit lonely with Julia leaving,\x01",
            "my friend. Her prowess does shine like the\x01",
            "sun. I understand. You may pursue your heart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0x15,
        (
            "#276F#6PJust who do you think I came along\x01",
            "for in the first place, you idiot?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D958")

    label("loc_D874")


    ChrTalk(    #521
        0xC,
        "#172F#3PMajor, we can't possibly both--\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 270, 400)

    ChrTalk(    #522
        0x15,
        (
            "#277F#4PYou don't need to worry yourself,\x01",
            "Captain.\x02\x03",

            "To be honest, my main concern is allowing\x01",
            "a certain imbecile to wander around\x01",
            "unsupervised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0xC,
        "#170F#3PHeh... I see.\x02",
    )

    CloseMessageWindow()

    label("loc_D958")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D96D")
    OP_8C(0x15, 180, 400)

    label("loc_D96D")


    ChrTalk(    #524
        0x15,
        (
            "#277F#6PRegardless.\x02\x03",

            "The offer stands. I will gladly\x01",
            "help you if you need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0x101,
        "#1006F#6PWe'll keep that in mind!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0x102,
        "#1040F#4PThank you, Captain, Major.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0x15, 130, 2000, 91480, 0)
    SetChrPos(0x101, -1130, 2000, 87700, 180)
    SetChrPos(0x102, -1130, 2000, 87700, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA97")
    SetChrPos(0xF8, -1130, 2000, 87700, 180)
    SetChrPos(0xF9, -1130, 2000, 87700, 180)
    Jump("loc_DACA")

    label("loc_DA97")

    SetChrPos(0xF8, -1130, 2000, 87700, 180)
    SetChrPos(0xF9, -1130, 2000, 87700, 180)
    SetChrPos(0xA, -910, 2000, 89640, 0)

    label("loc_DACA")

    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0xA, 0)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_6D(-1130, 2000, 87700, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x22D6)
    OP_31(0xE, 0x0, 0x55)
    OP_31(0xE, 0xFE, 0x0)
    OP_41(0xE, 0x87, 0xFF)
    OP_41(0xE, 0x107, 0xFF)
    OP_41(0xE, 0x128, 0xFF)
    OP_35(0xE, 0x0)
    OP_BB(0xE, 0x6, 0x11A)
    OP_37(0xE, 0x80, 0x3)
    OP_37(0xE, 0x81, 0x3)
    OP_37(0xE, 0x82, 0x2)
    OP_37(0xE, 0x83, 0x3)
    OP_37(0xE, 0x84, 0x2)
    OP_37(0xE, 0x85, 0x2)
    OP_37(0xE, 0x86, 0x2)
    OP_41(0xE, 0x276, 0x0)
    OP_41(0xE, 0x275, 0x1)
    OP_41(0xE, 0x2CB, 0x3)
    OP_41(0xE, 0x294, 0x4)
    OP_41(0xE, 0x29A, 0x5)
    OP_41(0xE, 0x2A2, 0x6)
    OP_31(0xF, 0x0, 0x56)
    OP_31(0xF, 0xFE, 0x0)
    OP_41(0xF, 0xA5, 0xFF)
    OP_41(0xF, 0x107, 0xFF)
    OP_41(0xF, 0x128, 0xFF)
    OP_35(0xF, 0x0)
    OP_BB(0xF, 0x6, 0x114)
    OP_37(0xF, 0x80, 0x2)
    OP_37(0xF, 0x81, 0x3)
    OP_37(0xF, 0x82, 0x2)
    OP_37(0xF, 0x83, 0x2)
    OP_37(0xF, 0x84, 0x2)
    OP_37(0xF, 0x85, 0x3)
    OP_37(0xF, 0x86, 0x3)
    OP_41(0xF, 0x294, 0x0)
    OP_41(0xF, 0x275, 0x1)
    OP_41(0xF, 0x298, 0x2)
    OP_41(0xF, 0x2D7, 0x3)
    OP_41(0xF, 0x272, 0x4)
    OP_41(0xF, 0x29A, 0x5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_19_CA56 end

    SaveToFile()

Try(main)
