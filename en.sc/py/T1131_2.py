from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131_2 ._SN',
        MapName             = 'Bose',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        "Function_1_1593",         # 01, 1
        "Function_2_1611",         # 02, 2
        "Function_3_190F",         # 03, 3
        "Function_4_1F18",         # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xA, 255)
    SetChrPos(0xA, -47710, 0, 44840, 270)
    SetChrPos(0x101, -46020, 0, 44370, 270)
    SetChrPos(0xF7, -45610, 0, 45370, 270)
    SetChrPos(0xF8, -44250, 0, 45330, 270)
    SetChrPos(0xF9, -44580, 0, 44110, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127")
    SetChrPos(0x4, -43430, 0, 44650, 270)

    label("loc_127")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_139")
    OP_8C(0xA, 90, 0)

    label("loc_139")

    OP_6D(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as cleared QST018\x01",          # 0
            "Set as not cleared QST018\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E3"),
        (1, "loc_1EB"),
        (SWITCH_DEFAULT, "loc_1F3"),
    )


    label("loc_1E3")

    OP_28(0x12, 0x4, 0x10)
    Jump("loc_1F3")

    label("loc_1EB")

    OP_28(0x12, 0x3, 0x10)
    Jump("loc_1F3")

    label("loc_1F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_2AF")

    ChrTalk(    #0
        0xA,
        "Bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        "Are you ready to talk about the job?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AC")

    ChrTalk(    #2
        0x101,
        (
            "#1007F#7PEh, we probably shouldn't yet.\x02\x03",

            "#1002FBut we'll be back, I promise!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x1000)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    label("loc_2AC")

    Jump("loc_621")

    label("loc_2AF")

    ClearChrFlags(0xA, 0x10)
    OP_8C(0xA, 90, 400)

    ChrTalk(    #3
        0xA,
        "Yes, what is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_40C")

    ChrTalk(    #4
        0x101,
        (
            "#1000F#7PUh, yeah, hi.\x01",
            "We saw your posting on the guild board.\x02\x03",

            "You're Gwen, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        "That's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        "Yes? ...Oh, wait, I know you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "Aren't you the ones who got ingredients\x01",
            "for us a while back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1017F#7PYep, that's us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "Haha, hello! It would seem our fates\x01",
            "are intertwined.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A2")

    label("loc_40C")


    ChrTalk(    #10
        0x101,
        (
            "#1000F#7PSo, I saw your posting on the guild\x01",
            "board.\x02\x03",

            "You're Gwen, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        "Yes, I'm Gwen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xA,
        (
            "You're bracers, no?\x01",
            "I've been waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A2")


    ChrTalk(    #13
        0xA,
        "Shall we get down to the details?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_621")

    ChrTalk(    #14
        0x101,
        (
            "#1006F#7PSure thing...\x02\x03",

            "#1007F...is what I'd LIKE to say, but we've\x01",
            "actually got urgent business to take\x01",
            "care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        "Of course. The dragon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "I won't keep you, then.\x01",
            "Come see me when you have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        (
            "It's not that dire, so please\x01",
            "don't feel the need to rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1002F#7PSorry. We'll be back!\x02",
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x1000)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    label("loc_621")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_6AF")

    ChrTalk(    #19
        0x101,
        (
            "#1007F#7PSorry, not yet.\x02\x03",

            "We'll be back, though!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_752")

    label("loc_6AF")


    ChrTalk(    #20
        0x101,
        (
            "#1015F#7PUmm, sorry, I don't think we have\x01",
            "time right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "I understand, then.\x01",
            "Return when you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1007F#7PSorry. We'll be back!\x02",
    )

    CloseMessageWindow()

    label("loc_752")

    OP_28(0x7B, 0x1, 0x1000)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    label("loc_76A")


    ChrTalk(    #24
        0x101,
        (
            "#1006F#7PSure!\x02\x03",

            "#1015FSo this is a job to collect\x01",
            "ingredients, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        "That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "I need some rare ingredients for research\x01",
            "into new frontiers of cooking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "And I'm going to need you to\x01",
            "go gather them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_8D3")

    ChrTalk(    #28
        0xA,
        (
            "It's not really an emergency, per se,\x01",
            "but I AM running out of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "So the sooner you can take care\x01",
            "of it, the better!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A53")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_965")

    ChrTalk(    #30
        0xA,
        (
            "Everyone's busy with the dragon\x01",
            "incident, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "It isn't terribly urgent, so feel\x01",
            "free to hold off until you have\x01",
            "more time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A53")

    label("loc_965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_9FA")

    ChrTalk(    #32
        0xA,
        (
            "You're terribly busy with all the\x01",
            "goings-on, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "It isn't terribly urgent, so feel\x01",
            "free to hold off until you have\x01",
            "more time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A53")

    label("loc_9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_A53")

    ChrTalk(    #34
        0xA,
        (
            "It isn't terribly urgent, so feel\x01",
            "free to hold off until you have\x01",
            "more time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A53")


    ChrTalk(    #35
        0x101,
        "#1006F#7PAll right, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFE")

    ChrTalk(    #36
        0x106,
        (
            "#050FI think we could use some advice on\x01",
            "collectin' this stuff.\x02\x03",

            "Some of the ingredients on the list\x01",
            "are pretty rare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9E")

    label("loc_AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B70")

    ChrTalk(    #37
        0x103,
        (
            "#020FCould you give us any idea where\x01",
            "we might find these?\x02\x03",

            "This list is kind of...obscure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9E")

    label("loc_B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C08")

    ChrTalk(    #38
        0x108,
        (
            "#070FIf you could give us some advice on\x01",
            "where to find these, that would\x01",
            "help, as well.\x02\x03",

            "Some of the ones listed seem quite rare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9E")

    label("loc_C08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9E")

    ChrTalk(    #39
        0x104,
        (
            "#030FAh, but could you perhaps direct us\x01",
            "to a good starting point for our search?\x02\x03",

            "Many of the items on your list seem\x01",
            "quite rare.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9E")


    ChrTalk(    #40
        0x101,
        (
            "#1011F#7PYeah, that's a good point.\x02\x03",

            "#1015F'Juicy Bones,' for example, are kinda\x01",
            "hard to get. At least the ones you want,\x01",
            "uh, intact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "The most difficult ones will be\x01",
            "'Juicy Bones' and 'Curative Horns.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "The 'Lucky Fangs' will be a bit\x01",
            "easier, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1002F#7PIs this all available in the Bose region?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "Yes, the monsters around here should\x01",
            "drop them in reasonable quantities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "You can get good bones in Nebel Valley,\x01",
            "I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "Horns are at their toughest north of\x01",
            "Ravennue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "And you can find fanged monsters\x01",
            "in the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1007F#7PThat's, uh, kind of spread out.\x02\x03",

            "This is gonna involve a lot of walking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        "Well, that's the idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "This very difficulty is why I need\x01",
            "assistance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1008F#7PYou...do have a point there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        (
            "Once you have all the ingredients,\x01",
            "bring them here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        "I'd like to receive them all at once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "If you bring them piecemeal, I'll just\x01",
            "send you right back out to get the rest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1006F#7PSo just deliver it all in one go?\x02\x03",

            "Honestly, I think that's easier on us\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1187")

    ChrTalk(    #56
        0x109,
        (
            "#1066FWell, we ain't planning on gnawing at\x01",
            "them or anything, so no problem.\x02\x03",

            "Though we'd better be careful not to\x01",
            "accidentally use 'em in any recipes\x01",
            "till we get 'em back here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1450")

    label("loc_1187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1234")

    ChrTalk(    #57
        0x104,
        (
            "#035FHeh, I doubt we plan on eating them,\x01",
            "either, no?\x02\x03",

            "Though we should take care not to\x01",
            "inadvertently mix them in any\x01",
            "recipes we make ere our return.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1450")

    label("loc_1234")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1302")

    ChrTalk(    #58
        0x108,
        (
            "#070FHaha, and it's not like we plan on\x01",
            "eating the ingredients ourselves!\x02\x03",

            "Though we should mind any recipes\x01",
            "we make along the way. Be real unfor-\x01",
            "tunate to throw one in accidentally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1450")

    label("loc_1302")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138B")

    ChrTalk(    #59
        0x103,
        (
            "#027FThat's assuming a certain someone\x01",
            "doesn't snack on them, of course.\x02\x03",

            "Or use them in a recipe along the\x01",
            "way...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1450")

    label("loc_138B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1450")

    ChrTalk(    #60
        0x106,
        (
            "#053FAssuming a certain someone doesn't\x01",
            "snack on 'em, anyway.\x02\x03",

            "We should keep track of what recipes\x01",
            "we prepare on the way back here, too,\x01",
            "and make sure we don't use any of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1450")


    ChrTalk(    #61
        0x101,
        "#1016F#7PAhaha, yeah, uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        (
            "Do you have any other questions?\x01",
            "If not, I must get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1015F#7PLessee, we have the locations we need,\x01",
            "instructions on delivery method...\x02\x03",

            "#1006FNope, I think we're all set!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        "Good luck, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xA,
        "I'll be waiting here.\x02",
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x1)
    OP_28(0x7B, 0x1, 0x2)
    OP_28(0x7B, 0x1, 0x4)
    OP_28(0x7B, 0x4, 0x4)
    OP_28(0x7B, 0x4, 0x8)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    # Function_0_AA end

    def Function_1_1593(): pass

    label("Function_1_1593")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",                  # 0
            "Show Ingredients\x01",      # 1
            "Leave\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FA")
    Call(0, 9)
    Return()

    label("loc_15FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160F")
    Call(2, 2)
    Return()

    label("loc_160F")

    Return()

    # Function_1_1593 end

    def Function_2_1611(): pass

    label("Function_2_1611")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xA, 255)
    SetChrPos(0xA, -47710, 0, 44840, 90)
    SetChrPos(0x101, -46020, 0, 44370, 270)
    SetChrPos(0xF7, -45610, 0, 45370, 270)
    SetChrPos(0xF8, -44250, 0, 45330, 270)
    SetChrPos(0xF9, -44580, 0, 44110, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168E")
    SetChrPos(0x4, -43430, 0, 44650, 270)

    label("loc_168E")

    OP_6D(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #66
        0xA,
        "Oh, do you have the ingredients?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1722")

    ChrTalk(    #67
        0x101,
        "#1002F#7PYeah, have a look.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1743")

    label("loc_1722")


    ChrTalk(    #68
        0x101,
        "#1006F#7PYeah, take a look.\x02",
    )

    CloseMessageWindow()

    label("loc_1743")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #69
        "\x07\x05Estelle showed the gathered ingredients to Gwen.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_17D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D0")
    Call(2, 3)
    Return()

    label("loc_17D0")

    Jump("loc_1823")

    label("loc_17D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1823")
    Call(2, 3)
    Return()

    label("loc_1823")


    ChrTalk(    #70
        0xA,
        "Hmm. Unfortunately...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        "...they're not all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1004F#7PWait, they're not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        "Most assuredly not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        "Please, take another look at the list.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1015F#7PAll right...\x02\x03",

            "Well, uh, we'll be back again.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    # Function_2_1611 end

    def Function_3_190F(): pass

    label("Function_3_190F")


    ChrTalk(    #76
        0xA,
        "Yes, this appears to be everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        "Let me take them off your hands, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1A11")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #78
        "\x07\x00Handed over #935i x10.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #79
        "\x07\x00Handed over #930i x10.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #80
        "\x07\x00Handed over #937i x10.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x3A7, 10)
    OP_3F(0x3A2, 10)
    OP_3F(0x3A9, 10)
    Jump("loc_1B25")

    label("loc_1A11")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #81
        "\x07\x00Handed over #926i x5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #82
        "\x07\x00Handed over #931i x5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #83
        "\x07\x00Handed over #929i x5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #84
        "\x07\x00Handed over #935i x10.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #85
        "\x07\x00Handed over #930i x10.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #86
        "\x07\x00Handed over #937i x10.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x39E, 5)
    OP_3F(0x3A3, 5)
    OP_3F(0x3A1, 5)
    OP_3F(0x3A7, 10)
    OP_3F(0x3A2, 10)
    OP_3F(0x3A9, 10)

    label("loc_1B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CB3")

    ChrTalk(    #87
        0x101,
        (
            "#1002F#7POkay, you got all that?\x02\x03",

            "Now, Gwen... I'm sorry, but we need to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        "You do seem to be in quite a hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        "That dragon, I take it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1002F#7PYeah, there's someplace we need to be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "I see. Don't let me keep you, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "You've been a very big help.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1006F#7PNo problem at all. See you around!\x02\x03",

            "And good luck with your experiment, Gwen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1CB3")


    ChrTalk(    #94
        0x101,
        "#1007F#7PPhew! And that is THAT.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        "Haha! Well done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "Really, thank you for helping me. I know\x01",
            "how busy you are, and it really means\x01",
            "a lot that you're so willing to assist.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1DAA")

    ChrTalk(    #97
        0xA,
        "You even introduced us to Mr. Orvid!\x02",
    )

    CloseMessageWindow()
    OP_2B(0x7B, 0x2)
    OP_2C(0x7B, 0x5DC)

    label("loc_1DAA")


    ChrTalk(    #98
        0x101,
        (
            "#1001F#7PHeehee! Don't worry about it.\x02\x03",

            "I'm just glad we could help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "If you have time, please,\x01",
            "come in again for a bite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        "And good luck in your travels!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1006F#7PYeah, see you.\x02\x03",

            "And good luck with your experiment, Gwen!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #102
        "Quest #2C[The Rarest Flavor] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1EF5")

    OP_28(0x7B, 0x1, 0x20)
    OP_28(0x7B, 0x4, 0x10)
    OP_A2(0x3)
    OP_A2(0xB)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    # Function_3_190F end

    def Function_4_1F18(): pass

    label("Function_4_1F18")

    EventBegin(0x0)
    ClearChrFlags(0x11, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0x11, 255)
    SetChrPos(0xA, -47710, 0, 44840, 90)
    SetChrPos(0x11, -46020, 0, 44840, 270)
    SetChrPos(0x101, -44910, 0, 44600, 270)
    SetChrPos(0xF7, -44680, 0, 45560, 270)
    SetChrPos(0xF8, -43250, 0, 45520, 270)
    SetChrPos(0xF9, -43450, 0, 44560, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FAA")
    SetChrPos(0x4, -42250, 0, 45000, 270)

    label("loc_1FAA")

    OP_6D(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #103
        0xA,
        "Oh, my, yes, the quality is just fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        "Let me take those right now, then!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #105
        (
            "\x07\x05Gwen received Orvid's Juicy Bones, Curative Horns,\x01",
            "and Lucky Fangs.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #106
        0x101,
        (
            "#1000FPhew! That's a big help.\x02\x03",

            "That takes care of all the hardest-to-find\x01",
            "ingredients all at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        "Indeed it does!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        (
            "The remainder will have to fall to you,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1006FNo problem! We can handle the rest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        "Even so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "Mr. Orvid, I must say I'm impressed with your\x01",
            "store of ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x11,
        (
            "Hahaha! But of course!\x02\x03",

            "I specialize in the handling of the finest\x01",
            "ingredients on the continent!\x02\x03",

            "My selection certainly isn't what you'll\x01",
            "find at the corner market!\x02\x03",

            "Should you require anything else, please,\x01",
            "contact me any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        "I'm sure I will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        (
            "I'd like to introduce you to the head chef,\x01",
            "but he's busy at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        "Do you have a little time to wait, perhaps?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x11,
        (
            "Of course! I'll be happy to wait as\x01",
            "long as it takes!\x02\x03",

            "Let me go find a seat.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8E(0x11, 0xFFFF4C0A, 0x0, 0xB518, 0x7D0, 0x0)

    def lambda_23D0():

        label("loc_23D0")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_23D0")

    QueueWorkItem2(0xF6, 1, lambda_23D0)

    def lambda_23E1():

        label("loc_23E1")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_23E1")

    QueueWorkItem2(0xF7, 1, lambda_23E1)

    def lambda_23F2():

        label("loc_23F2")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_23F2")

    QueueWorkItem2(0xF8, 1, lambda_23F2)

    def lambda_2403():

        label("loc_2403")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_2403")

    QueueWorkItem2(0xF9, 1, lambda_2403)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_242B")

    def lambda_2420():

        label("loc_2420")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_2420")

    QueueWorkItem2(0x4, 1, lambda_2420)

    label("loc_242B")

    OP_8E(0x11, 0xFFFF5AA6, 0x0, 0xB518, 0x7D0, 0x0)
    OP_8E(0x11, 0xFFFF5EF2, 0x0, 0xB0C2, 0x7D0, 0x0)
    OP_8E(0x11, 0xFFFF70CC, 0x0, 0xAF28, 0x7D0, 0x0)
    OP_44(0xF6, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2487")
    OP_44(0x4, 0x1)

    label("loc_2487")

    SetChrPos(0x11, -33640, 0, 42550, 0)

    def lambda_249E():
        OP_8C(0xF6, 270, 400)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_249E)

    def lambda_24AC():
        OP_8C(0xF7, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_24AC)
    Sleep(100)

    def lambda_24BF():
        OP_8C(0xF8, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_24BF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E1")

    def lambda_24D9():
        OP_8C(0x4, 270, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_24D9)

    label("loc_24E1")

    OP_8C(0xF9, 270, 400)

    ChrTalk(    #117
        0xA,
        (
            "The rest of the ingredients should\x01",
            "be very simple to get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "Good luck with the rest of it,\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x7B, 0x1, 0x10)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_4B(0x11, 255)
    Return()

    # Function_4_1F18 end

    SaveToFile()

Try(main)
