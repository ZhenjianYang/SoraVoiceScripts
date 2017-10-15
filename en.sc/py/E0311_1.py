from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0311_1 ._SN',
        MapName             = 'Event',
        Location            = 'E0311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0311   ._SN',
            'ED6_DT21/E0311_1 ._SN',
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
        "Function_2_152A",         # 02, 2
        "Function_3_2C16",         # 03, 3
        "Function_4_3F5F",         # 04, 4
        "Function_5_45A6",         # 05, 5
        "Function_6_4A53",         # 06, 6
        "Function_7_5F20",         # 07, 7
        "Function_8_6151",         # 08, 8
        "Function_9_6300",         # 09, 9
        "Function_10_6432",        # 0A, 10
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD")
    TalkBegin(0xFE)
    Jump("loc_1B4")

    label("loc_BD")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D")
    Jump("loc_18F")

    label("loc_14D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_169")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F")

    label("loc_169")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_185")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F")

    label("loc_185")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18F")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    label("loc_1B4")

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
        (0, "loc_217"),
        (1, "loc_14D0"),
        (2, "loc_1509"),
        (SWITCH_DEFAULT, "loc_150C"),
    )


    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_956")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52F")
    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #0
        0x8,
        (
            "#021FOho! That's a familiar face.\x02\x03",

            "#021FI never had imagined we'd meet\x01",
            "again in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10B,
        (
            "#214FThat is totally MY line!\x02\x03",

            "Sheesh, what is it with you and that whip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#027FOh, I was just playing with you\x01",
            "back then, dear.\x02\x03",

            "#525FIf you like, I could be a bit...\x01",
            "rougher next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10B,
        (
            "#216FNgaaah, why does it sound like you\x01",
            "aren't actually joking...?\x02\x03",

            "#413FA-Anyway... given where we are, I'm\x01",
            "willing to bury the hatchet. And the whip.\x01",
            "(Please, bury the whip.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#020FAs much as a little part of me would\x01",
            "enjoy it, whipping each other only serves\x01",
            "Ouroboros' interests, yes.\x02\x03",

            "I'm perfectly willing to consider the\x01",
            "hatchet six feet under.\x02\x03",

            "I'll be looking forward to seeing what\x01",
            "you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10B,
        "#210FHeh. Just you wait!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 0)
    OP_A2(0x8)
    OP_A2(0x22A0)
    Jump("loc_953")

    label("loc_52F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C8")
    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #6
        0x8,
        (
            "#020FI agree. Given where we are, the past\x01",
            "is water under the bridge.\x02\x03",

            "Let's stand together against the Society.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 0)
    Jump("loc_953")

    label("loc_5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_81C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_734")

    ChrTalk(    #7
        0x8,
        (
            "#027FIf we can get the left engine back in place,\x01",
            "the repairs will be more or less done.\x02\x03",

            "So, meanwhile, those of us who can't lift\x01",
            "engines are basically stuck sitting on\x01",
            "our hands until it's done.\x02\x03",

            "#026FHopefully we'll be ready to fly by the\x01",
            "time you come back...\x02\x03",

            "#525FAll we can do for now, though, is trust\x01",
            "in Professor Russell, hmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_819")

    label("loc_734")


    ChrTalk(    #8
        0x8,
        (
            "#027FIf we can get the left engine back in place,\x01",
            "the repairs will be more or less done.\x02\x03",

            "Hopefully we'll be ready to fly by the\x01",
            "time you come back...\x02\x03",

            "#525FAll we can do for now, though, is trust\x01",
            "in Professor Russell, hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_819")

    Jump("loc_953")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F9")

    ChrTalk(    #9
        0x8,
        (
            "#020FAhh, the lights are back on, at least.\x02\x03",

            "That will hopefully help repairs go faster,\x01",
            "since we aren't bumbling around in the\x01",
            "dark any longer.\x02\x03",

            "Right, then. I'd best find something else\x01",
            "to help with.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_953")

    label("loc_8F9")


    ChrTalk(    #10
        0x8,
        (
            "#020FWe finally have the lights back on.\x02\x03",

            "That'll help repairs go faster, hopefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_953")

    Jump("loc_14CD")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_CBC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C31")

    ChrTalk(    #11
        0x8,
        (
            "#020FI never had imagined we'd meet\x01",
            "again in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10B,
        (
            "#210FThat is totally MY line!\x02\x03",

            "Sheesh, what is it with you and that whip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#020FOh, I was just playing with you\x01",
            "back then, dear.\x02\x03",

            "If you like, I could be a bit...\x01",
            "rougher next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10B,
        (
            "#210FNgaaah, why does it sound like you\x01",
            "aren't actually joking...?\x02\x03",

            "A-Anyway... given where we are, I'm\x01",
            "willing to bury the hatchet. And the whip.\x01",
            "(Please, bury the whip.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#020FAs much as a little part of me would\x01",
            "enjoy it, whipping each other only serves\x01",
            "Ouroboros' interests, yes.\x02\x03",

            "I'm perfectly willing to consider the\x01",
            "hatchet six feet under.\x02\x03",

            "I'll be looking forward to seeing what\x01",
            "you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10B,
        "#210FHeh. Just you wait!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x22A0)
    Jump("loc_CB9")

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_CB1")

    ChrTalk(    #17
        0x8,
        (
            "#020FI agree. Given where we are, the past\x01",
            "is water under the bridge.\x02\x03",

            "Let's stand together against the Society.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB9")

    label("loc_CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB9")

    label("loc_CB9")

    Jump("loc_14CD")

    label("loc_CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_CC6")
    Jump("loc_14CD")

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_121F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1154")

    ChrTalk(    #18
        0x8,
        (
            "#026FOnly one tower left, hmm...?\x02\x03",

            "We still don't know what the enemy is\x01",
            "trying to accomplish, but it's clear\x01",
            "we're nearly finished... for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1002FYeah... I guess that's enough,\x01",
            "but, still...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E52")

    ChrTalk(    #20
        0x106,
        (
            "#050FWe can figure out what those clowns were\x01",
            "trying to do once we beat 'em to a pulp.\x02\x03",

            "For now, let's get over to that last\x01",
            "tower and put a stop to 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_E52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE6")

    ChrTalk(    #21
        0x108,
        (
            "#070FAh, right now I don't think we need to\x01",
            "worry about their plans.\x02\x03",

            "It will be enough to simply put a stop to\x01",
            "them for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_EE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA1")

    ChrTalk(    #22
        0x109,
        (
            "#1060FDon'cha think it's a little early to be sweatin'\x01",
            "the details of their big, sinister plan?\x02\x03",

            "Right now I'm cool with just cruising\x01",
            "over there and stopping them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_FA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1047")

    ChrTalk(    #23
        0x105,
        (
            "#042FI believe we can set aside the question\x01",
            "of their motivations for the moment.\x02\x03",

            "For now, it will be enough to simply put\x01",
            "a stop to their plans.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1047")


    ChrTalk(    #24
        0x8,
        (
            "#020FYes, you're right. We can worry about\x01",
            "the big picture a little later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1035FWhat we need to do now is act with haste...\x01",
            "or we may regret hesitating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1015FThe final tower, huh...\x02\x03",

            "#1002FEspecially with Renne there,\x01",
            "we'll need to stay focused.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E4A)
    Jump("loc_121C")

    label("loc_1154")


    ChrTalk(    #27
        0x8,
        (
            "#026FOnly one tower left, hmm...?\x02\x03",

            "#022FWe still don't know what the enemy is\x01",
            "trying to accomplish, but it's clear\x01",
            "we're nearly finished... for now.\x02\x03",

            "Good luck, everyone, but stay on\x01",
            "your guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121C")

    Jump("loc_14CD")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_1229")
    Jump("loc_14CD")

    label("loc_1229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_14CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146C")

    ChrTalk(    #28
        0x8,
        (
            "#020FSo, it's Zin's turn to shine, hmm?\x02\x03",

            "#025F*Sigh* Now I have no one to drink with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x108,
        (
            "#071FHaha, sorry! I'll be glad to join you\x01",
            "once I get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1019FI know we aren't quite in 'super-crisis oh,\x01",
            "Goddess, we're all gonna die' mode yet,\x01",
            "but... Schera? Please don't drink TOO much.\x02\x03",

            "We might need you for something,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#525FHeehee! Don't worry about me.㈱\x02\x03",

            "I'm hardly going to get drunk on\x01",
            "just wine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1016FThat's... nnnnot really what I meant...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#1048FWhy do I feel as though we're having\x01",
            "two different conversations...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E49)
    Jump("loc_14CD")

    label("loc_146C")


    ChrTalk(    #34
        0x8,
        (
            "#020FWell, go on, and be careful.\x02\x03",

            "I'll be here, so if you need my help,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CD")

    Jump("loc_150F")

    label("loc_14D0")


    ChrTalk(    #35
        0x8,
        "#020FShall I join the traveling party, then?\x02",
    )

    CloseMessageWindow()
    Call(0, 5)
    Jump("loc_150F")

    label("loc_1509")

    Jump("loc_150F")

    label("loc_150C")

    Jump("loc_150F")

    label("loc_150F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1521")
    TalkEnd(0xFE)
    Jump("loc_1529")

    label("loc_1521")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_1529")

    Return()

    # Function_1_AB end

    def Function_2_152A(): pass

    label("Function_2_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_2165")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15C1")
    Jump("loc_1603")

    label("loc_15C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15DD")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1603")

    label("loc_15DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15F9")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1603")

    label("loc_15F9")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1603")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
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
        (0, "loc_168B"),
        (1, "loc_2112"),
        (2, "loc_2154"),
        (SWITCH_DEFAULT, "loc_2157"),
    )


    label("loc_168B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 2)), scpexpr(EXPR_END)), "loc_1C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(    #36
        0x9,
        (
            "#031FAh, my compatriots!\x02\x03",

            "It seems you defeated a certain Phantom\x01",
            "Thief most magnificently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1002FYeah... somehow.\x02\x03",

            "#1007FIn the end, he ran away like always,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#1040FStill, our victory was decisive.\x02\x03",

            "I don't think we need to fear any further\x01",
            "interference from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "#035FHeh. He may be a foe, but I must applaud\x01",
            "his perfect withdrawal.\x02\x03",

            "I am certain we shall clash again,\x01",
            "someday, however.\x02\x03",

            "After all! There are words he and I must\x01",
            "settle. We must arrive at a true\x01",
            "definition of beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1015FWell, if you want to, go ahead, I guess...\x02\x03",

            "#1019FJust try not to get anyone else stuck\x01",
            "in the middle, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_194A")

    ChrTalk(    #41
        0x110,
        "#272FMy thoughts exactly.\x02",
    )

    CloseMessageWindow()

    label("loc_194A")

    OP_A2(0x229E)
    Jump("loc_1A01")

    label("loc_1950")


    ChrTalk(    #42
        0x9,
        (
            "#031FDisappearing from the stage like a shadow...\x01",
            "a perfect exit for a Phantom Thief.\x02\x03",

            "Heh, no less than I would expect of my rival.\x01",
            "Foe he may be, but I sing his praises!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A01")

    Jump("loc_1C1B")

    label("loc_1A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B76")

    ChrTalk(    #43
        0x9,
        (
            "#035FThe Phantom Thief may have withdrawn\x01",
            "from this battle...\x02\x03",

            "I am certain we shall clash again,\x01",
            "someday, however.\x02\x03",

            "After all! There are words he and I must\x01",
            "settle. We must arrive at a true\x01",
            "definition of beauty.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B30")

    ChrTalk(    #44
        0x110,
        (
            "#272F(... They really are exactly alike,\x01",
            "aren't they?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B30")


    ChrTalk(    #45
        0x101,
        (
            "#1019F(A war to decide who's\x01",
            "king of the ridiculous, huh?)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_1C1B")

    label("loc_1B76")


    ChrTalk(    #46
        0x9,
        (
            "#035FI'm sure the Phantom Thief and\x01",
            "I shall cross paths again.\x02\x03",

            "After all! There are words he and I must\x01",
            "settle. We must arrive at a true\x01",
            "definition of beauty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1B")

    Jump("loc_210F")

    label("loc_1C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_210F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E09")
    SetChrSubChip(0x9, 0)

    ChrTalk(    #47
        0xB,
        (
            "#070FI did imagine we'd drink together again\x01",
            "someday...\x02\x03",

            "It does feel a little strange, though,\x01",
            "after an entrance like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#031FHeh. I do wish I could have played\x01",
            "things out a little further.\x02\x03",

            "But, alas, I fear our most esteemed Prime\x01",
            "Minister is rather too impatient. I cannot\x01",
            "drag out things any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "#075FGoddess above.\x01",
            "I never imagined you were a prince!\x02\x03",

            "On some level, I feel sorry for the\x01",
            "citizens of Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x9)
    Jump("loc_1F1D")

    label("loc_1E09")


    ChrTalk(    #50
        0x9,
        (
            "#035FFor my part, I wish my soiree could have\x01",
            "gone on a little more.\x02\x03",

            "But, alas, I fear our most esteemed Prime\x01",
            "Minister is rather too impatient. I cannot\x01",
            "drag out things any longer.\x02\x03",

            "I do regret that I cannot join you in our\x01",
            "joyous competition of drink for much\x01",
            "longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1D")

    Jump("loc_210F")

    label("loc_1F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209A")

    ChrTalk(    #51
        0x9,
        (
            "#030FIt seems my journey has entered its final\x01",
            "chapter.\x02\x03",

            "Heh. I expect a finale worthy of the\x01",
            "rest of the tale!\x02\x03",

            "#037FAnd once everything is settled...\x01",
            "we must have a victory feast at\x01",
            "Grancel Castle.\x02\x03",

            "The besmirching I suffered at that last\x01",
            "banquet... ah, revenge, you are sweeter\x01",
            "than wine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1016FYou, uh, carry grudges kind of longer\x01",
            "than I thought...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_210F")

    label("loc_209A")


    ChrTalk(    #53
        0x9,
        (
            "#030FIt seems my journey has entered its final\x01",
            "chapter.\x02\x03",

            "Heh. I expect a finale worthy of the\x01",
            "rest of the tale!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210F")

    Jump("loc_215A")

    label("loc_2112")


    ChrTalk(    #54
        0x9,
        (
            "#035FAh, you require the power of genius,\x01",
            "then? Come!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 5)
    Jump("loc_215A")

    label("loc_2154")

    Jump("loc_215A")

    label("loc_2157")

    Jump("loc_215A")

    label("loc_215A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2C15")

    label("loc_2165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_23F1")
    TalkBegin(0xFE)
    OP_43(0x9, 0x0, 0x0, 0x3)
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
        (0, "loc_21D9"),
        (1, "loc_23A3"),
        (2, "loc_23E5"),
        (SWITCH_DEFAULT, "loc_23E8"),
    )


    label("loc_21D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2327")

    ChrTalk(    #55
        0x9,
        (
            "#035FHeh, good day, my compatriots.\x02\x03",

            "Have you come to hear the sweet sound\x01",
            "of Olivier Lenheim's lute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1019FOf all the... How can you be so casual\x01",
            "at a time like THIS?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "#035FHeh. I thought I would offer peace and\x01",
            "rest to those gathered here.\x02\x03",

            "I am prepared to join the expedition at\x01",
            "any time, so fear not.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_23A0")

    label("loc_2327")


    ChrTalk(    #58
        0x9,
        (
            "#035FTo offer still greater peace to those who\x01",
            "relax in the break room...\x02\x03",

            "Ah, a minstrel's duty is never finished!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A0")

    Jump("loc_23EB")

    label("loc_23A3")


    ChrTalk(    #59
        0x9,
        (
            "#035FAh, you require the power of genius,\x01",
            "then? Come!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 5)
    Jump("loc_23EB")

    label("loc_23E5")

    Jump("loc_23EB")

    label("loc_23E8")

    Jump("loc_23EB")

    label("loc_23EB")

    TalkEnd(0xFE)
    Jump("loc_2C15")

    label("loc_23F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_2C15")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2488")
    Jump("loc_24CA")

    label("loc_2488")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24A4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24CA")

    label("loc_24A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24C0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24CA")

    label("loc_24C0")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24CA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B07")

    ChrTalk(    #60
        0x9,
        "#030FAh, Estelle. Touring the ship?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1011FPretty much, yeah.\x02\x03",

            "#1019FEr, wait a minute.\x01",
            "Are you DRINKING before a mission?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "#035FHeh, this is a drink of celebration,\x01",
            "my sweet.\x02\x03",

            "I celebrate the imminent meeting of the\x01",
            "genius bard and legendary dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1015FWell, putting aside the 'genius bard'\x01",
            "bit... a legendary dragon...\x02\x03",

            "#1000FDo they still tell stories about\x01",
            "dragons in the Empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "#031FWhy, naturally!\x02\x03",

            "There are quite a number of legends and\x01",
            "tall tales of sightings, especially in\x01",
            "the southern regions near Bose.\x02\x03",

            "In fact, I believe the Imperial Institute of Science\x01",
            "was to launch an investigation... but\x01",
            "then the Hundred Days War broke out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1004FWow, sounds like you guys take the\x01",
            "'legends' kind of seriously.\x02\x03",

            "So even in the Empire, dragons are\x01",
            "pretty much a mystery, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "#030FHm. You could say that, I suppose...\x02\x03",

            "But to the people of the Empire, this\x01",
            "particular situation would have a more...\x01",
            "straightforward solution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1011FStraightforward... huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#030FErebonia is a far more... ah, pragmatic\x01",
            "realm than Liberl.\x02\x03",

            "If something like this were to happen in\x01",
            "the Empire, His Majesty would order\x01",
            "the destruction of the dragon immediately.\x02\x03",

            "#035FThe Empire believes in boldly standing\x01",
            "against all who would oppose it.\x02\x03",

            "Even if the opposition is a dragon, it\x01",
            "would be torn down without mercy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1016FTh-That seems a little bloodthirsty...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#034FSecuring national peace through force of\x01",
            "arms is... the Erebonian way.\x02\x03",

            "I confess, as a messenger of love\x01",
            "and peace, I do find it a bit... sad.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A20)
    Jump("loc_2C0D")

    label("loc_2B07")


    ChrTalk(    #71
        0x9,
        (
            "#035FIt would be an interesting turn of events\x01",
            "for the dragon to flee into Erebonia.\x02\x03",

            "#030FWere that to happen, though, it is all\x01",
            "too clear that it would be taken as an\x01",
            "excuse for rekindled war.\x02\x03",

            "Our good General Morgan is all too\x01",
            "aware of that, I suspect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C0D")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_2C15")

    Return()

    # Function_2_152A end

    def Function_3_2C16(): pass

    label("Function_3_2C16")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CA6")
    Jump("loc_2CE8")

    label("loc_2CA6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CC2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CE8")

    label("loc_2CC2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CDE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CE8")

    label("loc_2CDE")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CE8")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
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
        (0, "loc_2D70"),
        (1, "loc_3F21"),
        (2, "loc_3F50"),
        (SWITCH_DEFAULT, "loc_3F53"),
    )


    label("loc_2D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_31F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F51")
    SetChrSubChip(0xB, 0)

    ChrTalk(    #72
        0xB,
        (
            "#070FI did imagine we'd drink together again\x01",
            "someday...\x02\x03",

            "It does feel a little strange, though,\x01",
            "after an entrance like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#031FHeh. I do wish I could have played things\x01",
            "out a little further.\x02\x03",

            "But, alas, I fear our most esteemed Prime\x01",
            "Minister is rather too impatient. I cannot\x01",
            "drag out things any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        (
            "#075FGoddess above.\x01",
            "I never imagined you were a prince!\x02\x03",

            "On some level, I feel sorry for the\x01",
            "citizens of Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x9)
    Jump("loc_2FE0")

    label("loc_2F51")


    ChrTalk(    #75
        0xB,
        (
            "#075FGreat Goddess... I still can't believe you're\x01",
            "a prince.\x02\x03",

            "On some level, I have to shed a tear for\x01",
            "the people of the Empire, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE0")

    Jump("loc_31EF")

    label("loc_2FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312F")

    ChrTalk(    #76
        0xB,
        (
            "#070FAidios' beard, things were a mess in here!\x01",
            "It's under control now, I think.\x02\x03",

            "#072FI fear our job is just beginning,\x01",
            "however.\x02\x03",

            "It will likely be nothing but one brutal\x01",
            "fight after another in that central tower.\x02\x03",

            "Do not be afraid to retreat if you need to.\x01",
            "Return here to rest, do not push yourselves\x01",
            "too far.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_31EF")

    label("loc_312F")


    ChrTalk(    #77
        0xB,
        (
            "#072FIt will likely be nothing but one brutal\x01",
            "fight after another in that central tower.\x02\x03",

            "Do not be afraid to retreat if you need to.\x01",
            "Return here to rest, do not push\x01",
            "yourselves too far.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31EF")

    Jump("loc_3F1E")

    label("loc_31F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_340D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336E")

    ChrTalk(    #78
        0xB,
        (
            "#072FSo the final Enforcer is Renne, huh?\x01",
            "The 'Angel of Slaughter'...\x02\x03",

            "The ease with which she played us for\x01",
            "fools... I can't believe she just picked that\x01",
            "up somewhere.\x02\x03",

            "#572FThat child... I wonder.\x02\x03",

            "I feel as though she must carry a great\x01",
            "burden on her back--greater than is\x01",
            "obvious at first.\x02\x03",

            "Great power such as hers always carries\x01",
            "a cost, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_340A")

    label("loc_336E")


    ChrTalk(    #79
        0xB,
        (
            "#072FThe ease with which she played us for\x01",
            "fools... I can't believe she just picked that\x01",
            "up somewhere.\x02\x03",

            "She may carry a burden greater than\x01",
            "we know...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340A")

    Jump("loc_3F1E")

    label("loc_340D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_36A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362E")

    ChrTalk(    #80
        0xB,
        "#070FAh, everyone! Heading for the tower?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#1040FYes, once we're done preparing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1011FTaking a break, Zin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        (
            "#070FTo be honest, I would like to take a\x01",
            "chance to rest, perhaps meditate...\x02\x03",

            "But now is not really the time.\x01",
            "If you call, I'll be ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        (
            "#021FYou don't need to push yourself.\x02\x03",

            "After all, you took down Walter!\x01",
            "You can afford to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        "#1040FYes, don't strain yourself too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xB,
        (
            "#070FHaha. Thanks for the thought.\x02\x03",

            "You don't need to hold back for my sake,\x01",
            "though. Just say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E43)
    Jump("loc_36A1")

    label("loc_362E")


    ChrTalk(    #87
        0xB,
        (
            "#070FIt would be nice to rest for a while,\x01",
            "but this isn't really the time.\x02\x03",

            "If you need my fist, just say so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A1")

    Jump("loc_3F1E")

    label("loc_36A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_36AE")
    Jump("loc_3F1E")

    label("loc_36AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_3F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E99")

    ChrTalk(    #88
        0xB,
        "#070FHello, everyone.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_373A")

    ChrTalk(    #89
        0x103,
        (
            "#020FHmmmmm, alone today?\x02\x03",

            "I don't usually see you flying solo,\x01",
            "as it were.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AE")

    label("loc_373A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_378E")

    ChrTalk(    #90
        0x106,
        (
            "#051FHeh, alone today, huh?\x02\x03",

            "Never seen you drink alone much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AE")

    label("loc_378E")


    ChrTalk(    #91
        0x102,
        "#1044FAre you alone today?\x02",
    )

    CloseMessageWindow()

    label("loc_37AE")


    ChrTalk(    #92
        0xB,
        (
            "#071FHaha, well, my usual drinking partner's\x01",
            "gone back to his Empire, you know.\x02\x03",

            "It might be a bit late, but I was giving\x01",
            "him a farewell toast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1015FOh, right...\x02\x03",

            "You drank with Olivier a lot,\x01",
            "didn't you, Zin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#1041FYou two make for an odd pair,\x01",
            "thinking about it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F5")

    ChrTalk(    #95
        0x105,
        "#048FHaha! That's true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_398C")

    label("loc_38F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3920")

    ChrTalk(    #96
        0x107,
        "#560FHeehee, yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_398C")

    label("loc_3920")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_394A")

    ChrTalk(    #97
        0x106,
        "#051FHeh, I'll say.\x02",
    )

    CloseMessageWindow()
    Jump("loc_398C")

    label("loc_394A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_398C")

    ChrTalk(    #98
        0x103,
        (
            "#021FNow that you mention it,\x01",
            "they kind of do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_398C")


    ChrTalk(    #99
        0xB,
        (
            "#074FIt's true, we didn't have much in common\x01",
            "except a love of good alcohol.\x02\x03",

            "#070FMaybe that's why we got along so well.\x02\x03",

            "People can enjoy seeking out things different\x01",
            "from themselves, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1011FYeah... maybe.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B7B")

    ChrTalk(    #101
        0x103,
        (
            "#525FWell, I can join you from now on,\x01",
            "if you like.\x02\x03",

            "It's not healthy to drink alone,\x01",
            "you know.㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #102
        0x101,
        (
            "#1015FErrr, um...\x02\x03",

            "(It'd probably be even LESS healthy\x01",
            "to drink with Schera...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        "#1048F(... You'll get whipped if she hears that.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E21")

    label("loc_3B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D28")

    ChrTalk(    #104
        0x109,
        (
            "#1060FWell, hey, if you want, I can pull up a\x01",
            "chair with you!\x02\x03",

            "Ain't healthy to drink alone, after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #105
        0x101,
        (
            "#1004FEr. But...\x02\x03",

            "Are priests even allowed to drink alcohol?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #106
        0x109,
        (
            "#1068FWelllllllll...\x01",
            "To be precise, no, it's forbidden...\x02\x03",

            "#1066FBut I'm sure Aidios, in Her infinite\x01",
            "grace, would forgive a minor trespass.\x01",
            "Or three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1019FBoy, you're just a paragon of faith,\x01",
            "aren't you, Kevin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E21")

    label("loc_3D28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA9")

    ChrTalk(    #108
        0x106,
        (
            "#051FWell, you can invite me from now on if\x01",
            "you want.\x02\x03",

            "I ain't really as fun as he is, though,\x01",
            "I'll admit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E21")

    label("loc_3DA9")


    ChrTalk(    #109
        0x102,
        (
            "#1040FI could join you, if you like.\x02\x03",

            "I'll have to refrain from the alcohol,\x01",
            "but I'd be happy to keep you company.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E21")


    ChrTalk(    #110
        0xB,
        (
            "#070FThanks, that's kind of you.\x02\x03",

            "Can't let an offer like that go to waste,\x01",
            "can I? I'll invite you sometime.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E28)
    Jump("loc_3F1E")

    label("loc_3E99")


    ChrTalk(    #111
        0xB,
        (
            "#070FI'll be here tipping back glasses for a bit.\x01",
            "I won't go overboard, don't worry.\x02\x03",

            "You need me to back you up, say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F1E")

    Jump("loc_3F56")

    label("loc_3F21")


    ChrTalk(    #112
        0xB,
        "#070FTime for me to join the team?\x02",
    )

    CloseMessageWindow()
    Call(0, 5)
    Jump("loc_3F56")

    label("loc_3F50")

    Jump("loc_3F56")

    label("loc_3F53")

    Jump("loc_3F56")

    label("loc_3F56")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_2C16 end

    def Function_4_3F5F(): pass

    label("Function_4_3F5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_3FC8")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F8B")
    SetChrSubChip(0xFE, 0)
    Jump("loc_3FBC")

    label("loc_3F8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FA1")
    SetChrSubChip(0xFE, 2)
    Jump("loc_3FBC")

    label("loc_3FA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FB7")
    SetChrSubChip(0xFE, 1)
    Jump("loc_3FBC")

    label("loc_3FB7")

    SetChrSubChip(0xFE, 0)

    label("loc_3FBC")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)

    label("loc_3FC8")

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
        (0, "loc_402B"),
        (1, "loc_4556"),
        (2, "loc_4597"),
        (SWITCH_DEFAULT, "loc_459A"),
    )


    label("loc_402B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_41BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415C")

    ChrTalk(    #113
        0x10,
        "#051FYo, Scherazard. You're up now, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        (
            "#025FLooks like it, yes.\x02\x03",

            "Sorry I can't stay and have a drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "#051FBooze aside, if you need my sword,\x01",
            "I'll come along any time.\x02\x03",

            "You need me, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x103,
        (
            "#525FHeh. Thank you, Mister Heavy Blade.\x01",
            "I owe you one.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E45)
    SetChrSubChip(0xFE, 0)
    Jump("loc_41BB")

    label("loc_415C")


    ChrTalk(    #117
        0x10,
        (
            "#051FIf you need my sword,\x01",
            "I'll come along anytime.\x02\x03",

            "You need me, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_41BB")

    Jump("loc_4553")

    label("loc_41BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_4553")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_425C")

    ChrTalk(    #118
        0x10,
        (
            "#053FThe 'Direwolf', huh?\x02\x03",

            "We couldn't lay a finger on him back\x01",
            "in Zeiss.\x02\x03",

            "#050FWell, with you around it might be\x01",
            "a bit easier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_425C")


    ChrTalk(    #119
        0x10,
        (
            "#053FWalter the Direwolf, huh?\x02\x03",

            "He practically juggled us back in Zeiss.\x02\x03",

            "#050FMight be a bit easier with you around,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42DF")


    ChrTalk(    #120
        0x108,
        (
            "#070FDo not put too much faith in me.\x01",
            "I don't know if I will be of any help\x01",
            "until I meet him in battle.\x02\x03",

            "If you want to see, Agate, why not\x01",
            "come along?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x108, 400)

    ChrTalk(    #121
        0x10,
        (
            "#051FHeh, good point.\x02\x03",

            "I'll be ready.\x01",
            "You need me, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#1006FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#1040FWe'll be counting on you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E44)
    Jump("loc_4553")

    label("loc_440B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_44AB")
    TurnDirection(0x10, 0x108, 0)

    ChrTalk(    #124
        0x10,
        (
            "#050FThe Direwolf... Those friggin' punches\x01",
            "of his ain't normal.\x02\x03",

            "#051FHeh, lookin' forward to seeing how\x01",
            "you guys handle him. Good luck!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4553")

    label("loc_44AB")

    TurnDirection(0x10, 0x108, 0)

    ChrTalk(    #125
        0x10,
        (
            "#050FWalter the Direwolf... He's no normal\x01",
            "kung-fu wannabe, that's for damn sure.\x02\x03",

            "#051FHeh, you guys are gonna put on a show\x01",
            "when you throw down with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4553")

    Jump("loc_459D")

    label("loc_4556")


    ChrTalk(    #126
        0x10,
        (
            "#050FNeed to change team members?\x01",
            "I'm all set to go.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 5)
    Jump("loc_459D")

    label("loc_4597")

    Jump("loc_459D")

    label("loc_459A")

    Jump("loc_459D")

    label("loc_459D")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_3F5F end

    def Function_5_45A6(): pass

    label("Function_5_45A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_4A4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49DB")

    ChrTalk(    #127
        0xD,
        "#160FMs. Bright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1000FIs something wrong, General Morgan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        (
            "#160FMm. I was taking a moment to look over\x01",
            "the battle plan again.\x02\x03",

            "A plan that can seem perfect when first\x01",
            "drafted can show faults over time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#1002FHave you, um, found any problems, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xD,
        (
            "#163FNone that stand out to me.\x02\x03",

            "Short of the truly unpredictable happening,\x01",
            "this plan should succeed.\x02\x03",

            "#165FI'm afraid there'll be no need for you\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1015FWell, I won't mind if that turns out to be\x01",
            "true...\x02\x03",

            "#1002FBut. If we need to, we'll help as best we can.\x02\x03",

            "You did, um, let us aboard, after all, sir.\x01",
            "You must suspect something could happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xD,
        (
            "#160FIt's possible. But remember...\x02\x03",

            "You will only act if our plan ends... prematurely.\x02\x03",

            "I expect you to follow orders during the\x01",
            "mission itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1006FDon't worry, we understand.\x02\x03",

            "We'll just watch for now and see what you\x01",
            "guys can do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xD,
        (
            "#165FHmph. Quite a head on your shoulders,\x01",
            "Ms. Bright.\x02\x03",

            "We still have a little time before contact\x01",
            "with the dragon.\x02\x03",

            "Use the time until then to ensure you're\x01",
            "prepared.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A72)
    Jump("loc_4A4F")

    label("loc_49DB")


    ChrTalk(    #136
        0xD,
        (
            "#160FYou bracers will only act if our plans\x01",
            "go awry.\x02\x03",

            "I expect you to follow orders during the\x01",
            "mission itself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A4F")

    TalkEnd(0xFE)
    Return()

    # Function_5_45A6 end

    def Function_6_4A53(): pass

    label("Function_6_4A53")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4C30")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                             # 0
            "Buy Items\x01",                        # 1
            "Buy Ingredients\x01",                  # 2
            "[Bitter Omelet] - 1800 mira\x01",      # 3
            "Leave\x01",                            # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AF6")
    OP_A9(0x2C)
    TalkEnd(0x1C)
    Return()

    label("loc_4AF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0C")
    OP_A9(0x2B)
    TalkEnd(0x1C)
    Return()

    label("loc_4B0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C1C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4BE2")
    SubMira(1800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #137
        "\x06Ate #2CBitter Omelet#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x9C4)
    OP_31(0x1, 0xFD, 0x9C4)
    OP_31(0x2, 0xFD, 0x9C4)
    OP_31(0x3, 0xFD, 0x9C4)
    OP_31(0x4, 0xFD, 0x9C4)
    OP_31(0x5, 0xFD, 0x9C4)
    OP_31(0x6, 0xFD, 0x9C4)
    OP_31(0x7, 0xFD, 0x9C4)
    OP_31(0x8, 0xFD, 0x9C4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BD4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xC)"), scpexpr(EXPR_END)), "loc_4BA5")
    Jump("loc_4BD4")

    label("loc_4BA5")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #138
        "\x06Learned [#2CBitter Omelet#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_4BD4")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_4C0A")

    label("loc_4BE2")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #139
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_4C0A")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x1C)
    Return()

    label("loc_4C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C2D")
    TalkEnd(0x1C)
    Return()

    label("loc_4C2D")

    Jump("loc_4CCF")

    label("loc_4C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4CCF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Buy Items\x01",            # 1
            "Buy Ingredients\x01",      # 2
            "Leave\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CA8")
    OP_A9(0x2A)
    TalkEnd(0x1C)
    Return()

    label("loc_4CA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CBE")
    OP_A9(0x2B)
    TalkEnd(0x1C)
    Return()

    label("loc_4CBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CCF")
    TalkEnd(0x1C)
    Return()

    label("loc_4CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_502E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE0")

    ChrTalk(    #140
        0x1C,
        (
            "Hey, captain. Sounds like the expedition\x01",
            "into the city core's nearing the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x1C,
        (
            "You're a one-woman army, so I bet\x01",
            "we'll come out of it okay, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x1C,
        "A lot of the crew are pretty worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x1C,
        "So come home safe AND quick, okay?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4E88")

    label("loc_4DE0")


    ChrTalk(    #144
        0x1C,
        (
            "We'll get the Ladybird flying again\x01",
            "somehow, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x1C,
        "So make sure you get home quick, you hear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x1C,
        (
            "The Ladybird won't be the same without\x01",
            "you commanding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E88")

    Jump("loc_502B")

    label("loc_4E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F98")

    ChrTalk(    #147
        0x1C,
        "Yo, Team Bracer! What's shaking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x1C,
        (
            "Sounds like the expedition into the city\x01",
            "core's nearing the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x1C,
        (
            "We'll get the Ladybird flying again\x01",
            "somehow, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x1C,
        (
            "Get back safe, you hear? I want us all\x01",
            "together when we head back to the\x01",
            "surface.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_502B")

    label("loc_4F98")


    ChrTalk(    #151
        0x1C,
        (
            "We'll get the Ladybird flying again\x01",
            "somehow, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x1C,
        (
            "Get back safe, you hear? I want us all\x01",
            "together when we head back to the\x01",
            "surface.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_502B")

    Jump("loc_5F1C")

    label("loc_502E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_5194")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_511A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50D5")

    ChrTalk(    #153
        0x1C,
        (
            "Huh. That's actually not bad\x01",
            "lute...ing, if I say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x1C,
        (
            "Looks like that self-proclaimed minstrel\x01",
            "wasn't all hot air.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5117")

    label("loc_50D5")


    ChrTalk(    #155
        0x1C,
        (
            "Huh. That's actually not bad\x01",
            "lute...ing, if I say so myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5117")

    Jump("loc_5191")

    label("loc_511A")


    ChrTalk(    #156
        0x1C,
        (
            "To think we ended up working with\x01",
            "the sky bandits, of all people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x1C,
        "I'm amazed Captain Julia agreed to that...\x02",
    )

    CloseMessageWindow()

    label("loc_5191")

    Jump("loc_5F1C")

    label("loc_5194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_52C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5258")

    ChrTalk(    #158
        0x1C,
        (
            "I made sure to stock up heavily before\x01",
            "we left port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x1C,
        (
            "I've got more stuff for sale than most\x01",
            "stores!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x1C,
        (
            "You need something, just ask and\x01",
            "I'll see if I can find it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_52C6")

    label("loc_5258")


    ChrTalk(    #161
        0x1C,
        (
            "I made sure to stock up heavily before\x01",
            "we left port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1C,
        (
            "I've got more stuff for sale than most\x01",
            "stores!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52C6")

    Jump("loc_5F1C")

    label("loc_52C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_53B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5354")

    ChrTalk(    #163
        0x1C,
        "Yo, Team Bracer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x1C,
        "I'm finally done cleaning up in here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x1C,
        (
            "Make sure to stock up before heading\x01",
            "out there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_53B4")

    label("loc_5354")


    ChrTalk(    #166
        0x1C,
        "I'm finally done cleaning up in here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x1C,
        (
            "Make sure to stock up before heading\x01",
            "out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53B4")

    Jump("loc_5F1C")

    label("loc_53B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_5B7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_553E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_549D")

    ChrTalk(    #168
        0x1C,
        "Just one tower left now, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x1C,
        (
            "Finally close to the end of the mission,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x1C,
        (
            "Still, they say the greatest danger in\x01",
            "sky travel is the takeoff and the\x01",
            "landing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x1C,
        "Be careful, you hear?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_553B")

    label("loc_549D")


    ChrTalk(    #172
        0x1C,
        (
            "They say the greatest danger in sky\x01",
            "travel is the takeoff and the landing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x1C,
        (
            "You be careful out there... 'cause this\x01",
            "is gonna be one rough landing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_553B")

    Jump("loc_5B7B")

    label("loc_553E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_56F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5632")

    ChrTalk(    #174
        0x1C,
        (
            "Seems like the entire country's gone\x01",
            "completely barking mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x1C,
        (
            "I'm sure our boys below've got their\x01",
            "hands full...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x1C,
        (
            "Er, what I'm saying is, it's great that\x01",
            "we've got you lot to take care of these\x01",
            "blasted towers!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_56F1")

    label("loc_5632")


    ChrTalk(    #177
        0x1C,
        (
            "Sending you bracers into the towers\x01",
            "was the right tactical decision, I say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x1C,
        (
            "Just what I'd expect from Brigadier General Bright.\x01",
            "He knows how to give the right person\x01",
            "the right job!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56F1")

    Jump("loc_5B7B")

    label("loc_56F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_5A07")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5917")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F2")

    ChrTalk(    #179
        0x1C,
        "That woman at the table... what a beauty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x1C,
        (
            "I'd love to get her a drink, but she's on\x01",
            "standby before a mission, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x1C,
        (
            "Even a bit of alcohol can impair\x01",
            "your judgment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x1C,
        "... so I'll hold off for now.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5914")

    label("loc_57F2")


    ChrTalk(    #183
        0x1C,
        (
            "Alcohol can make you feel like you're on\x01",
            "top of the world, sure, but it also impairs\x01",
            "your judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x1C,
        (
            "There's one simple conclusion you can\x01",
            "draw from this, mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x1C,
        (
            "It's our ability to judge and understand\x01",
            "the world that causes unhappiness!\x01",
            "Still, don't know if I'd give it up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5914")

    Jump("loc_5A04")

    label("loc_5917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59B6")

    ChrTalk(    #186
        0x1C,
        (
            "Yo, good work so far. Come to get\x01",
            "something to eat before heading out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x1C,
        (
            "You eat the right meal and you'll have\x01",
            "energy when you need it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_5A04")

    label("loc_59B6")


    ChrTalk(    #188
        0x1C,
        (
            "Want to grab a bite before you head out?\x01",
            "You need to stay fed, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A04")

    Jump("loc_5B7B")

    label("loc_5A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_5B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF9")

    ChrTalk(    #189
        0x1C,
        (
            "Yo, bracers. You're odd ones, showing up\x01",
            "here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x1C,
        (
            "Anyway, the commissary is open, and I've\x01",
            "got everything you'll ever need, including\x01",
            "ingredients for cooking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x1C,
        "You need anything, you just come see Casey.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5B7B")

    label("loc_5AF9")


    ChrTalk(    #192
        0x1C,
        (
            "The galley's the closest thing we've got\x01",
            "to a 'shop' aboard ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x1C,
        (
            "You need any supplies, you just come\x01",
            "and speak to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B7B")

    Jump("loc_5F1C")

    label("loc_5B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_5F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E45")

    ChrTalk(    #194
        0x1C,
        "Yo, bracers! Welcome to the ship's galley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x1C,
        (
            "The name's Casey. I run this little corner\x01",
            "of the Ladybird as ship's cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x1C,
        (
            "I run the ship commissariat, too,\x01",
            "but that's not quite ready yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x1C,
        (
            "If you want some supplies, I'll have to\x01",
            "ask you to come back a bit later.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_END)), "loc_5E3F")

    ChrTalk(    #198
        0x101,
        "#1011FAww, you're not open? Oh well.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(500)

    ChrTalk(    #199
        0x101,
        (
            "#1015F...Hang on, though. Why's he drinking,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x1C,
        (
            "Oh, the guy in the white coat?\x01",
            "I treated him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x1C,
        (
            "I was checking the stock of liquor and\x01",
            "he struck up a conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x1C,
        (
            "He seemed to know what he was talkin'\x01",
            "about, so I gave him a drink.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1C, 400)
    Sleep(500)

    ChrTalk(    #203
        0x101,
        (
            "#1004FI, uh, I see...\x02\x03",

            "(Olivier calls himself a gourmand\x01",
            "for a reason, I guess.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E3F")

    OP_A2(0x0)
    Jump("loc_5F1C")

    label("loc_5E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_END)), "loc_5EB7")

    ChrTalk(    #204
        0x1C,
        (
            "That golden-haired guy seems to be\x01",
            "from Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x1C,
        (
            "Well... his taste in wine's good,\x01",
            "at least!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1C")

    label("loc_5EB7")


    ChrTalk(    #206
        0x1C,
        "Sorry, the commissary isn't open just yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x1C,
        (
            "If you need some supplies,\x01",
            "check back in a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F1C")

    TalkEnd(0x1C)
    Return()

    # Function_6_4A53 end

    def Function_7_5F20(): pass

    label("Function_7_5F20")

    TalkBegin(0xFE)
    SetChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F45")
    SetChrSubChip(0xFE, 0)
    Jump("loc_5F76")

    label("loc_5F45")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F5B")
    SetChrSubChip(0xFE, 1)
    Jump("loc_5F76")

    label("loc_5F5B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F71")
    SetChrSubChip(0xFE, 2)
    Jump("loc_5F76")

    label("loc_5F71")

    SetChrSubChip(0xFE, 0)

    label("loc_5F76")

    OP_8C(0xFE, 0, 0)
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6006")

    ChrTalk(    #208
        0xFE,
        (
            "Huh! Been a while since I've heard\x01",
            "a lute played in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "The music's nice. Really relaxing!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_602E")

    label("loc_6006")


    ChrTalk(    #210
        0xFE,
        "The music's nice. Really relaxing!\x02",
    )

    CloseMessageWindow()

    label("loc_602E")

    Jump("loc_6148")

    label("loc_6031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CD")

    ChrTalk(    #211
        0xFE,
        (
            "All right, time to get something to\x01",
            "eat while I still can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "I'm going on shift and might end\x01",
            "up in the thick of it later, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_6148")

    label("loc_60CD")


    ChrTalk(    #213
        0xFE,
        (
            "All right, time to get something to\x01",
            "eat while I still can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "Let's see what that old dog Casey\x01",
            "recommends today...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6148")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_7_5F20 end

    def Function_8_6151(): pass

    label("Function_8_6151")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_62FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6263")

    ChrTalk(    #215
        0xFE,
        (
            "Not much of a choice but to eat here\x01",
            "when we're on a long-haul voyage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "The harder the job is, though,\x01",
            "the nicer eating here is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "And Casey's got one hell of a job, changing\x01",
            "the menu up every day so we don't get\x01",
            "tired of the same thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_62FC")

    label("loc_6263")


    ChrTalk(    #218
        0xFE,
        (
            "Not much of a choice but to eat here\x01",
            "when we're on a long-haul voyage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "Thankfully, Casey's a hell of a cook.\x01",
            "Thank Aidios for small blessings!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FC")

    TalkEnd(0xFE)
    Return()

    # Function_8_6151 end

    def Function_9_6300(): pass

    label("Function_9_6300")

    TalkBegin(0xFE)
    SetChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6325")
    SetChrSubChip(0xFE, 0)
    Jump("loc_6356")

    label("loc_6325")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_633B")
    SetChrSubChip(0xFE, 2)
    Jump("loc_6356")

    label("loc_633B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6351")
    SetChrSubChip(0xFE, 1)
    Jump("loc_6356")

    label("loc_6351")

    SetChrSubChip(0xFE, 0)

    label("loc_6356")

    OP_8C(0xFE, 180, 0)
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63E2")

    ChrTalk(    #220
        0xFE,
        "Phew! Managed to get an early break!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "Well, I'll be manning the deck shift\x01",
            "in a little while, but still.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_6429")

    label("loc_63E2")


    ChrTalk(    #222
        0xFE,
        "Phew! Managed to get an early break!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        "Right, then, chow time!\x02",
    )

    CloseMessageWindow()

    label("loc_6429")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_9_6300 end

    def Function_10_6432(): pass

    label("Function_10_6432")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_643F")
    Jump("loc_6767")

    label("loc_643F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_6617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_659B")

    ChrTalk(    #224
        0xFE,
        (
            "... Steam may seem to disappear, but it's\x01",
            "just dispersed into the atmosphere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "Conservation of matter and energy,\x01",
            "the same's got to apply to this, the\x01",
            "orbal energy's got to be stored SOMEWHERE...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "The 'shadow towers', and folded dimensions...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "Could that be where the disappearing\x01",
            "orbal energy is going...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_6614")

    label("loc_659B")


    ChrTalk(    #228
        0xFE,
        "The 'shadow towers', and folded dimensions...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "That's got to be where the 'disappearing'\x01",
            "orbal energy is going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6614")

    Jump("loc_6767")

    label("loc_6617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_6767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E0")

    ChrTalk(    #230
        0xFE,
        (
            "From what I've heard, Zeiss has\x01",
            "it rough right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "Looks like the fruits of my research are\x01",
            "going to be needed pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        "I'll need to really put myself into it!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_6767")

    label("loc_66E0")


    ChrTalk(    #233
        0xFE,
        (
            "From what I've heard, Zeiss has\x01",
            "it rough right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "Looks like the fruits of my research are\x01",
            "going to be needed pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6767")

    TalkEnd(0xFE)
    Return()

    # Function_10_6432 end

    SaveToFile()

Try(main)
