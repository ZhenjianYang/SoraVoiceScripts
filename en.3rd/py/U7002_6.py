from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7002_6 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7002.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_299A",         # 03, 3
        "Function_4_485E",         # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_5EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_270")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #0
        0x12,
        (
            "#066FAgate really respects Mr. Bright, too...\x02\x03",

            "#562FWhy can't he just be more honest with himself?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18C")

    ChrTalk(    #1
        0x101,
        (
            "#1028F(An interesting question!\x01",
            "Your thoughts, Agate?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247")

    label("loc_18C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED")

    ChrTalk(    #2
        0x103,
        (
            "#1535F(What an interesting question.)\x01",
            "Care to give any input, Agate?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247")

    label("loc_1ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_222")

    ChrTalk(    #3
        0x10A,
        "#816F(Anything to say, Agate?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_247")

    label("loc_222")


    ChrTalk(    #4
        0x109,
        "#1840F(Anything to say, Agate?)\x02",
    )

    CloseMessageWindow()

    label("loc_247")


    ChrTalk(    #5
        0x106,
        "#055F(Aww, cram it up your ass!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_432")

    label("loc_270")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 1)), scpexpr(EXPR_END)), "loc_356")

    ChrTalk(    #6
        0x12,
        (
            "#066FAgate seems to be really happy that\x01",
            "he got to fight Mr. Bright.\x02\x03",

            "#564F...He keeps talking about how he wants\x01",
            "to beat up the real one next time he sees\x01",
            "him, though...\x02\x03",

            "#562F*sigh* Why is he always like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432")

    label("loc_356")


    ChrTalk(    #7
        0x12,
        (
            "#060FAgate really wanted to fight Mr. Bright\x01",
            "judging by the way he's grumbling.\x02\x03",

            "#063FBut I wonder why? I know that deep down,\x01",
            "he actually really respects him...\x02\x03",

            "#562FWhy can't he just be more honest with\x01",
            "himself?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432")

    OP_A2(0x1)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_5EB")

    label("loc_440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_522")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #8
        0x12,
        (
            "#066FAgate really respects Mr. Bright, too...\x02\x03",

            "#562F...so why can't he just be more honest\x01",
            "with himself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x106,
        (
            "#551F(H-How am I supposed to talk to her when\x01",
            "she's all down in the dumps like this?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E3")

    label("loc_522")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0x12,
        (
            "#063FAgate really respects Mr. Bright, too...\x02\x03",

            "#063F...and yet he keeps going on and on\x01",
            "about wanting to fight him or settling\x01",
            "some score...\x02\x03",

            "#562FI wish I knew what he was thinking...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E3")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_5EB")

    Jump("loc_2999")

    label("loc_5EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_853")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_733")
    TalkBegin(0xFE)

    ChrTalk(    #11
        0x12,
        (
            "#060FFrom what I know, Kilika went back to Calvard\x01",
            "not long before Grandpa left Zeiss on vacation.\x02\x03",

            "#564FShe just showed up at our house one day to tell\x01",
            "us she was off, and that was that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_705")

    ChrTalk(    #12
        0x101,
        "#1016FThat sounds just like her, all right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_72A")

    label("loc_705")


    ChrTalk(    #13
        0x109,
        "#1066FHaha. Sounds about right.\x02",
    )

    CloseMessageWindow()

    label("loc_72A")

    OP_A2(0x1)
    TalkEnd(0xFE)
    Jump("loc_850")

    label("loc_733")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #14
        0x12,
        (
            "#064FOh, speaking of Zeiss...\x02\x03",

            "#063FI hope Mr. Murdock is doing okay.\x02\x03",

            "...And I hope Mom isn't causing more\x01",
            "trouble for him...\x02\x03",

            "Especially now that he won't have Kilika\x01",
            "to help him.\x02\x03",

            "#561FI hope he hasn't worked himself sick or\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_850")

    Jump("loc_2999")

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_CC5")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EA")
    Jump("loc_92C")

    label("loc_8EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_906")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_92C")

    label("loc_906")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_922")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_92C")

    label("loc_922")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_92C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C69")
    OP_A2(0x1)

    ChrTalk(    #15
        0x12,
        (
            "#563F#40W...\x02\x03",

            "#562F...Mm...\x01",
            "...Mmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #16
        0x12,
        "#064F...?!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)
    SetChrChipByIndex(0xFE, 39)
    Sleep(800)

    ChrTalk(    #17
        0x12,
        "#0562F#40W...Mm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1016F(Aww. Looks like she's having a little nap.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        (
            "#1448F(She was the first person we released from a \x01",
            "sealing stone, incidentally.)\x02\x03",

            "(She must be exhausted.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B34")

    ChrTalk(    #20
        0x106,
        "#556F(Makes sense. Guess we should just let her rest.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1000F(Yeah, you're right.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_C66")

    label("loc_B34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B99")

    ChrTalk(    #22
        0x102,
        "#1501F(I think we should let her rest, then.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1000F(Yeah, you're right.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_C66")

    label("loc_B99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFE")

    ChrTalk(    #24
        0x105,
        "#1165F(I think we should let her rest, then.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1000F(Yeah, you're right.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_C66")

    label("loc_BFE")


    ChrTalk(    #26
        0x101,
        (
            "#1006F(Yeah, you're probably right. I guess we should\x01",
            "let her rest, then.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10F,
        "#1447F(...Indeed.)\x02",
    )

    CloseMessageWindow()

    label("loc_C66")

    Jump("loc_CBA")

    label("loc_C69")


    ChrTalk(    #28
        0x12,
        (
            "#562F#40WMmm...\x01",
            "...Mm...\x02\x03",

            "#067F#20W...Heehee...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10F,
        "#1442F(She's so cute.)\x02",
    )

    CloseMessageWindow()

    label("loc_CBA")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2999")

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 2)), scpexpr(EXPR_END)), "loc_F50")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E78")

    ChrTalk(    #30
        0x12,
        (
            "#564FI'm worried about Kevin, but that's not all \x01",
            "I'm worried about...\x02\x03",

            "#063FIt sounded like the Lord of Phantasma knew\x01",
            "Kevin would use his Stigma's power and end\x01",
            "up collapsing...\x02\x03",

            "...and that that would make their kingdom draw\x01",
            "closer to completion or something. Which is...\x01",
            "worrying, too.\x02\x03",

            "#561FWe're going to need to be even more careful\x01",
            "than before, aren't we?\x02\x03",

            "I don't want anyone else getting hurt...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_F4A")

    label("loc_E78")


    ChrTalk(    #31
        0x12,
        (
            "#063FThe Lord of Phantasma has never hurt any of\x01",
            "us directly, sure...\x02\x03",

            "...but they're still willing to use devils to do it,\x01",
            "which isn't that much different.\x02\x03",

            "#062FWe're going to need to be really careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4A")

    TalkEnd(0xFE)
    Jump("loc_2999")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_125E")
    TalkBegin(0xFE)
    TurnDirection(0x12, 0x101, 0)

    ChrTalk(    #32
        0x12,
        (
            "#064FOhhh, Estelle!\x02\x03",

            "#063FUmm... Do you know how Kevin's doing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_100C")

    ChrTalk(    #33
        0x101,
        (
            "#1000FHe's fine, I think.\x02\x03",

            "#1016FHe's got Josette looking after him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_100C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1064")

    ChrTalk(    #34
        0x101,
        (
            "#1012FHe's fine, I think.\x02\x03",

            "#1000FHe's got Kloe looking after him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_1064")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BE")

    ChrTalk(    #35
        0x101,
        (
            "#1000FHe's fine, I think.\x02\x03",

            "#1012FHe's got Joshua looking after him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115")

    label("loc_10BE")


    ChrTalk(    #36
        0x101,
        (
            "#1000FHe's fine, I think.\x02\x03",

            "#1012FHe's got both Joshua and Kloe looking\x01",
            "after him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1115")


    ChrTalk(    #37
        0x12,
        (
            "#066FOh, right... \x02\x03",

            "#561FWhew... What a relief.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(    #38
        0x10F,
        (
            "#1440F...I, umm...\x02\x03",

            "#1445F...I'm sorry for worrying you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x12, 0x10F, 300)
    Sleep(500)

    ChrTalk(    #39
        0x12,
        "#064FHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10F, 300)

    ChrTalk(    #40
        0x101,
        "#1015FWhat're you apologizing for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        (
            "#1440F...\x01",
            "...Nothing.\x02\x03",

            "#1446FForget I said anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1016FUh... Okay...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2632)
    TalkEnd(0xFE)
    Jump("loc_2999")

    label("loc_125E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 1)), scpexpr(EXPR_END)), "loc_152F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1407")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132A")

    ChrTalk(    #43
        0x12,
        (
            "#560F...So, anyway...\x02\x03",

            "...while the shadow towers were flat in structure,\x01",
            "the dimensional space we're in is comprised of\x01",
            "several floors, or 'planes.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1401")

    label("loc_132A")

    TurnDirection(0x12, 0x106, 0)

    ChrTalk(    #44
        0x106,
        (
            "#051FStay here and wait for me, got it, shortstuff?\x02\x03",

            "I'll go look into what's goin' on in this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x12,
        (
            "#560FOh, okay!\x02\x03",

            "#067FTake care, promise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x106,
        "#051FCourse I will. Who do you think I am?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 245, 0)

    label("loc_1401")

    OP_A2(0x1)
    Jump("loc_1520")

    label("loc_1407")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149E")

    ChrTalk(    #47
        0x12,
        (
            "#560FWhile the shadow towers were flat in structure,\x01",
            "the dimensional space we're in is comprised of\x01",
            "several floors, or 'planes.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1520")

    label("loc_149E")

    TurnDirection(0x12, 0x106, 0)

    ChrTalk(    #48
        0x106,
        (
            "#051FStay here and wait for me, got it, shortstuff?\x02\x03",

            "I'll go look into what's goin' on in this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        "#067FOkay!\x02",
    )

    CloseMessageWindow()

    label("loc_1520")

    TalkEnd(0xFE)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2999")

    label("loc_152F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_1BA2")
    SetChrFlags(0x12, 0x10)
    TalkBegin(0x12)
    OP_4A(0x1D, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1864")

    ChrTalk(    #50
        0x12,
        (
            "#067FI'm so glad you're okay, Agate!\x02\x03",

            "#560FI was already worried about whether you were\x01",
            "drawn here, but not knowing if you were okay\x01",
            "was--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x1D,
        (
            "#551FOkay, I get it! Stop hugging me!\x02\x03",

            "#050FBesides...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0x1D,
        (
            "#552F...never mind me. You haven't been gettin'\x01",
            "yourself hurt while I was away, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x12,
        (
            "#565FUmm...\x02\x03",

            "N-No. I'm okay...\x02\x03",

            "#067FI had lots of people looking out for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x1D,
        (
            "#053FReally?\x02\x03",

            "#051FWell, that's good.\x02\x03",

            "Now all that's left is to save the other guys who\x01",
            "ended up trapped in stones and get the hell out \x01",
            "of this weird place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x109, 400)
    Sleep(500)

    ChrTalk(    #55
        0x1D,
        (
            "#050FNext time you're heading out, take me with you.\x02\x03",

            "I don't feel like I'm gonna get what's going on\x01",
            "unless I see it all for myself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x1D, 400)

    ChrTalk(    #56
        0x109,
        "#1066FHaha. Daaamn. Someone's motivated.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x12, 400)
    Jump("loc_1B90")

    label("loc_1864")

    TurnDirection(0x12, 0x106, 0)

    ChrTalk(    #57
        0x12,
        (
            "#067FI'm so glad you're okay, Agate!\x02\x03",

            "#560FI was already worried about whether you were\x01",
            "drawn here, but not knowing if you were okay\x01",
            "was--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x106,
        (
            "#551FOkay, I get it! Stop hugging me!\x02\x03",

            "#050FBesides...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x106,
        (
            "#552F...never mind me. You haven't been gettin'\x01",
            "yourself hurt while I was away, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x12,
        (
            "#565FUmm...\x02\x03",

            "N-No. I'm okay...\x02\x03",

            "#067FI had lots of people looking out for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x106,
        (
            "#053FReally?\x02\x03",

            "#051FWell, that's good.\x02\x03",

            "Now all that's left is to save the other guys who\x01",
            "ended up trapped in stones and get the hell out \x01",
            "of this weird place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x109, 400)
    Sleep(500)

    ChrTalk(    #62
        0x106,
        (
            "#050FAnd on that note, what say we get goin'?\x02\x03",

            "I don't feel like I'm really gonna get what's going\x01",
            "on unless I see it all for myself, so let's hop to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x106, 400)

    ChrTalk(    #63
        0x109,
        "#1066FHaha. Daaamn. Someone's motivated.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 245, 0)

    label("loc_1B90")

    OP_A2(0x2631)
    OP_4B(0x1D, 255)
    TalkEnd(0x12)
    SetChrFlags(0x12, 0x10)
    Jump("loc_2999")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_1E8D")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C39")
    Jump("loc_1C7B")

    label("loc_1C39")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C55")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C7B")

    label("loc_1C55")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C71")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C7B")

    label("loc_1C71")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C7B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB3")

    ChrTalk(    #64
        0x12,
        (
            "#062FConsidering we're always traveling using warps\x01",
            "and the cube, it's hard to be sure...\x02\x03",

            "...but it does feel like every time we arrive at\x01",
            "a new plane, we're moving farther and farther\x01",
            "downward.\x02\x03",

            "#065FIt makes me wonder what's at the bottom of\x01",
            "Phantasma.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1E82")

    label("loc_1DB3")


    ChrTalk(    #65
        0x12,
        (
            "#063FWe seem to be getting more familiar over time\x01",
            "with the rules for this place.\x02\x03",

            "#561FNot that we have any real clue just what this\x01",
            "place IS...\x02\x03",

            "...or what the Lord of Phantasma's trying to do \x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E82")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2999")

    label("loc_1E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_2169")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BA")

    ChrTalk(    #66
        0x12,
        (
            "#560FHeehee. I'm so glad we were able to set\x01",
            "Joshua free from his stone.\x02\x03",

            "I've really missed him!\x02\x03",

            "#063FI'm worried we haven't found Estelle yet,\x01",
            "though... It sounds like she's probably in\x01",
            "one of them somewhere, too, after all.\x02\x03",

            "I hope we can find hers soon.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B4")
    TurnDirection(0x12, 0x10D, 400)
    Sleep(300)

    ChrTalk(    #67
        0x12,
        "#063FOh, and Olivier's, too, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10D,
        (
            "#270F...Hmm?\x02\x03",

            "#278FOh, there's no need to say that just because\x01",
            "I'm here.\x02\x03",

            "#277FThat's idiot's prepared for far worse than being\x01",
            "sealed in a stone. If anything, it might even do\x01",
            "him some good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B4")

    OP_A2(0x1)
    Jump("loc_2163")

    label("loc_20BA")


    ChrTalk(    #69
        0x12,
        (
            "#063FI'm sure there are a lot more people out\x01",
            "there stuck in sealing stones and waiting\x01",
            "to be rescued.\x02\x03",

            "#062FWe should hurry and find them so we can\x01",
            "set them free!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2163")

    TalkEnd(0xFE)
    Jump("loc_2999")

    label("loc_2169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_2462")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2200")
    Jump("loc_2242")

    label("loc_2200")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_221C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2242")

    label("loc_221C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2238")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2242")

    label("loc_2238")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2242")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DB")

    ChrTalk(    #70
        0x12,
        (
            "#063FCompared to some of the other mysteries\x01",
            "we've got to solve here, this garden is one\x01",
            "of the easier ones.\x02\x03",

            "We already know the ancient Zemurians had\x01",
            "the ability to make spaces like this because\x01",
            "of the shadow towers, so that's that.\x02\x03",

            "#562FBut how people ended up sealed in stones\x01",
            "and what happened to the capital is a lot\x01",
            "less easy to explain away...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2457")

    label("loc_23DB")


    ChrTalk(    #71
        0x12,
        (
            "#063FUmm... Hmm...\x02\x03",

            "#561F...Nope. I can't wrap my head around any of it.\x02\x03",

            "I wish we had a few more clues to go off of.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2457")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2999")

    label("loc_2462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 0)), scpexpr(EXPR_END)), "loc_26B1")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24F9")
    Jump("loc_253B")

    label("loc_24F9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2515")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_253B")

    label("loc_2515")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2531")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_253B")

    label("loc_2531")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_253B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2639")

    ChrTalk(    #72
        0x12,
        "#063FArtifacts...dimensional spaces...sealing stones...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x12,
        "#562FUrgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10F,
        "#1440F...The poor girl must be hungry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x109,
        "#1068FNot everyone is like you, you know.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_26A6")

    label("loc_2639")


    ChrTalk(    #76
        0x12,
        "#063FArtifacts...dimensional spaces...sealing stones...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77
        0x12,
        "#562F...Hmm...\x02",
    )

    CloseMessageWindow()

    label("loc_26A6")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2999")

    label("loc_26B1")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2741")
    Jump("loc_2783")

    label("loc_2741")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_275D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2783")

    label("loc_275D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2779")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2783")

    label("loc_2779")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2783")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #78
        0x12,
        "#064F...Huh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        (
            "#1079FWhat's up, Tita?\x02\x03",

            "You okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        (
            "#060FOh... It's okay. I'm fine.\x02\x03",

            "I just kind of spaced out a bit... Sorry.\x02\x03",

            "#561FTrying to wrap my brain around all of this is\x01",
            "making my head hurt, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x109,
        (
            "#1060FCan't blame you there. I think we're in the\x01",
            "same boat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x12,
        (
            "#064FTh-That doesn't mean I'm not happy to help\x01",
            "if you need me to, though!\x02\x03",

            "#62FSo if you need me, just let me know. I'll be up\x01",
            "and ready in a flash!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x109,
        "#1066FHaha. Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10F,
        "#1440F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2630)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_2999")

    Return()

    # Function_2_AC end

    def Function_3_299A(): pass

    label("Function_3_299A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_2AB6")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A64")

    ChrTalk(    #85
        0x1B,
        "#812FHaaaaaah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A5E")

    ChrTalk(    #86
        0x101,
        (
            "#1002F(Wow... She's so focused.)\x02\x03",

            "#1006F(I'm gonna have to start training harder\x01",
            "if I don't want my rival to be soaring ahead\x01",
            "of me!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5E")

    OP_A2(0xA)
    Jump("loc_2AAB")

    label("loc_2A64")


    ChrTalk(    #87
        0x1B,
        (
            "#812FI'm just getting warmed up!\x02\x03",

            "#815FI can do better than this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAB")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_485D")

    label("loc_2AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_3311")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EA")
    SetChrFlags(0x1B, 0x10)
    TalkBegin(0x1B)

    ChrTalk(    #88
        0x1B,
        (
            "#813FHmm...\x02\x03",

            "#1312FHmmmmm...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #89
        0x101,
        (
            "#1011FUmm... Anelace?\x02\x03",

            "#1020FWh-What're you doing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B7F")

    ChrTalk(    #90
        0x103,
        "#1525F...Are you still at that, Anelace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1026FA-At what?\x02",
    )

    CloseMessageWindow()

    label("loc_2B7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C25")
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(    #92
        0x103,
        (
            "#1526FWell, you heard what Renne said earlier,\x01",
            "right?\x02\x03",

            "#1522FAbout how this world changes as a result\x01",
            "of what the people inside it want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB3")

    label("loc_2C25")


    ChrTalk(    #93
        0x1C,
        (
            "#1526FWell, you heard what Renne said earlier,\x01",
            "right?\x02\x03",

            "#1522FAbout how this world changes as a result\x01",
            "of what the people inside it want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB3")


    ChrTalk(    #94
        0x101,
        "#1026FYeah, but what does that have to do with this?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D63")

    ChrTalk(    #95
        0x103,
        (
            "#1525FShe's desperately trying to wish a stuffed toy\x01",
            "into existence with the power of her mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC8")

    label("loc_2D63")


    ChrTalk(    #96
        0x1C,
        (
            "#1525FShe's desperately trying to wish a stuffed toy\x01",
            "into existence with the power of her mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC8")

    Sleep(300)
    TurnDirection(0x1B, 0x0, 400)

    ChrTalk(    #97
        0x1B,
        (
            "#812FHey! I'm TRYING to concentrate here!\x02\x03",

            "Can you be a little more quiet?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E3D")
    TurnDirection(0x103, 0x1B, 0)
    Jump("loc_2E42")

    label("loc_2E3D")

    SetChrSubChip(0x1C, 0)

    label("loc_2E42")

    OP_8C(0x1B, 316, 400)
    Sleep(300)
    OP_62(0x1B, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    ChrTalk(    #98
        0x1B,
        (
            "#811FShould I go with a fluffy, beady-eyed Pom...?\x02\x03",

            "Oooh! Or maybe a nice, silky bear? Or a super\x01",
            "soft panda?\x02\x03",

            "#1311FHeehee! There're so many wonderful choices, \x01",
            "I can't decide which to go with... ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B)
    OP_62(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3031")
    Sleep(1000)

    ChrTalk(    #99
        0x103,
        (
            "#1526FConcentrate? You can't even decide what\x01",
            "you want!\x02\x03",

            "#1534FAt least focus on one of them and see how\x01",
            "that goes before getting greedy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30DC")

    label("loc_3031")

    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x1C,
        (
            "#1526FConcentrate? You can't even decide what\x01",
            "you want!\x02\x03",

            "#1534FAt least focus on one of them and see how\x01",
            "that goes before getting greedy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30DC")

    OP_A2(0x264D)
    TalkEnd(0x1B)
    ClearChrFlags(0x1B, 0x10)
    Jump("loc_330E")

    label("loc_30EA")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3239")
    OP_A2(0xA)

    ChrTalk(    #101
        0x1B,
        (
            "#811FShould I go with a fluffy, beady-eyed Pom...?\x02\x03",

            "Oooh! Or maybe a nice, silky bear? Or a super\x01",
            "soft panda?\x02\x03",

            "#1311FHeehee! There're so many wonderful choices, \x01",
            "I can't decide which to go with... ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1019F...She looks happy enough just daydreaming even \x01",
            "without a Gospel to make her dreams come true. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3306")

    label("loc_3239")


    ChrTalk(    #103
        0x1B,
        (
            "#811FShould I go with a fluffy, beady-eyed Pom...?\x02\x03",

            "Oooh! Or maybe a nice, silky bear? Or a super\x01",
            "soft panda?\x02\x03",

            "#1311FHeehee! There're so many wonderful choices, \x01",
            "I can't decide which to go with... ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3306")

    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_330E")

    Jump("loc_485D")

    label("loc_3311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_40B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F15")
    TalkBegin(0xFE)
    OP_4A(0x1D, 255)
    OP_4A(0x1B, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_397B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3366")

    ChrTalk(    #104
        0x1B,
        "#814FOh! Hey, Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3382")

    label("loc_3366")


    ChrTalk(    #105
        0x1B,
        "#814FOh! Hey, Estelle!\x02",
    )

    CloseMessageWindow()

    label("loc_3382")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3404")

    ChrTalk(    #106
        0x106,
        (
            "#053FHey, Anelace...\x02\x03",

            "#051FI heard from Schera earlier you fought the\x01",
            "colonel here a while back. That true?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_347C")

    label("loc_3404")


    ChrTalk(    #107
        0x1D,
        (
            "#051FHey, you heard this thing about Anelace?\x02\x03",

            "#051FApparently, she fought our buddy Colonel\x01",
            "Richard a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_347C")


    ChrTalk(    #108
        0x101,
        "#1004FWhoa. Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x1B,
        (
            "#819FHeehee. Yeah, it's true.\x02\x03",

            "I wasn't expecting it to happen, though.\x01",
            "But it was just a friendly bout, so don't\x01",
            "take it too seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10C,
        (
            "#111FBrigadier General Bright was the one who\x01",
            "arranged for it to happen, incidentally.\x02\x03",

            "#110FI saw no reason to object, so I was happy\x01",
            "to put my swordsmanship to the test.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36B7")

    ChrTalk(    #111
        0x101,
        (
            "#1017FO-Oh, right.\x02\x03",

            "#1015FCome to think of it, I've fought you once before,\x01",
            "too, haven't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#1500FYeah... Although that was a four-on-one battle,\x01",
            "and even then, we barely managed to scrape a\x01",
            "victory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3780")

    label("loc_36B7")


    ChrTalk(    #113
        0x101,
        (
            "#1017FO-Oh, right.\x02\x03",

            "#1015FCome to think of it, I've fought you once before,\x01",
            "too, haven't I?\x02\x03",

            "Although that was a four-on-one battle, and even\x01",
            "then we barely managed to scrape by with a victory...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3780")


    ChrTalk(    #114
        0x10C,
        (
            "#118FHaha... I can't say that occasion is an especially\x01",
            "pleasant memory to me at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3882")
    TurnDirection(0x106, 0x10C, 400)

    ChrTalk(    #115
        0x106,
        (
            "#051FYou learned your swordsmanship under the\x01",
            "old man directly, right?\x02\x03",

            "I'd be down for a one-on-one fight against\x01",
            "you if you are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3911")

    label("loc_3882")

    TurnDirection(0x1D, 0x10C, 400)

    ChrTalk(    #116
        0x1D,
        (
            "#051FYou learned your swordsmanship under the\x01",
            "old man directly, right?\x02\x03",

            "I'd be down for a one-on-one fight against\x01",
            "you if you are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3911")


    ChrTalk(    #117
        0x10C,
        (
            "#495F(I fear you're only setting yourself up for\x01",
            "disappointment by comparing me to him...)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 136, 0)
    Jump("loc_3F04")

    label("loc_397B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39A8")

    ChrTalk(    #118
        0x1B,
        "#814FOh! Hey, Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_39C4")

    label("loc_39A8")


    ChrTalk(    #119
        0x1B,
        "#814FOh! Hey, Estelle!\x02",
    )

    CloseMessageWindow()

    label("loc_39C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A46")

    ChrTalk(    #120
        0x106,
        (
            "#053FHey, Anelace...\x02\x03",

            "#051FI heard from Schera earlier you fought the\x01",
            "colonel here a while back. That true?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB9")

    label("loc_3A46")


    ChrTalk(    #121
        0x1D,
        (
            "#051FHey, you heard this thing about Anelace?\x02\x03",

            "Apparently, she fought our buddy Colonel\x01",
            "Richard a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB9")


    ChrTalk(    #122
        0x101,
        "#1004FWhoa. Really?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B26")

    ChrTalk(    #123
        0x103,
        (
            "#1525FI couldn't believe my ears when I first found out,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B26")


    ChrTalk(    #124
        0x1B,
        (
            "#819FHeehee. Yeah, it's true.\x02\x03",

            "I wasn't expecting it to happen, though.\x01",
            "But it was just a friendly bout, so don't\x01",
            "take it too seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C99")

    ChrTalk(    #125
        0x101,
        (
            "#1017FO-Oh, right.\x02\x03",

            "#1015FCome to think of it, we've fought him once before,\x01",
            "too, haven't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        (
            "#1500FYeah... Although that was a four-on-one battle,\x01",
            "and even then, we barely managed to scrape a\x01",
            "victory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D53")

    label("loc_3C99")


    ChrTalk(    #127
        0x101,
        (
            "#1017FO-Oh, right.\x02\x03",

            "#1015FCome to think of it, I've fought him once\x01",
            "before, too, haven't I?\x02\x03",

            "But that fight was four against one, and even\x01",
            "then we barely scraped by with a victory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E34")

    ChrTalk(    #128
        0x106,
        (
            "#053FWell, you know someone's gonna be tough\x01",
            "when your old man's the one who trained\x01",
            "him with a sword.\x02\x03",

            "#051FI'd be down for a one-on-one fight against\x01",
            "him if he is. Hell, maybe I should go ask him\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F04")

    label("loc_3E34")


    ChrTalk(    #129
        0x1D,
        (
            "#053FWell, you know someone's gonna be tough\x01",
            "when your old man's the one who trained\x01",
            "him with a sword.\x02\x03",

            "#051FI'd be down for a one-on-one fight against\x01",
            "him if he is. Hell, maybe I should go ask him\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F04")

    OP_4B(0x1D, 255)
    OP_4B(0x1B, 255)
    OP_A2(0x264E)
    TalkEnd(0xFE)
    Jump("loc_40B0")

    label("loc_3F15")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401E")

    ChrTalk(    #130
        0x1B,
        (
            "#818FI'd like to think I've become a bit stronger\x01",
            "since I last fought the colonel, too...\x02\x03",

            "Maybe I should ask him for another match?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4018")

    ChrTalk(    #131
        0x10C,
        (
            "#495F(What will it take to make everyone understand\x01",
            "that I'm no longer a colonel...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4018")

    OP_A2(0xA)
    Jump("loc_40A8")

    label("loc_401E")


    ChrTalk(    #132
        0x1B,
        (
            "#818FI'd like to think I've become a bit stronger\x01",
            "since I last fought the colonel, too...\x02\x03",

            "Maybe I should ask him for another match?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A8")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_40B0")

    Jump("loc_485D")

    label("loc_40B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_4628")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_414A")
    Jump("loc_418C")

    label("loc_414A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4166")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_418C")

    label("loc_4166")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4182")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_418C")

    label("loc_4182")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_418C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458F")

    ChrTalk(    #133
        0x1B,
        "#814FOh, Ries! Are you okay now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10F,
        (
            "#1448FI'm fine. I managed to avoid taking any direct\x01",
            "blows in the battle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 5)), scpexpr(EXPR_END)), "loc_42C8")

    ChrTalk(    #135
        0x1B,
        (
            "#819FHeehee. Still, I'm really glad you came for us\x01",
            "when you did.\x02\x03",

            "#816FI don't even want to imagine what would've\x01",
            "happened if you didn't.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4315")

    label("loc_42C8")


    ChrTalk(    #136
        0x1B,
        (
            "#819FHeehee. I knew you'd go and help Kevin out if\x01",
            "he really needed it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4315")


    ChrTalk(    #137
        0x10F,
        (
            "#1446F...Well, I did some serious thinking about what\x01",
            "you said.\x02\x03",

            "#1440FJust as Kevin had his reasons for wanting to be\x01",
            "a knight, I've got my own reasons for becoming\x01",
            "a squire.\x02\x03",

            "#1448FSo...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x1B,
        (
            "#810F...Okay, then.\x02\x03",

            "#1310FNow all we need to do is wait for Kevin to wake\x01",
            "up so you can tell him how you feel! Am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x10F,
        (
            "#1442FYes, you're right.\x02\x03",

            "#1806FAnelace...thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x1B,
        "#811FHeh. Think nothing of it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1015FWow...\x02\x03",

            "#1011FI didn't know you two were so close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x1B,
        (
            "#1311FOh, but I'm sure you know why, though!\x02\x03",

            "#815F#3SIt's because she's so, so, SO CUTE! #2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1016FIs anyone surprised? No? No.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x265E)
    Jump("loc_461D")

    label("loc_458F")


    ChrTalk(    #144
        0x1B,
        (
            "#810FWell, we've freed you, Estelle...\x02\x03",

            "#1310FNow all that's left is to wait for Kevin\x01",
            "to wake up and everything'll be hunky\x01",
            "dory again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_461D")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_485D")

    label("loc_4628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_485D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_478A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46DB")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #145
        0x1B,
        (
            "#814FOh, Schera.\x02\x03",

            "#810FHave you spoken to Ries yet?\x02\x03",

            "#811FShe's kind of unusual, but she seems like\x01",
            "a really interesting person.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_4784")

    label("loc_46DB")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #146
        0x1B,
        (
            "#816FSchera! Let's go over to the library!\x02\x03",

            "There's a weird sister hanging out over there.\x02\x03",

            "#1311FShe's real cute, though. I think you'll like her!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_4784")

    OP_A2(0xA)
    Jump("loc_485D")

    label("loc_478A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_481F")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #147
        0x1B,
        (
            "#818FRies is a little strange, I'll admit...\x02\x03",

            "#811F...but she's also a CUUU-TEE PIE. And that's all\x01",
            "that matters!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_485D")

    label("loc_481F")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #148
        0x1B,
        "#812FHeeey... Are you listening, Schera?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_485D")

    Return()

    # Function_3_299A end

    def Function_4_485E(): pass

    label("Function_4_485E")

    EventBegin(0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1E, 14)
    SetChrSubChip(0x1E, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x16, 6)
    SetChrSubChip(0x16, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x1E, -52160, 1000, -31820, 135)
    SetChrPos(0x16, -52770, 1000, -32640, 135)
    SetChrPos(0xEE, -50000, 1000, -32990, 270)
    SetChrPos(0xEF, -50800, 1000, -34830, 328)
    SetChrPos(0xF0, -49170, 1000, -35040, 300)
    SetChrPos(0xF1, -48960, 1000, -33690, 300)
    SetChrPos(0x109, -51280, 1000, -33640, 322)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-51810, 1000, -32700, 0)
    OP_67(0, 7730, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(270000, 0)
    OP_6E(450, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4956")
    SetChrFlags(0x101, 0x8)

    label("loc_4956")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4969")
    SetChrFlags(0x102, 0x8)

    label("loc_4969")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #149
        (
            "\x07\x05Kevin explained to Joshua that they thought he was the person the nohval\x01",
            "monument's inscription was asking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #150
        0x16,
        (
            "#1505F...\x02\x03",

            "It sounds like the final area is where\x01",
            "that Schwarzritter's waiting for us.\x02\x03",

            "#1503FWhy he specifically wants me to go,\x01",
            "I don't know, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x109,
        (
            "#1065F#12PSeems like he does, though.\x02\x03",

            "#1063FSo, what're you gonna do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x16,
        (
            "#1505FNaturally, I'll be accepting his invitation.\x02\x03",

            "#1502FWe should head back to the monument as soon\x01",
            "as we're fully prepared. Just let me know when\x01",
            "you intend to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x1E,
        "#1003FJoshua...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BD6")

    ChrTalk(    #154
        0x10B,
        "#215FU-Umm...\x02",
    )

    CloseMessageWindow()

    label("loc_4BD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BF9")

    ChrTalk(    #155
        0x105,
        "#1163FJoshua...\x02",
    )

    CloseMessageWindow()

    label("loc_4BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C1D")

    ChrTalk(    #156
        0x107,
        "#063FJ-Joshua...\x02",
    )

    CloseMessageWindow()

    label("loc_4C1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C46")

    ChrTalk(    #157
        0x110,
        "#1300F...You're sure?\x02",
    )

    CloseMessageWindow()

    label("loc_4C46")


    ChrTalk(    #158
        0x16,
        (
            "#1513FI am. No matter what happens, I'll be just fine.\x02\x03",

            "#1500FAll we can do now is keep moving forward,\x01",
            "and that's what I intend to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B22)
    Fade(500)
    EventEnd(0x5)
    OP_4F(0x64, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_67(0, 3620, -10000, 0)
    SetChrChipByIndex(0x1E, 27)
    SetChrSubChip(0x1E, 0)
    OP_44(0x1E, 0x0)
    SetChrFlags(0x1E, 0x4)
    SetChrPos(0x1E, -54150, 2000, -29940, 135)
    SetChrChipByIndex(0x16, 29)
    SetChrSubChip(0x16, 0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -54720, 2000, -30720, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D50")
    SetChrFlags(0x1E, 0x80)

    label("loc_4D50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D63")
    SetChrFlags(0x16, 0x80)

    label("loc_4D63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D76")
    ClearChrFlags(0x101, 0x8)

    label("loc_4D76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D89")
    ClearChrFlags(0x102, 0x8)

    label("loc_4D89")

    Return()

    # Function_4_485E end

    SaveToFile()

Try(main)
