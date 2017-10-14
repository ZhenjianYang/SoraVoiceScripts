from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'E0011_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0011_1 ._SN',
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
        "Function_1_ABA",          # 01, 1
        "Function_2_11C6",         # 02, 2
        "Function_3_20BF",         # 03, 3
        "Function_4_2BE7",         # 04, 4
        "Function_5_41B8",         # 05, 5
        "Function_6_4BAB",         # 06, 6
        "Function_7_4BBD",         # 07, 7
        "Function_8_59CD",         # 08, 8
        "Function_9_6016",         # 09, 9
        "Function_10_6465",        # 0A, 10
        "Function_11_6BD5",        # 0B, 11
        "Function_12_70EB",        # 0C, 12
        "Function_13_7812",        # 0D, 13
        "Function_14_7D6D",        # 0E, 14
        "Function_15_8AF2",        # 0F, 15
        "Function_16_8DF4",        # 10, 16
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3")
    Call(0, 57)

    label("loc_C3")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116310, 0, 3680, 0)
    OP_67(0, 6750, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 115700, 0, 3700, 90)
    SetChrSubChip(0x8, 1)
    OP_0D()

    ChrTalk(    #0
        0x8,
        "#052FEstelle? What's up?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D7")

    ChrTalk(    #1
        0x101,
        (
            "#1016F#6POh, uh, just having my usual walk\x01",
            "around the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#051FAh, right.\x02\x03",

            "Heh. I'm kind of amazed you don't\x01",
            "get bored with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1019F#6PWhy do you treat me like a hyperactive\x01",
            "Pom?\x02\x03",

            "We've just got time before we hit Bose,\x01",
            "is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#051FEnough time for a quick nap, at least.\x02\x03",

            "#552FSo Bose up next, huh.\x02\x03",

            "Ruan, Zeiss, Grancel... Wonder what the\x01",
            "society'll try throwing at us next.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC")

    label("loc_2D7")


    ChrTalk(    #5
        0x101,
        (
            "#1016F#6PAh, yeah.\x02\x03",

            "I always want to wander around when\x01",
            "I get on an airship.\x02\x03",

            "I just can't seem to sit still in my seat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#051FHaha. Yeah, that sounds like you,\x01",
            "all right.\x02\x03",

            "#556FStill, though...sorta surprised you don't\x01",
            "relish the opportunity to take a breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#051FY'know, after all the crazy bullcrap the\x01",
            "society seems to keep throwin' at you.\x02\x03",

            "It wasn't just that mess in Grancel.\x01",
            "It sounds like you ran into their guys\x01",
            "in Ruan and Zeiss, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1025F#6PYeah...\x02\x03",

            "Sounds like you had just as big a fight\x01",
            "on your hands with the Intelligence guys,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#051FEh, it was just a lot of running around.\x02\x03",

            "#552FSo, Bose up next, huh.\x01",
            "Well, after Rolent, at any rate...\x02\x03",

            "Ruan, Zeiss, Grancel... Wonder what else\x01",
            "the society'll try throwing at us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC")


    ChrTalk(    #11
        0x101,
        (
            "#1015F#6PYeah...\x02\x03",

            "'Nothing' would be the best answer, but\x01",
            "I have a feeling we won't be that lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#053FYou too, huh?\x02\x03",

            "#050FWell, let's hit the ground running and\x01",
            "get to investigating those bandits once\x01",
            "we land, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1020F#6PWait, what...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#052FWhy the surprise?\x02\x03",

            "It's possible they're workin' for\x01",
            "the society.\x02\x03",

            "You said it yourself, remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1008F#6PAh, yeah, I did, but...\x02\x03",

            "#1013FCooome to think of it, I don't think that's\x01",
            "all that likely, y'know? Yeah, it's sorta\x01",
            "stupid, haha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "#050F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1016F#6PI mean, we've fought them\x01",
            "a number of times, right?\x02\x03",

            "They didn't really seem to be the kind of\x01",
            "baby-eaters the society usually brings on.\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#053F...Well, whatever.\x02\x03",

            "#051FI'm sure we'll hear the details from\x01",
            "old Lugran when we get to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1007F#6PYeah... Yeah, we will.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1807)
    SetChrSubChip(0x8, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_AB9")

    label("loc_939")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C9")
    Jump("loc_A0B")

    label("loc_9C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E5")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0B")

    label("loc_9E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A01")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0B")

    label("loc_A01")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A0B")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #20
        0x8,
        (
            "#053FRecapturing an airship, huh?\x01",
            "That'll be tricky.\x02\x03",

            "#051FI'm sure we'll hear the details from\x01",
            "Lugran when we get to Bose.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)

    label("loc_AB9")

    Return()

    # Function_0_AA end

    def Function_1_ABA(): pass

    label("Function_1_ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1071")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117000, 0, -150, 0)
    OP_67(0, 6750, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0xC, 1)
    SetChrPos(0x101, 116240, 0, -160, 90)
    OP_0D()

    ChrTalk(    #21
        0xC,
        "#073FAh, Estelle. Where'd you disappear off to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1025F#6POh, um... I just went to get some fresh air.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        (
            "#070FI see.\x02\x03",

            "So I heard we'll be landing in a town\x01",
            "called Rolent on our way.\x02\x03",

            "That's your hometown, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1011F#6PYeah, it is.\x02\x03",

            "Well, to be specific about it, our house\x01",
            "is just a bit outside the city limits.\x02\x03",

            "Dad wanted it that way, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "#073FHuh. Interesting.\x02\x03",

            "#071FA house built by Master Cassius...\x01",
            "Must be quite a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1008F#6PI, uh...dunno about that.\x02\x03",

            "I mean, I'm not sure if I'd say it's fabulous or\x01",
            "anything, but it IS really comfy.\x02\x03",

            "It holds lots of memories for me of Dad, Mom...\x01",
            "and Joshua, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        "#572F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1016F#6PNo, Zin, it's okay, really.\x02\x03",

            "#1017FIf we were staying in Rolent,\x01",
            "I'd invite you over.\x02\x03",

            "Next time, for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xC,
        (
            "#070FI'll look forward to it.\x02\x03",

            "By the way, Estelle.\x02\x03",

            "When we arrive in Bose, would you mind\x01",
            "accompanying me on some training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1004F#6PHuh? This seems kinda sudden.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        (
            "#075FBack at the Grancel guildhouse, not only\x01",
            "did I miss the sleep agent in the cookies,\x01",
            "but I was unable to awaken myself.\x02\x03",

            "It's obvious I need to re-train in some\x01",
            "areas I've been neglecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016F#6POh, uh, okay.\x02\x03",

            "#1006FWell, I dunno how good a training partner\x01",
            "I'd be for an A-rank bracer, but...\x02\x03",

            "If you want me, you've got me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        "#071FThat's settled, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1808)
    SetChrSubChip(0xC, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_11C5")

    label("loc_1071")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1101")
    Jump("loc_1143")

    label("loc_1101")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_111D")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1143")

    label("loc_111D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1139")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1143")

    label("loc_1139")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1143")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #34
        0xC,
        (
            "#070FWell, then...\x02\x03",

            "Nothing to do, really, so I think\x01",
            "I'm going to catch a nap.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)

    label("loc_11C5")

    Return()

    # Function_1_ABA end

    def Function_2_11C6(): pass

    label("Function_2_11C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F31")
    EventBegin(0x0)
    OP_44(0xD, 0x0)
    Fade(1000)
    OP_6D(89340, -1000, 53720, 0)
    OP_67(0, 7240, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 89280, -1000, 52860, 270)
    TurnDirection(0xD, 0x101, 0)
    SetChrSubChip(0xD, 0)
    OP_0D()

    ChrTalk(    #35
        0xD,
        "#040F#6PHello, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1011F#4PKloe! So this is where you've been hiding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xD,
        (
            "#041F#6PHaha, yes. It's a lovely view, isn't it?\x02\x03",

            "#542FI'm guessing you're on one of your airship walks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1016F#4PAh, yeah. Kinda felt the need.\x02\x03",

            "#1025F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        (
            "#040F#6P...\x02\x03",

            "#047FWhat's happened to Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0x101,
        (
            "#1020F#4PWHAT?!\x02\x03",

            "H-H-How did you--?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xD,
        (
            "#048F#6PHaha... Thought so.\x02\x03",

            "So that WAS what Nial wanted\x01",
            "to talk to you about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1004F#4P...\x02\x03",

            "#1019FDid you just BAIT me, Princess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "#045F#6PHaha. Well, I am the possible heiress\x01",
            "to a nation.\x02\x03",

            "Let's just say I'm well-educated in\x01",
            "Secret Royal Bargaining Tactics and\x01",
            "leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1007F#4P*sigh* I'm no match for you, really.\x02\x03",

            "#1025FYeah... It's about Joshua, all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "#047F#6PSo Joshua is safe, and even still in the\x01",
            "borders of Liberl.\x02\x03",

            "But there's some element to it that means\x01",
            "you can't be happy about it.\x02\x03",

            "#040FIs that about it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #46
        0xD,
        "#542F#6PUm... That is it, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1007F#4PKloe...you aren't a princess, you're a\x01",
            "freaking mind reader.\x02\x03",

            "#1006FYou ask me, you've got this queen thing\x01",
            "in the bag.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "#045F#6PHaha. Thanks.\x02\x03",

            "#048FStill...that's good. Joshua is safe.\x02\x03",

            "Even knowing he's okay is a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1025F#4PYeah. I was happy to find that out too,\x01",
            "but...\x02\x03",

            "#1003F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xD,
        "#044F#6PEstelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1003F#4PKloe... You remember when we went to\x01",
            "arrest Dalmore, right?\x02\x03",

            "And how Joshua responded when Dalmore\x01",
            "threatened me with that gun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        "#042F#6PI...do, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1026F#4PIf I said that Joshua's eyes are like that,\x01",
            "right now...\x02\x03",

            "What would you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xD,
        (
            "#043F#6POh...\x02\x03",

            "#049FI'd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1007F#4PEr, sorry, Kloe.\x02\x03",

            "I shouldn't really drop questions like\x01",
            "that on you without context.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "#047F#6PNo... It's fine.\x02\x03",

            "#040FI can understand, at least a little,\x01",
            "why you're so worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1025F#4PYeah...\x02\x03",

            "#1015F...\x02\x03",

            "#1007FAnd, um, on a note that's absolutely\x01",
            "in no way related at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        "#044F#6PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1013F#4PLike, yeah, totally has nothing to do with\x01",
            "anything, totally hypothetical, but, um.\x02\x03",

            "What would you say if I said, while I'm\x01",
            "here worrying my butt off over him,\x01",
            "he's with another girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "#044F#6P...\x02\x03",

            "#042FHow old?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1007F#4PAbout the same age as us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "#043F#6P...\x02\x03",

            "#047FTo answer this hypothetical question...\x01",
            "I would find myself uninterested in any\x01",
            "excuses Joshua would have to make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1005F#4PI know, right?!\x02\x03",

            "It'd be totally out of line!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        (
            "#042F#6PCertainly.\x02\x03",

            "#047FJust what are you thinking, Joshua...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1019F#4PYeah, my current plan is to have\x01",
            "Olivier sing at him for an hour, and\x01",
            "then we'll hear everything.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0xD)
    Sleep(500)

    ChrTalk(    #66
        0xD,
        "#045F#3P#1KHeehee...\x02",
    )


    ChrTalk(    #67
        0x101,
        "#1016F#4P#1K*snrk*...\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(500)

    ChrTalk(    #68
        0x101,
        (
            "#1008F#4PThanks, Kloe.\x02\x03",

            "I feel a little bit better now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        (
            "#048F#6PHaha... You're welcome, Estelle.\x02\x03",

            "I'm glad I could help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1017F#4POnce I get my head on a bit straighter,\x01",
            "I'll tell everyone what's happened.\x02\x03",

            "Can you keep quiet until then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        (
            "#041F#6POf course.\x02\x03",

            "#040FI think I'll head back to my seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1006F#4POkay, see you later.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)

    def lambda_1E3C():

        label("loc_1E3C")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1E3C")

    QueueWorkItem2(0x101, 2, lambda_1E3C)
    SetChrFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x20)
    OP_8E(0xD, 0x152CA, 0xFFFFFC18, 0xCE72, 0x9C4, 0x0)

    def lambda_1E6B():
        OP_6D(88830, -1000, 50980, 2500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1E6B)
    OP_8E(0xD, 0x1531A, 0xFFFFFC18, 0xC1A2, 0x9C4, 0x0)
    ClearChrFlags(0xD, 0x4)
    OP_8E(0xD, 0x15676, 0x64, 0xABD6, 0x9C4, 0x0)

    def lambda_1EB0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1EB0)
    OP_8E(0xD, 0x1575C, 0x64, 0xA7F8, 0x9C4, 0x0)
    SetChrFlags(0xD, 0x80)
    OP_44(0x101, 0x2)
    Sleep(500)
    Fade(1000)
    OP_6D(89280, -1000, 52860, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1809)
    OP_A3(0x8)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_20BE")

    label("loc_1F31")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FC1")
    Jump("loc_2003")

    label("loc_1FC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FDD")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2003")

    label("loc_1FDD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FF9")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2003")

    label("loc_1FF9")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2003")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(    #73
        0xD,
        (
            "#040FThe dignitaries for the non-aggression\x01",
            "pact signing should be arriving in Grancel\x01",
            "soon.\x02\x03",

            "I hope it goes off without any problems...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)

    label("loc_20BE")

    Return()

    # Function_2_11C6 end

    def Function_3_20BF(): pass

    label("Function_3_20BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6B")
    EventBegin(0x0)
    OP_4A(0xB, 255)
    Fade(1000)
    OP_6D(58860, 0, -1390, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 58800, 0, -870, 180)
    OP_0D()

    ChrTalk(    #74
        0xB,
        "#063F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1004F#6PTita! What'cha doing?\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #76
        0xB,
        (
            "#065F#4POh, Estelle!\x02\x03",

            "#561FUm, I was kind of thinking about things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1015F#6PThings? Like what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xB,
        (
            "#561F#4PWell...um...\x02\x03",

            "#063FEstelle?\x02\x03",

            "I'm not really reliable, am I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1004F#6PHuuuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xB,
        (
            "#062F#4PYou seem like you're worried about\x01",
            "something...\x02\x03",

            "But is it something I can't help with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1003F#6POh. Umm...\x02\x03",

            "#1007FOh, man.\x01",
            "Even Tita sees right through me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xB,
        (
            "#065F#4PI knew it!\x02\x03",

            "#562FI knew it was kinda selfish to ask to come\x01",
            "along, and I'm not really much help...\x02\x03",

            "I... I couldn't even stop Renne...\x02\x03",

            "I'm just holding you back, aren't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1025F#6PTita...\x02\x03",

            "#1016FOh, you little dummy.\x01",
            "You're worried about THAT?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xB,
        "#065F#4PBut, but!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1025F#6PI'm not really...worried, you see.\x01",
            "It's more like I'm confused about something.\x02\x03",

            "I don't think it's really something anyone\x01",
            "can solve for me, so...\x02\x03",

            "I just need some time to think on my own,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xB,
        (
            "#063F#4PBut, Estelle...\x02\x03",

            "Isn't there anything I can do to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1006F#6PYou bet there is.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x40)
    OP_8E(0x101, 0xE57E, 0x0, 0xFFFFF9C0, 0x3E8, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 43)
    SetChrSubChip(0xB, 0)
    OP_99(0xB, 0x0, 0x2, 0x3E8)
    Sleep(500)

    ChrTalk(    #88
        0xB,
        (
            "#064F#4PHuh?\x02\x03",

            "#065FWawawaaaaaaah!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1001F#6PMmmmmmmmm! This is so relaxing.\x02\x03",

            "So soft, so cuddly, so warm...\x01",
            "I could squeeze you aaaaall day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xB,
        "#067F#4PAwww, Esteeeeeelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1017F#6PTita, having you along is a big help,\x01",
            "okay?\x02\x03",

            "I don't just mean your mechanical\x01",
            "knowledge, even though that's part\x01",
            "of it.\x02\x03",

            "Just seeing you smile cheers me\x01",
            "up a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xB,
        "#064F#4POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1006F#6PEven Renne looked like she had\x01",
            "a lot of fun when she was playing\x01",
            "with you, right?\x02\x03",

            "Now, maybe that was all just an\x01",
            "act to fool us so she could do Evil\x01",
            "Ouroboros Stuff, or something...\x02\x03",

            "But you know what?\x01",
            "Somehow, I can't believe it was all\x01",
            "a lie.\x02\x03",

            "You reached her. I know it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xB,
        (
            "#560F#4PYou really think so?\x02\x03",

            "#061FOh... I hope so!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1006F#6PHaha. There's that smile.\x02\x03",

            "Eeeeexcellent.\x01",
            "Your smile is the best, you know!\x02\x03",

            "#1001FNow, you're also cute and huggable\x01",
            "when you're all sniffly and sad, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xB,
        "#067F#4POooh, Estelle...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 5)
    SetChrSubChip(0xB, 0)
    OP_8F(0x101, 0xE57E, 0x0, 0xFFFFFC18, 0x320, 0x0)
    Sleep(500)

    ChrTalk(    #97
        0xB,
        (
            "#560F#4PThank you, Estelle. Thank you...\x02\x03",

            "I'm gonna go back to my seat, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1006F#6POkay! See you in a bit.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    def lambda_29DB():

        label("loc_29DB")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_29DB")

    QueueWorkItem2(0x101, 1, lambda_29DB)
    OP_8E(0xB, 0xE1DC, 0x0, 0xFFFFF7EA, 0x9C4, 0x0)

    def lambda_2A00():
        OP_6D(59600, 0, 2700, 3000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A00)
    OP_8E(0xB, 0xE1BE, 0x0, 0x8B6, 0x9C4, 0x0)
    OP_8E(0xB, 0xEDDA, 0x0, 0x12FC, 0x9C4, 0x0)
    OP_8E(0xB, 0xEE8E, 0xAF0, 0x1FFD, 0x9C4, 0x0)
    SetChrFlags(0xB, 0x80)
    OP_44(0x101, 0x1)
    OP_69(0x101, 0x640)
    OP_A2(0x180A)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_2BE6")

    label("loc_2A6B")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AFB")
    Jump("loc_2B3D")

    label("loc_2AFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B17")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B3D")

    label("loc_2B17")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B33")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B3D")

    label("loc_2B33")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B3D")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #99
        0xB,
        (
            "#560FWe'll be stopping in Rolent soon.\x02\x03",

            "We'll be getting off at Bose, though,\x01",
            "so I guess we still have some time,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)

    label("loc_2BE6")

    Return()

    # Function_3_20BF end

    def Function_4_2BE7(): pass

    label("Function_4_2BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4019")
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0xA, 0x0)
    OP_6D(31780, 0, 6980, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 31650, 0, 6980, 274)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 10)
    ClearChrFlags(0xA, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #100
        0xA,
        (
            "#035FHmm. I see.\x02\x03",

            "#030FNo, actually, the reporter came to talk\x01",
            "to Estelle.\x02\x03",

            "Estelle seemed...bothered after they\x01",
            "spoke. I did wonder wha--\x02\x03",

            "#035FHeh. Well, that answers that.\x02\x03",

            "...\x02\x03",

            "#030FYes, that's fine. We needn't report\x01",
            "anything to the Royal Army yet.\x02\x03",

            "I imagine 'he' has predicted all of this,\x01",
            "anyway.\x02\x03",

            "...\x02\x03",

            "#031FHahaha! I called it perfectly, no?\x02\x03",

            "Well, to be honest, it was little more than\x01",
            "a wild guess. But I suppose even jokes can\x01",
            "be true, sometimes...even the bad ones.\x02\x03",

            "...\x02\x03",

            "#030FI know, I know. You needn't raise your\x01",
            "voice so, my friend.\x02\x03",

            "Regardless, you're to see to our\x01",
            "preparations the moment you return to the\x01",
            "Imperial capital.\x02\x03",

            "#032FYes... So that he might intervene,\x01",
            "if possible.\x02\x03",

            "#035FAs always, you have my 'special' thanks.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrSubChip(0xA, 5)
    OP_0D()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    Fade(500)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 4)
    OP_0D()
    Sleep(500)

    ChrTalk(    #101
        0xA,
        (
            "#035FAh, Joshua.\x01",
            "To think you'd be a match for Mueller!\x02\x03",

            "I suppose I should have expected nothing\x01",
            "less from one of Ouroboros' chosen.\x02\x03",

            "#032FStill, that's one guess I dearly wish\x01",
            "hadn't been true...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 30720, 0, -1440, 0)
    ClearChrFlags(0x101, 0x80)

    ChrTalk(    #102
        0x101,
        "#1PWhat's true now?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_30B3():
        OP_6D(31560, 0, 6450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30B3)

    def lambda_30CB():
        OP_67(0, 7310, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30CB)

    def lambda_30E3():
        OP_6E(282, 3000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_30E3)

    def lambda_30F3():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_30F3)
    TurnDirection(0xA, 0x101, 400)
    OP_8E(0x101, 0x7648, 0x0, 0xA28, 0x9C4, 0x0)
    OP_8E(0x101, 0x7800, 0x0, 0x111C, 0x9C4, 0x0)
    TurnDirection(0x101, 0xA, 400)
    Sleep(500)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #103
        0xA,
        "#033FEr, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1006FAnd what the heck are you whispering\x01",
            "about down here? You and--\x02\x03",

            "#1004FHuh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    TurnDirection(0x101, 0xA, 400)
    Sleep(500)

    ChrTalk(    #105
        0x101,
        "#1015FOlivier, who were you talking to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "#035FAh, whatever could you mean?\x02\x03",

            "#030FDo you truly believe I would engage\x01",
            "in a secret soiree with a woman other\x01",
            "than my Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1019FI can only pray. But c'mon.\x02\x03",

            "I know I heard you talking with someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        (
            "#031FHa-ha-ha! Oh, my!\x02\x03",

            "You heard me talking to myself,\x01",
            "did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1004FTalking...to yourself?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "#035FWell, talking to myself like a madman\x01",
            "wouldn't quite be accurate...\x02\x03",

            "#030FI was going over lines from a play\x01",
            "I once performed in, wherein I was the\x01",
            "leading man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#1020FPlay lines? But why here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        (
            "#034FOur destination, Bose, is the closest\x01",
            "city in Liberl to my homeland.\x02\x03",

            "As we draw closer to it, I must confess\x01",
            "I feel the pull of...homesickness.\x02\x03",

            "I fear that memories of home cannot\x01",
            "help but tumble from my mouth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1026FOh, uh, okay...\x02\x03",

            "#1019FDo you think I have cottage cheese\x01",
            "for a brain or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        "#033FEr. Well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1007FY'know, there're a LOT of suspicious\x01",
            "things about you, Olivier.\x02\x03",

            "I remember you were talking with Dad\x01",
            "about something secret too.\x02\x03",

            "#1009FYou mind coming straight with me\x01",
            "about why you're REALLY here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        (
            "#030FMmm. To think you've become\x01",
            "such a bloodhound for the truth.\x02\x03",

            "#031FYou've grown, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1016FI've had good teachers.\x02\x03",

            "#1002FSo talk already, Mister Erebonian\x01",
            "Suspicious Person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "#035FHm. Allow me to relieve some\x01",
            "of your worries in exchange for\x01",
            "my silence.\x02\x03",

            "I would ask that you grant me\x01",
            "that small favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1004FUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xA,
        (
            "#030FYou are troubled over the theft of the\x01",
            "bandit airship, yes?\x02\x03",

            "I do not think that will prove to be a\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#1020FWhat?! Why not?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xA,
        (
            "#030FYou recall our earlier conversation?\x02\x03",

            "#035FThe fact that the bandits are led by\x01",
            "former Erebonian nobility is an embarrassing\x01",
            "blemish on the Empire's image.\x02\x03",

            "Liberl does not wish to exacerbate the\x01",
            "issue any more than we do, however, as it\x01",
            "could impede the signing of the pact.\x02\x03",

            "#030FSo if anything, the theft of the ship,\x01",
            "at this exact moment, conveniently sweeps\x01",
            "aside a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1015FIs that...really how it would work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xA,
        (
            "#035FWell. If the bandits return to their old\x01",
            "ways in Liberl's skies, that will be a\x01",
            "different story.\x02\x03",

            "I find it unlikely they would be so foolish,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1025FThat's...true.\x02\x03",

            "(If nothing else, Joshua won't\x01",
            "let them steal from others...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #126
        0x101,
        (
            "#1009F...Wait, how do you know they\x01",
            "won't return to piracy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        "#030FWhy did you agree?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1019FErk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xA,
        (
            "#031FHeh. Now, then... I think I shall\x01",
            "return to my seat.\x02\x03",

            "#030FWould you care to join me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1007FI think I'll pass.\x02\x03",

            "#1015F...Hey, Olivier? Can I ask you\x01",
            "one thing before you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xA,
        "#030FNaturally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007FOkay, look, there's a lot I don't know\x01",
            "about you, and you seem to like to keep\x01",
            "your distance from everyone...\x02\x03",

            "#1002FBut even so, I think you're a really\x01",
            "important part of the team.\x02\x03",

            "I believe--and maybe it's crazy as hell,\x01",
            "I dunno, but I do--that I can trust you.\x01",
            "No matter what.\x02\x03",

            "#1013FOh, geez, that came out kind of sappy.\x01",
            "What I'm saying is, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xA,
        "#033F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1019FHey, what's with the drippy,\x01",
            "dinner plate eyes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xA,
        (
            "#033FNo, it's...nothing.\x02\x03",

            "#031FHeh. You touch my heart, my fair Estelle.\x02\x03",

            "You need not fear. I shall not betray your\x01",
            "trust...nor do I find your trust and love a\x01",
            "burden. I give myself gladly to your cause!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1007FUh, 'love' has nothing to do with it...\x02\x03",

            "#1017FBut...thanks, Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xA,
        (
            "#031FOf course.\x02\x03",

            "#030FSo, if you'll pardon me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F45():
        OP_6D(30630, 0, 4390, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F45)

    def lambda_3F5D():
        OP_6C(1000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F5D)

    def lambda_3F6D():

        label("loc_3F6D")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_3F6D")

    QueueWorkItem2(0x101, 1, lambda_3F6D)
    OP_8E(0xA, 0x740E, 0x0, 0x1112, 0x9C4, 0x0)
    OP_8E(0xA, 0x7396, 0x0, 0xFFFFF1FA, 0x9C4, 0x0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    SetChrFlags(0xA, 0x80)
    OP_44(0x101, 0x1)
    Sleep(500)
    Fade(1000)
    OP_6D(30430, 0, 5730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 30430, 0, 5730, 180)
    OP_0D()
    OP_A2(0x180B)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_41B7")

    label("loc_4019")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40A9")
    Jump("loc_40EB")

    label("loc_40A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40C5")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40EB")

    label("loc_40C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40E1")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40EB")

    label("loc_40E1")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40EB")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #138
        0xA,
        (
            "#035FAh, our next stop is Rolent!\x02\x03",

            "#030FI would have loved to enjoy their fresh,\x01",
            "pastoral cuisine again...\x02\x03",

            "Ah, well. There shall always be another time!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)

    label("loc_41B7")

    Return()

    # Function_4_2BE7 end

    def Function_5_41B8(): pass

    label("Function_5_41B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(113330, 200, 4290, 0)
    OP_67(0, 6870, -10000, 0)
    OP_6B(2730, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x16, 60470, -2000, 52850, 0)
    SetChrPos(0x101, 113430, 0, 4430, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #139
        "\x07\x05Thank you for flying with us today.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x32, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x32, 255)

    AnonymousTalk(    #140
        "\x07\x05We will be arriving in Rolent shortly.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_42C9():
        OP_8C(0x32, 0, 500)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_42C9)

    AnonymousTalk(    #141
        (
            "\x07\x05Please be aware that there may be turbulence\x01",
            "while landing, so we ask that all passengers\x01",
            "take their seats.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #142
        0x101,
        "#1004F#6POh, hey!\x02",
    )

    CloseMessageWindow()

    def lambda_436A():
        OP_6D(115290, 0, 2910, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_436A)
    Sleep(500)
    SetChrSubChip(0x9, 1)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #143
        0x9,
        (
            "#020F#4PYou should probably find your seat,\x01",
            "Estelle.\x02\x03",

            "It really is dangerous to stand during\x01",
            "a landing like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        "#1025F#6POkay!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)

    def lambda_4421():
        OP_6D(116550, 0, 2320, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4421)
    OP_8E(0x101, 0x1C764, 0x0, 0x60E, 0x7D0, 0x0)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0x101, 0x4)
    SetChrSubChip(0x101, 0)
    OP_8C(0x101, 0, 400)
    Fade(500)
    SetChrPos(0x101, 116650, 100, 1200, 0)
    SetChrChipByIndex(0x101, 20)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #145
        (
            "\x07\x05Ladies and gentlemen, thank you for flying with\x01",
            "us today.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #146
        (
            "\x07\x05Passengers departing in Rolent, please check\x01",
            "to ensure you haven't left behi--aaaaaah!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0xBB8)

    def lambda_4549():
        OP_6D(116960, 200, 5430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4549)

    def lambda_4561():
        OP_67(0, 4780, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4561)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Fade(1000)
    OP_72(0x3, 0x4)
    OP_0D()
    Sleep(300)

    ChrTalk(    #147
        0x101,
        "#1004F#1PEr, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x9,
        "#023F#2POh, my...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x51)
    Sleep(200)
    Fade(1000)
    OP_6D(59370, -450, 53240, 0)
    OP_67(0, 4630, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #149
        0x1E,
        "#2PWHAT IN THE NAME OF GEHENNA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x1E,
        (
            "#2PHow could we have entered a cloud at this\x01",
            "altitude?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x20,
        (
            "#5PWe didn't enter a cloud, sir! We're descending!\x01",
            "This doesn't seem like a cloud, though,\x01",
            "it's more like--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x1F,
        (
            "#1PCaptain! Transmission from Rolent\x01",
            "Air Traffic Control!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x1F,
        (
            "#1PThe city and surrounding area\x01",
            "has been engulfed in a deep fog!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x1E,
        "#2PWHAT?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x9, 2)
    SetChrSubChip(0x8, 2)
    SetChrSubChip(0xA, 2)
    SetChrSubChip(0xD, 2)
    SetChrSubChip(0xB, 2)
    SetChrSubChip(0xC, 2)
    SetChrPos(0x32, 116140, 0, 11120, 40)
    OP_4B(0x32, 255)
    SetChrPos(0x31, 116790, 0, 10500, 40)
    SetChrChipByIndex(0x31, 46)
    OP_43(0x31, 0x0, 0x0, 0x2)
    OP_6D(118000, 100, 8660, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2730, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(118000, 100, 3330, 3000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #155
        0x101,
        "#1020F#5PWhat the heck...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xB,
        "#064F#6PWow, it's completely white!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        "#030F#6PHm. Did we enter a cloud bank?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x9,
        (
            "#022F#5PPossibly, but...this also seems impossibly\x01",
            "low to be a cloud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xC,
        "#072F#5PIs this...usual when landing an airship?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#552F#6PI sure as hell have never seen\x01",
            "anything like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        "#043F#6PNor have I...\x02",
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #162
        (
            "\x07\x05Ladies and gentlemen, please, um...\x01",
            "remain calm.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #163
        (
            "\x07\x05We've received word from Rolent that a deep\x01",
            "fog has appeared over the entirety of the\x01",
            "city and surrounding area.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #164
        (
            "\x07\x05Air control is currently preparing searchlights\x01",
            "to aid our landing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #165
        "\x07\x05Thank you for your patience.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #166
        0x101,
        (
            "#1015F#5PFog?\x02\x03",

            "Rolent does get fog, but it's usually\x01",
            "just like a thin fuzz, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        (
            "#026F#5PYes. I don't ever remember seeing it\x01",
            "this thick.\x02\x03",

            "#022FThis...really worries me.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_41B8 end

    def Function_6_4BAB(): pass

    label("Function_6_4BAB")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_A2(0x1A79)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_6_4BAB end

    def Function_7_4BBD(): pass

    label("Function_7_4BBD")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(57210, 0, -1640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(57590, 0, -1400, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 57220, 0, -1100, 180)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(    #168
        0x8,
        "#552F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1004F#6PHey...is something wrong, Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        "#053F#6P...It's nothin'.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    Sleep(500)

    ChrTalk(    #171
        0x8,
        "#051F#4PYou still wanderin' around the ship?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DBD")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as Agate was in party at the end of Chapter 4\x01",          # 0
            "Set as Agate was not in party at the end of Chapter 4\x01",      # 1
            "No change\x01",                                                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DB1"),
        (1, "loc_4DB7"),
        (SWITCH_DEFAULT, "loc_4DBD"),
    )


    label("loc_4DB1")

    OP_A2(0x183C)
    Jump("loc_4DBD")

    label("loc_4DB7")

    OP_A3(0x183C)
    Jump("loc_4DBD")

    label("loc_4DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 4)), scpexpr(EXPR_END)), "loc_5141")

    ChrTalk(    #172
        0x101,
        (
            "#1006F#6PYeah, basically.\x02\x03",

            "#1015FOh, um...about earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        "#052F#4PEarlier? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1007F#6PYou know, when we were put to sleep\x01",
            "in Mistwald.\x02\x03",

            "#1025FDid you see some kind of, um...\x01",
            "dream, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        "#552F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1013F#6POh... I see, sorry.\x02\x03",

            "Do you not want to talk about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#053F#4PNah... It's all right.\x02\x03",

            "#051FYeah, I saw a dream.\x02\x03",

            "Heh... It WAS nostalgic as hell,\x01",
            "I'll say that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1016F#6PYou too, huh, Agate?\x02\x03",

            "#1008FSo...um...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#551F#4PY'know, Estelle, you've gotta work on your poker\x01",
            "face and hidin' you want to know stuff.\x01",
            "Ain't good to be that easy to read.\x02\x03",

            "#556FAnyway...it was just some silly memories of\x01",
            "when I was a kid back...back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1016F#6PAh-haha... Umm, sorry about the eagerness.\x02\x03",

            "#1006FBut yeah, now I remember.\x01",
            "You're from Ravennue, right?\x01",
            "In the Bose region?\x02\x03",

            "This'll be your first time back home in\x01",
            "a while, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D3")

    label("loc_5141")


    ChrTalk(    #181
        0x101,
        (
            "#1016F#6PYeah, basically.\x02\x03",

            "#1006FOh, you're from Ravennue in the Bose\x01",
            "region, right?\x02\x03",

            "This'll be your first time back home in\x01",
            "a while, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5280")

    ChrTalk(    #182
        0x8,
        (
            "#052F#4PUh, no. Was there just a bit ago chasin'\x01",
            "down the Intelligence Division guys.\x02\x03",

            "#055F...Hey, wait a second.\x02\x03",

            "Why are you assumin' I'm goin' back home?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_534F")

    label("loc_5280")


    ChrTalk(    #183
        0x8,
        (
            "#051F#4PIt's been a little while, yeah.\x02\x03",

            "I did stop by the old place after the queen's\x01",
            "Birthday Celebration a while back, though.\x02\x03",

            "#055F...Hey, wait a second.\x02\x03",

            "Why are you assumin' I'm goin' back home?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_534F")


    ChrTalk(    #184
        0x101,
        (
            "#1001F#6PAwww, don't be embarrassed,\x01",
            "you big teddy bear!\x02\x03",

            "#1006FYou've got a little sister back in Ravennue,\x01",
            "right? You mentioned her once.\x02\x03",

            "#1028FHehehe... You must be the biggest softy\x01",
            "when it comes to her, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x8,
        "#555F#4PUh. Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1004F#6POh, yeah, where the heck in Ravennue is\x01",
            "your house, anyway?\x02\x03",

            "#1015FI don't remember meeting any girl who stood\x01",
            "out as 'Agate's little sister' when we\x01",
            "were there investigating the sky bandits.\x02\x03",

            "There was a girl with Lewey, but...no,\x01",
            "too young, and I figure your little sister's\x01",
            "GOTTA have your hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#051F#4PI'll...introduce you to Mischa soon.\x02\x03",

            "Assuming we have some reason to visit,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1016F#6PYeah! Please do.\x02\x03",

            "#1006FAnd in that case, we'll have to\x01",
            "bring Tita along, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        "#055F#4PWh-Why would we have to do that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#1006F#6PTita's kind of attached to you, in case you\x01",
            "hadn't noticed!\x02\x03",

            "She'd be pretty let down if you didn't\x01",
            "introduce her to your sister, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x8,
        "#552F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#1004F#6POH! I get it!\x02\x03",

            "#1028FYou don't want Mischa and Tita to meet,\x01",
            "hmmmmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x8,
        "#052F#4PWh--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#1016F#6PHaha! Noooow I get it!\x02\x03",

            "#1006FThey might get together and get in lots of trouble\x01",
            "like Tita did with Renne, or they might get\x01",
            "jealous of each other...\x02\x03",

            "#1001FAhhhh, being an older brother must\x01",
            "be hard work. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x8,
        "#053F#4POh... That's what you meant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#1015F#6PHuh?\x02\x03",

            "#1006FWell, don't worry, I'll clean up any mess\x01",
            "that happens. I've gotten pretty good at\x01",
            "Tita-herding!\x02\x03",

            "So you just go ahead and introduce those two,\x01",
            "um, crazy kids and I'll make sure nothing blows\x01",
            "up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#051F#4P...Yeah. Thanks.\x02\x03",

            "I'll be countin' on you for that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A03)
    OP_8C(0x8, 270, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_7_4BBD end

    def Function_8_59CD(): pass

    label("Function_8_59CD")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(90670, 0, 44790, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0xB, 255)
    OP_8C(0xB, 270, 0)
    SetChrPos(0x101, 90160, 0, 44840, 90)
    OP_0D()

    ChrTalk(    #198
        0xB,
        "#061F#4POh, hi, Estelle! Still walking around?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B2D")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as Tita was in party at the end of Chapter 4\x01",          # 0
            "Set as Tita was not in party at the end of Chapter 4\x01",      # 1
            "No change\x01",                                                 # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B21"),
        (1, "loc_5B27"),
        (SWITCH_DEFAULT, "loc_5B2D"),
    )


    label("loc_5B21")

    OP_A2(0x183D)
    Jump("loc_5B2D")

    label("loc_5B27")

    OP_A3(0x183D)
    Jump("loc_5B2D")

    label("loc_5B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 5)), scpexpr(EXPR_END)), "loc_5E3E")

    ChrTalk(    #199
        0x101,
        (
            "#1006F#6PSorta, yeah.\x02\x03",

            "#1015FOh, yeah, Tita, I was wondering.\x02\x03",

            "Did you dream at all when we\x01",
            "were put to sleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xB,
        (
            "#066F#4PYeah, I did!\x02\x03",

            "It was a dream where Mom and Dad came home.\x02\x03",

            "And Mom and Grandpa got into a loving\x01",
            "fistfight for the first time in forever...\x01",
            "*sigh*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        (
            "#1016F#6PUm, I... I seeeee...\x02\x03",

            "#1006FThat still sounds like a really nice dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xB,
        (
            "#067F#4PHeehee... Yeah.\x02\x03",

            "You showed up, of course, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        "#1004F#6PWait, I did?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xB,
        (
            "#560F#4PUh-huh! After Mom and Dad came home...\x02\x03",

            "You and Joshua and Agate all came\x01",
            "by to visit!\x02\x03",

            "Then Grandpa suggested we all take a trip\x01",
            "to the hot springs in Elmo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#1001F#6PHaha! That really does sound like\x01",
            "a fun dream.\x02\x03",

            "#1006FYeah...and now we've just got to make\x01",
            "that dream come true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xB,
        "#061F#4PYeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6005")

    label("loc_5E3E")


    ChrTalk(    #207
        0x101,
        (
            "#1006F#6PSorta, yeah.\x02\x03",

            "#1015FOh, Tita, this is your first time\x01",
            "in Bose, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xB,
        (
            "#560F#4PUh-huh.\x02\x03",

            "I've heard there's a really big store in Bose.\x01",
            "I kind of want to see it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#1006F#6PThe Bose Market, yeah.\x02\x03",

            "Think of it like the department store in\x01",
            "Grancel...but even BIGGER.\x02\x03",

            "It's actually a bunch of different stores\x01",
            "all in one space. It's really busy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xB,
        (
            "#064F#4PWow, that sounds amazing!\x02\x03",

            "#067FHeehee... I hope we arrive in Bose soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6005")

    OP_8C(0xB, 90, 400)
    OP_4B(0xB, 255)
    OP_A2(0x1A04)
    EventEnd(0x0)
    Return()

    # Function_8_59CD end

    def Function_9_6016(): pass

    label("Function_9_6016")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(90670, 0, 44790, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0xB, 255)
    OP_8C(0xB, 270, 0)
    SetChrPos(0x101, 90160, 0, 44840, 90)
    OP_0D()

    ChrTalk(    #211
        0xB,
        (
            "#560F#4POh, Estelle! Have you been to\x01",
            "Ravennue Village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1006F#6PYep! I stopped there once on a job.\x02\x03",

            "#1015FThat's Agate's hometown, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xB,
        (
            "#061F#4PUh-huh, he has a little sister named\x01",
            "Mischa living there.\x02\x03",

            "Agate goes back pretty often, I think.\x01",
            "At least once a year to say hello to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1004F#6PAh, right.\x02\x03",

            "#1006FAgate's little sister, huh?\x02\x03",

            "Must be hard for the poor girl, having\x01",
            "such an antisocial lump for a brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xB,
        (
            "#063F#4PEsteeeelle, that's not nice!\x02\x03",

            "Agate can be, um...blunt?\x01",
            "But he's also really nice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        (
            "#1016F#6PAh, yeah, yeah.\x02\x03",

            "#1017FHe is just kind of clumsy and easily\x01",
            "embarrassed, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xB,
        (
            "#061F#4PHeehee...\x02\x03",

            "#560FYou know, I bet Mischa's a really\x01",
            "good person.\x02\x03",

            "Whenever Agate talks about her,\x01",
            "his eyes turn so gentle...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        "#1004F#6PTita? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xB,
        (
            "#067F#4PNo, it's nothing.\x02\x03",

            "My heart just felt, um...\x01",
            "kind of weird for a bit...\x02\x03",

            "Haha! I wonder why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#1016F#6P(Hmm... Soooomebody's a bit jealous\x01",
            "of Mischa, I bet!)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 90, 400)
    OP_4B(0xB, 255)
    OP_A2(0x1A05)
    EventEnd(0x0)
    Return()

    # Function_9_6016 end

    def Function_10_6465(): pass

    label("Function_10_6465")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(88790, 0, -3030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 88300, 0, -2780, 90)
    SetChrSubChip(0xA, 1)
    OP_0D()

    ChrTalk(    #221
        0xA,
        (
            "#030FAh, Estelle. At last we return to Bose!\x01",
            "The land laden with memories of our\x01",
            "first meeting.\x02\x03",

            "#035FHeh... It makes my heart swell to return\x01",
            "to a place of such sweet nostalgia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        (
            "#1006F#6PShocking as it may be, I kinda have to\x01",
            "agree on the 'heart-swelling memories'\x01",
            "bit...\x02\x03",

            "#1019FAlthough, as I remember it, you were kind\x01",
            "of rude back then.\x02\x03",

            "You said I wasn't attractive and made fun\x01",
            "of me like a schoolboy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xA,
        (
            "#031FYou misunderstand me, my fair rose.\x02\x03",

            "I would only display such cute, bashful\x01",
            "behavior in order to hide feelings of love\x01",
            "unabated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        (
            "#1007F#6PYeah, I'll bet that's it, exactly.\x02\x03",

            "#1009FYou sure didn't waste any time putting\x01",
            "the moves on Schera, as I remember.\x01",
            "Or JOSHUA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xA,
        (
            "#035FWell. Putting that aside.\x02\x03",

            "#030FAs you stand now, your beauty is\x01",
            "incomparable to what it was then.\x02\x03",

            "Yours is a supple, healthy beauty,\x01",
            "with a maiden's gentle virtue.\x02\x03",

            "#031FIndeed, you have grown, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        (
            "#1008F#6POh, um, thank you.\x02\x03",

            "#1013FThough when you put it that way, it's\x01",
            "kind of embarrassing... Please don't\x01",
            "say it like that again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xA,
        (
            "#035FThere is no shame to be had in virtue,\x01",
            "Estelle.\x02\x03",

            "#037FStill, you have but only begun to climb\x01",
            "the ladder of adulthood.\x02\x03",

            "Should you wish to ascend even higher,\x01",
            "I would be more than happy to...assist you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#1019F#6PNo. Thank. You.\x02\x03",

            "If I was ever in a position to ask anyone\x01",
            "about that sort of thing, I'd be a million\x01",
            "times better off asking Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xA,
        (
            "#034FAh! A pity. The things I could teach!\x02\x03",

            "#033FThough...Schera would be the one to...\x02\x03",

            "...\x02\x03",

            "#037F...Ahhhhhh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        "#1005F#6PI'LL REMIND YOU THAT I HAVE A VERY LARGE STICK.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BCA")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as Olivier was in party at the end of Chapter 4\x01",          # 0
            "Set as Olivier was not in party at the end of Chapter 4\x01",      # 1
            "No change\x01",                                                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6BBE"),
        (1, "loc_6BC4"),
        (SWITCH_DEFAULT, "loc_6BCA"),
    )


    label("loc_6BBE")

    OP_A2(0x183E)
    Jump("loc_6BCA")

    label("loc_6BC4")

    OP_A3(0x183E)
    Jump("loc_6BCA")

    label("loc_6BCA")

    SetChrSubChip(0xA, 0)
    OP_A2(0x1A07)
    EventEnd(0x0)
    Return()

    # Function_10_6465 end

    def Function_11_6BD5(): pass

    label("Function_11_6BD5")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(88790, 0, -3030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 88300, 0, -2780, 90)
    SetChrSubChip(0xA, 1)
    OP_0D()

    ChrTalk(    #231
        0x101,
        (
            "#1004F#6POh, yeah.\x02\x03",

            "#1015FOlivier, you were put to sleep there, too.\x02\x03",

            "Did you dream like I did?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        (
            "#033FAh... I suppose I did.\x02\x03",

            "#032FYes... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        "#1026F#6PHuh? Is something wrong, Olivier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xA,
        (
            "#034FWell, I was simply thinking that it was a\x01",
            "shame.\x02\x03",

            "For you see, in my dreams I was in the\x01",
            "company of peerless, beautiful maidens!\x01",
            "Betwixt shapes verily blessed by Aidios!\x02\x03",

            "If you had not awoken me, Estelle, I could\x01",
            "have done this and that and...\x02\x03",

            "#037FPerhaps fate has willfully stirred me at your\x01",
            "arrival. Well? Would you care to discover\x01",
            "that which can only be conceived in dreams?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        (
            "#1001F#6PRemember what I said about my stick?\x01",
            "I can always put you to sleep with it.\x01",
            "Forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xA,
        "#036FEr, no, no, I'm sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        (
            "#1007F#6PFor the love of...\x02\x03",

            "#1003F(Still...Olivier's eyes were so...sad\x01",
            "for a moment.)\x02\x03",

            "(What did he dream of...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xA,
        (
            "#035FAh... You needn't make such a face,\x01",
            "my sweet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xA,
        (
            "#030FIn truth, it was nothing special.\x01",
            "Simply a memory of my boyhood.\x02\x03",

            "Dear Mueller showed up in it, for example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1025F#6PI see...\x02\x03",

            "#1019FThen why the heck couldn't you just\x01",
            "mention that from the start, you perv?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xA,
        (
            "#031FNow, now! Anger unbecomes you,\x01",
            "Lady Estelle.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    OP_A2(0x1A08)
    EventEnd(0x0)
    Return()

    # Function_11_6BD5 end

    def Function_12_70EB(): pass

    label("Function_12_70EB")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116960, 0, 3460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 116470, 0, 3640, 90)
    SetChrSubChip(0xD, 1)
    OP_0D()

    ChrTalk(    #243
        0xD,
        "#040FEstelle. Out for a walk again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        (
            "#1008F#6PAhaha, more or less.\x02\x03",

            "#1007FMore importantly, I'm sorry.\x02\x03",

            "I didn't really open up about Joshua\x01",
            "until the very end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xD,
        (
            "#041FHaha. Don't worry.\x02\x03",

            "#542FStill, that girl with Joshua is one of\x01",
            "the sky bandits, isn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#1019F#6PYeah. She's a cheeky, insulting little punk\x01",
            "by the name of Josette Capua.\x02\x03",

            "She's also the single biggest tomboy I've\x01",
            "ever laid eyes on. And people call ME a\x01",
            "tomboy sometimes! Pfft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xD,
        (
            "#542FI, um, I see...\x02\x03",

            "#045FShe does, um, seem a bit charming,\x01",
            "from the photograph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1007F#6PMmmm. She can be pretty cute if she\x01",
            "keeps her mouth shut.\x02\x03",

            "And she did manage to play a PERFECT\x01",
            "upper-crust girl when we first met her, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xD,
        "#044FI'm sorry?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #250
        (
            "\x07\x05Estelle explained about how she first met Josette\x01",
            "at the mayor's residence in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #251
        0xD,
        (
            "#044FI... I see!\x02\x03",

            "#041FThat is impressively dexterous,\x01",
            "if I may say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        (
            "#1015F#6PWell, it does make sense, since she's\x01",
            "apparently former Erebonian nobility.\x02\x03",

            "Putting on a face like that is her\x01",
            "specialty, I think.\x02\x03",

            "#1007FPeel away the layers, though, and\x01",
            "like I said--at the core she's a cheeky,\x01",
            "classless little punk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xD,
        (
            "#048FHaha... Still, from what I've heard,\x01",
            "I can't really find cause to hate her.\x02\x03",

            "I suspect that if we found a chance to talk,\x01",
            "we might have quite a lot in common.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        (
            "#1019F#6PYeeeeeah, I can't see that happening.\x02\x03",

            "We'd slide off each other like oil and water.\x01",
            "Our personalities wouldn't fit together.\x01",
            "Trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xD,
        "#045FHaha, maybe...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7807")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as Kloe was in party at the end of Chapter 4\x01",          # 0
            "Set as Kloe was not in party at the end of Chapter 4\x01",      # 1
            "No change\x01",                                                 # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_77FB"),
        (1, "loc_7801"),
        (SWITCH_DEFAULT, "loc_7807"),
    )


    label("loc_77FB")

    OP_A2(0x183F)
    Jump("loc_7807")

    label("loc_7801")

    OP_A3(0x183F)
    Jump("loc_7807")

    label("loc_7807")

    SetChrSubChip(0xD, 0)
    OP_A2(0x1A09)
    EventEnd(0x0)
    Return()

    # Function_12_70EB end

    def Function_13_7812(): pass

    label("Function_13_7812")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116960, 0, 3460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 116470, 0, 3640, 90)
    SetChrSubChip(0xD, 1)
    OP_0D()

    ChrTalk(    #256
        0x101,
        (
            "#1004F#6POh, um...\x02\x03",

            "#1015FKloe, you were put to sleep with\x01",
            "us back there.\x02\x03",

            "Did you have some kind of dream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xD,
        "#542FI did... It was during the Hundred Days War.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        (
            "#1004F#6PDuring the war?\x02\x03",

            "#1025FOh, I see.\x01",
            "That's when you were with Matron Theresa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xD,
        (
            "#040FYes, I was in the care of Matron Theresa\x01",
            "during the fighting. We lived together for\x01",
            "some time.\x02\x03",

            "#045FAnd... Heehee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        "#1004F#6PUm, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xD,
        (
            "#048FIt's just that, even though it was set ten\x01",
            "years ago, Clem and Jill both showed up.\x02\x03",

            "If I had stayed in the dream long enough,\x01",
            "perhaps even you and Joshua might have\x01",
            "appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#1016F#6PAhaha, well, that's a dream for you.\x01",
            "Coherence not guaranteed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xD,
        (
            "#045FHaha, very!\x02\x03",

            "#043FStill...in hindsight, it was a little\x01",
            "frightening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        "#1026F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xD,
        (
            "#049FIn the dream, I was...happy.\x01",
            "Very, very happy.\x02\x03",

            "I wanted everything to stay that way from\x01",
            "the bottom of my heart.\x02\x03",

            "#043FBut...that isn't right, is it?\x01",
            "Simply wishing to escape reality in that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        (
            "#1007F#6PYeah, I know what you mean.\x02\x03",

            "#1002FIt's always nice to have a happy dream,\x01",
            "sure.\x02\x03",

            "But...yeah, if you asked if I wanted to see\x01",
            "that dream again? I'd be a little hesitant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xD,
        (
            "#047FYes...\x02\x03",

            "#042FThe dangers of the Gospel...\x02\x03",

            "I feel like we've gotten a real hint of them.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    OP_A2(0x1A0A)
    EventEnd(0x0)
    Return()

    # Function_13_7812 end

    def Function_14_7D6D(): pass

    label("Function_14_7D6D")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116890, 0, -550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 116390, 0, -360, 90)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(    #268
        0xC,
        (
            "#071FOh, Estelle! Good work this time.\x02\x03",

            "You're really growing as a bracer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#1017F#6PAhaha... I'm still kind of a newbie,\x01",
            "I think.\x02\x03",

            "Like, I'm not even remotely as good with\x01",
            "a staff as Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xC,
        (
            "#070FWell, I don't think you should\x01",
            "worry about Master Cassius much.\x02\x03",

            "#075FAn S-rank bracer is a master of their profession\x01",
            "to a degree that they attain the unity of purpose\x01",
            "all martial artists seek, after all.\x02\x03",

            "To be honest, I don't think I could attain such\x01",
            "enlightenment even if I spent my whole life\x01",
            "trying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        (
            "#1004F#6PI, umm... I see...\x02\x03",

            "#1025FI gotta admit, it's kind of hard for me\x01",
            "to understand how incredible my dad is,\x01",
            "but...\x02\x03",

            "Actually, Zin, you mentioned the whole 'unity of purpose,'\x01",
            "idea to Kloe back at the castle.\x01",
            "What exactly DOES that mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xC,
        (
            "#074FYeah, I did. It's...kinda tough to explain,\x01",
            "to be honest.\x02\x03",

            "#070FWell, here goes. Master Cassius was once such a\x01",
            "transcendent master of the sword, he was\x01",
            "given the title of 'Divine Blade.'\x02\x03",

            "Today, though, he can wield a staff just\x01",
            "as easily as the sword he spent his life\x01",
            "training with.\x02\x03",

            "Why do you think that is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        "#1015F#6PUmm... He practiced really hard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xC,
        (
            "#070FThat's part of it, sure.\x02\x03",

            "But more than that, it is because he could\x01",
            "instantly understand and relate the nature of\x01",
            "staff combat to his previous experience.\x02\x03",

            "#074FSomething beyond what we call 'skill,'\x01",
            "above practicing forms and reflexes,\x01",
            "above muscle memory...\x02\x03",

            "Think of it as a mental state where one can grasp\x01",
            "the true nature of all things and control them at\x01",
            "will...\x02\x03",

            "#072FThat whole concept is what we refer to\x01",
            "as 'unity of purpose.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        "#1002F#6PThe true nature of all things, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xC,
        (
            "#070FHis plan to push back the Imperial Army\x01",
            "during your war was the same, I'd bet.\x02\x03",

            "He understood the nature of war--of combat--\x01",
            "so intrinsically, so instinctively, that he was\x01",
            "able to construct the plan he did.\x02\x03",

            "There would be no one more fearsome as a foe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        (
            "#1007F#6PI get it...I think.\x02\x03",

            "#1002FBut...that means that even my supposedly\x01",
            "enlightened dad was beaten in some ways\x01",
            "by the society.\x02\x03",

            "During the coup he was lured out of the\x01",
            "country, for starters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xC,
        (
            "#072FYeah. They almost certainly possess someone\x01",
            "equal to Master Cassius.\x02\x03",

            "It's hard to know if it's whoever 'Loewe'\x01",
            "is or this 'professor,' though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        (
            "#1015F#6PCould it be the guy we know as 'Lorence'?\x01",
            "He was...pretty powerful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xC,
        (
            "#073FI don't know...\x02\x03",

            "#072FHe IS incredibly skilled, sure, but I doubt\x01",
            "he could match up to Master Cassius.\x02\x03",

            "#572FBesides...his chi. His soul.\x01",
            "They did not have unity of purpose.\x01",
            "Not in the way I have spoken of.\x02\x03",

            "He is a blade, sharpened in one specific way\x01",
            "by the coldest frost, tempered to perfection,\x01",
            "untouched by anyone...\x02\x03",

            "That is the sense I got of him in the arena,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        (
            "#1002F#6PYeah, I get what you mean.\x02\x03",

            "#1007FHe hasn't shown himself, but I figure\x01",
            "he's got to be up to something...\x02\x03",

            "#1003FHe...did seem to have some kind of\x01",
            "fixation on Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xC,
        (
            "#072FIt wouldn't surprise me if they know\x01",
            "each other from Joshua's days in\x01",
            "the society.\x02\x03",

            "#074FBetween him, me, and Scherazard,\x01",
            "we've all got some strange ties in our past\x01",
            "to this group.\x02\x03",

            "I wonder if this is the guidance of\x01",
            "She Who Dwells Above...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AE7")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as Zin was in party at the end of Chapter 4\x01",          # 0
            "Set as Zin was not in party at the end of Chapter 4\x01",      # 1
            "No change\x01",                                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8ADB"),
        (1, "loc_8AE1"),
        (SWITCH_DEFAULT, "loc_8AE7"),
    )


    label("loc_8ADB")

    OP_A2(0x1840)
    Jump("loc_8AE7")

    label("loc_8AE1")

    OP_A3(0x1840)
    Jump("loc_8AE7")

    label("loc_8AE7")

    SetChrSubChip(0xC, 0)
    OP_A2(0x1A0B)
    EventEnd(0x0)
    Return()

    # Function_14_7D6D end

    def Function_15_8AF2(): pass

    label("Function_15_8AF2")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116890, 0, -550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 116390, 0, -360, 90)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(    #283
        0x101,
        (
            "#1004F#6POh, that reminds me.\x02\x03",

            "#1015FZin, you were put to sleep\x01",
            "with the rest of us.\x02\x03",

            "Did you see a dream of some sort\x01",
            "when that happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xC,
        (
            "#070FMmm, yes.\x01",
            "It was a dream of my days at the dojo.\x02\x03",

            "#071FMade me realize that Kilika hasn't changed\x01",
            "much over the years, to start with.\x02\x03",

            "Even in the dream, I had to laugh at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        "#1011F#6PHuh! So Kilika's always been...um, like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xC,
        (
            "#070FYes, 'like that' is a good way to put it.\x02\x03",

            "I always thought it was unbelievable that\x01",
            "she and Walter, of all people, had\x01",
            "gotten toge--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x101,
        "#1004F#6PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xC,
        (
            "#075F...That was a slip of the mouth.\x02\x03",

            "#070FSorry, but forget that. Please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        "#1013F#6PY-Yeah, sure.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    OP_A2(0x1A0C)
    EventEnd(0x0)
    Return()

    # Function_15_8AF2 end

    def Function_16_8DF4(): pass

    label("Function_16_8DF4")

    EventBegin(0x0)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #290
        "\x07\x05Thank you for flying with us today.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #291
        "\x07\x05We will be arriving in Bose shortly.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #292
        (
            "\x07\x05Please be aware that there may be turbulence\x01",
            "while landing, so we ask that all passengers\x01",
            "take their seats.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_8DF4 end

    SaveToFile()

Try(main)
