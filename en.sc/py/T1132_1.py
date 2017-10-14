from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1132_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1132_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
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
        "Function_1_1F6",          # 01, 1
        "Function_2_C56",          # 02, 2
        "Function_3_F6B",          # 03, 3
        "Function_4_2EE5",         # 04, 4
        "Function_5_2F15",         # 05, 5
        "Function_6_2F4A",         # 06, 6
        "Function_7_2F7F",         # 07, 7
        "Function_8_2FC8",         # 08, 8
        "Function_9_2FFD",         # 09, 9
        "Function_10_3074",        # 0A, 10
        "Function_11_44F3",        # 0B, 11
        "Function_12_4543",        # 0C, 12
        "Function_13_467B",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3")
    Return()

    label("loc_C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_DF")
    Call(1, 2)
    Jump("loc_E3")

    label("loc_DF")

    Call(1, 1)

    label("loc_E3")

    Jump("loc_1F5")

    label("loc_E6")

    OP_4A(0xB, 255)
    TalkBegin(0xB)

    ChrTalk(    #0
        0xB,
        (
            "This room is currently in use\x01",
            "by the Imperial ambassador.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xB,
        (
            "If you have no business here,\x01",
            "please refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E4")
    SetChrPos(0x4, -128130, 0, 138000, 270)

    label("loc_1E4")

    OP_69(0xF6, 0x0)
    OP_30(0x0)
    OP_0D()
    TalkEnd(0xB)
    OP_4B(0xB, 255)

    label("loc_1F5")

    Return()

    # Function_0_AA end

    def Function_1_1F6(): pass

    label("Function_1_1F6")

    EventBegin(0x0)
    OP_4A(0xB, 255)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_232")
    TurnDirection(0x4, 0xB, 0)

    label("loc_232")


    ChrTalk(    #2
        0xB,
        (
            "This room is currently in use\x01",
            "by the Imperial ambassador.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "If you have no business here,\x01",
            "please refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_BCB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CA")

    ChrTalk(    #4
        0x106,
        (
            "#052FIs this where we can contact\x01",
            "the Imperial ambassador?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        "Yes, that's correct, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        "Do you have some business with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#050FYou're the ones who have business,\x01",
            "I think.\x02\x03",

            "We're from the Bracer Guild.\x01",
            "We saw your request on the board.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E")

    label("loc_3CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DC")

    ChrTalk(    #8
        0x103,
        (
            "#020FIs this where we can contact\x01",
            "the Imperial ambassador?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        "Yes, that's correct, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        "Do you have some business with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        (
            "#020FYou're the ones who have business\x01",
            "with us, I think.\x02\x03",

            "We're from the Bracer Guild.\x01",
            "You submitted a request, yes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E")

    label("loc_4DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FF")

    ChrTalk(    #12
        0x108,
        (
            "#070FIs this where we can contact\x01",
            "the Imperial ambassador?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        "Yes, that's correct, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        "Do you have some business with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x108,
        (
            "#070FI believe you're the ones who have\x01",
            "business with us.\x02\x03",

            "We're from the Bracer Guild. We came\x01",
            "because of the request you submitted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E")

    label("loc_5FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E")

    ChrTalk(    #16
        0x104,
        (
            "#030FIs this where we can contact\x01",
            "the Imperial ambassador?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        "Yes, that's correct, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        "...Oh, it's you, Olivier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xB,
        (
            "What business do you have with\x01",
            "the ambassador today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1000FYou're the ones who have business,\x01",
            "I think.\x02\x03",

            "We're from the Bracer Guild.\x01",
            "You guys submitted a request...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E")

    label("loc_73E")


    ChrTalk(    #21
        0x101,
        (
            "#1011FIs this where we can contact\x01",
            "the Imperial ambassador?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        "Yes, that's correct, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xB,
        "Do you have some business with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1000FYou're the ones who have business,\x01",
            "I think.\x02\x03",

            "We're from the Bracer Guild.\x01",
            "You guys submitted a request...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83E")


    ChrTalk(    #25
        0xB,
        "Ah, bracers, I see. Pardon me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "If possible, I'd like to have you listen to\x01",
            "an explanation of the case immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        "Do you have the time at the moment?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7E")

    ChrTalk(    #28
        0x101,
        (
            "#1007FUh, s-sorry...\x02\x03",

            "Now that I think about it,\x01",
            "we can't do this right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        "Oh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        (
            "Well, then, when you have finished your\x01",
            "other business, come by again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1000FWe'll do that.\x02\x03",

            "#1015FFor now we need to get to Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A64")
    SetChrPos(0x4, -128130, 0, 138000, 270)

    label("loc_A64")

    OP_69(0xF6, 0x0)
    OP_0D()
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    OP_28(0x78, 0x1, 0x8000)
    Return()

    label("loc_A7E")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AED")

    ChrTalk(    #32
        0x101,
        "#1006FYeah, no problem.\x02",
    )

    CloseMessageWindow()
    Call(1, 3)
    Return()

    label("loc_AED")


    ChrTalk(    #33
        0x101,
        (
            "#1015FSorry, but not right this second.\x02\x03",

            "We've got other business to attend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        "Oh, is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        (
            "Well, then, when you have finished your\x01",
            "other business, come by again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1000FYeah, we'll do that.\x02",
    )

    CloseMessageWindow()
    OP_28(0x78, 0x1, 0x8000)

    label("loc_BCB")

    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")
    SetChrPos(0x4, -128130, 0, 138000, 270)

    label("loc_C42")

    OP_69(0xF6, 0x0)
    OP_0D()
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_1_1F6 end

    def Function_2_C56(): pass

    label("Function_2_C56")

    EventBegin(0x0)
    OP_4A(0xB, 255)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C92")
    TurnDirection(0x4, 0xB, 0)

    label("loc_C92")


    ChrTalk(    #37
        0xB,
        "Everyone, we've been waiting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "Have you finished your other work?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD8")

    ChrTalk(    #39
        0x101,
        (
            "#1007FEr, sorry... Not yet.\x02\x03",

            "#1015FAnyway, we need to hurry to Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBE")
    SetChrPos(0xFA, -128130, 0, 138000, 270)

    label("loc_DBE")

    OP_69(0xF6, 0x0)
    OP_0D()
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    OP_28(0x78, 0x1, 0x8000)
    Return()

    label("loc_DD8")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E47")

    ChrTalk(    #40
        0x101,
        "#1006FYeah, we're fine.\x02",
    )

    CloseMessageWindow()
    Call(1, 3)
    Return()

    label("loc_E47")


    ChrTalk(    #41
        0x101,
        (
            "#1015FAh, sorry.\x02\x03",

            "It'll still take a bit longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "Well, there's nothing we can do, I suppose.\x01",
            "Please come again as soon as you can.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0xB, -126260, 0, 138000, 270)
    SetChrPos(0xF6, -128130, 0, 138000, 270)
    SetChrPos(0xF7, -128130, 0, 138000, 270)
    SetChrPos(0xF8, -128130, 0, 138000, 270)
    SetChrPos(0xF9, -128130, 0, 138000, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F57")
    SetChrPos(0x4, -128130, 0, 138000, 270)

    label("loc_F57")

    OP_69(0xF6, 0x0)
    OP_0D()
    OP_4B(0xB, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_2_C56 end

    def Function_3_F6B(): pass

    label("Function_3_F6B")


    ChrTalk(    #44
        0xB,
        "This way, then, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        "The secretary will explain the details.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xB, 0x1)
    OP_44(0xB, 0x2)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6D(-123540, 0, 180180, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0xB, -130449, 0, 179930, 90)
    SetChrPos(0x101, -131450, 0, 179930, 90)
    SetChrPos(0xF7, -132450, 0, 179930, 90)
    SetChrPos(0xF8, -133450, 0, 179930, 90)
    SetChrPos(0xF9, -134450, 0, 179930, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1082")
    SetChrPos(0x4, -135450, 0, 179930, 90)

    label("loc_1082")

    OP_4A(0xD, 255)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)
    OP_70(0x2, 0xE)

    def lambda_10B9():
        OP_6D(-126280, 0, 181030, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10B9)
    OP_8E(0xB, 0xFFFE0AE8, 0x0, 0x2BDFE, 0x7D0, 0x0)
    OP_8E(0xB, 0xFFFE0A5D, 0x0, 0x2C268, 0x7D0, 0x0)
    OP_8C(0xB, 90, 400)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #46
        0xB,
        "Sir, the bracers have come to attend you.\x02",
    )

    CloseMessageWindow()
    OP_4A(0xA, 255)
    TurnDirection(0xA, 0xB, 400)
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #47
        0xA,
        "#1101FOh, you're here!\x02",
    )

    CloseMessageWindow()

    def lambda_1162():

        label("loc_1162")

        TurnDirection(0xD, 0x101, 400)
        OP_48()
        Jump("loc_1162")

    QueueWorkItem2(0xD, 1, lambda_1162)
    OP_43(0x101, 0x0, 0x1, 0x4)
    OP_43(0xF7, 0x0, 0x1, 0x5)
    OP_43(0xF8, 0x0, 0x1, 0x6)
    OP_43(0xF9, 0x0, 0x1, 0x7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_119C")
    OP_43(0x4, 0x0, 0x1, 0x8)

    label("loc_119C")


    def lambda_11A2():
        OP_6D(-125210, 0, 179480, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11A2)
    OP_8E(0xA, 0xFFFE20C8, 0x0, 0x2BC28, 0x5DC, 0x0)
    OP_8C(0xA, 270, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E3")
    WaitChrThread(0x4, 0x0)
    Jump("loc_11E8")

    label("loc_11E3")

    WaitChrThread(0xF9, 0x0)

    label("loc_11E8")

    OP_44(0xB, 0x1)
    OP_43(0xB, 0x0, 0x1, 0x9)
    OP_44(0xD, 0x1)

    ChrTalk(    #48
        0xA,
        "#1100F#4POh, you are all...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1248")

    ChrTalk(    #49
        0x105,
        "#040FIt's been some time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_126B")

    label("loc_1248")


    ChrTalk(    #50
        0x101,
        "#1011FHey, it's been a while.\x02",
    )

    CloseMessageWindow()

    label("loc_126B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1292")

    ChrTalk(    #51
        0x108,
        "#070FWe meet again.\x02",
    )

    CloseMessageWindow()

    label("loc_1292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E8")

    ChrTalk(    #52
        0x104,
        "#030FHeh, you seem as well as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        "#1100F#4PHm... you too.\x02",
    )

    CloseMessageWindow()

    label("loc_12E8")


    ChrTalk(    #54
        0x101,
        (
            "#1000FUm, thank you very much for\x01",
            "your support in the capital.\x02\x03",

            "#1015FWhat brings you to Bose?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1465")

    ChrTalk(    #55
        0xA,
        (
            "#1102F#4PWith the signing ceremony over\x01",
            "I finally have a somewhat open schedule.\x02\x03",

            "I'd been planning a visit for some time,\x01",
            "and I've finally managed to realize it.\x02\x03",

            "#1100FUnfortunately, thanks to the events at the market\x01",
            "I haven't had as much success as I had hoped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150D")

    label("loc_1465")


    ChrTalk(    #56
        0xA,
        (
            "#1102F#4PWith the signing ceremony over\x01",
            "I finally have a somewhat open schedule.\x02\x03",

            "I'd been planning a visit for some time,\x01",
            "and I've finally managed to realize it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1542")

    ChrTalk(    #57
        0x103,
        "#020FI see, a survey of sorts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15EF")

    label("loc_1542")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157E")

    ChrTalk(    #58
        0x106,
        "#050FAh, got'cha. An inspection trip.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15EF")

    label("loc_157E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15AC")

    ChrTalk(    #59
        0x108,
        "#070FAh, an inspection.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15EF")

    label("loc_15AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(    #60
        0x104,
        "#030FHeh, a little commerce reconnaissance, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_15EF")


    ChrTalk(    #61
        0xA,
        (
            "#1100F#4PHmph, it matters not.\x02\x03",

            "#1101FMore importantly, my medal MUST be recovered!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1004FI-Is it that important?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#1103F#4PBarkley! What are you waiting for?\x02\x03",

            "Hurry up and show it to the bracers!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #64
        0xD,
        "#3PYes, immediately.\x02",
    )

    CloseMessageWindow()
    OP_8E(0xD, 0xFFFE1DC6, 0x0, 0x2B9BC, 0x3E8, 0x0)
    TurnDirection(0xD, 0x101, 400)
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_8E(0xA, 0xFFFE20C8, 0x0, 0x2BC28, 0x5DC, 0x0)
    OP_8C(0xA, 90, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1002FI-It seems like the ambassador's quite,\x01",
            "uh, concerned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        "Well, it's not an unreasonable reaction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        (
            "This event is quite the serious crisis\x01",
            "for the good ambassador.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "After all, that medal is an heirloom of\x01",
            "great honor and glory bestowed directly\x01",
            "from the emperor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        (
            "To have that stolen is a slap directly\x01",
            "to the ambassador's face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xD,
        (
            "Should news of this reach the Fatherland,\x01",
            "the good ambassador would be the laughing\x01",
            "stock of the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1016FThe laughing stock of the capital...\x02\x03",

            "Isn't that a bit, uh, extreme?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xD,
        (
            "Mmm, I'm afraid not.\x01",
            "I love my country dearly, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xD,
        (
            "A blunder like that would be blood\x01",
            "in the water for the high society sharks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        (
            "#4PShould the rumor spread, there is no\x01",
            "doubt that his reputation would take\x01",
            "quite the beating behind the scenes.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#1019FYikes. Talk about nasty.\x02\x03",

            "#1007FErebonian society really is a scary\x01",
            "place, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF3")

    ChrTalk(    #76
        0x107,
        "#561FS-Seriously...\x02",
    )

    CloseMessageWindow()

    label("loc_1AF3")


    ChrTalk(    #77
        0xD,
        "That is the fate of those who live in politics.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        (
            "Do you understand now why we\x01",
            "asked you to come?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BFE")

    ChrTalk(    #79
        0x106,
        (
            "#053FI see. I think I've got it.\x02\x03",

            "#050FSo, what's this thing the ambassador\x01",
            "talked about?\x02\x03",

            "He acted like he wanted to show us something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E23")

    label("loc_1BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB9")

    ChrTalk(    #80
        0x103,
        (
            "#025FMmmm, I believe I get the gist of the situation.\x02\x03",

            "#027FSo, what's this thing the ambassador\x01",
            "was talking about?\x02\x03",

            "He acted like he wanted to show us something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E23")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D6C")

    ChrTalk(    #81
        0x108,
        (
            "#070FI believe I understand the situation.\x02\x03",

            "By the way, what is this thing the\x01",
            "ambassador was talking about?\x02\x03",

            "It felt like he wanted to show us something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E23")

    label("loc_1D6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E23")

    ChrTalk(    #82
        0x104,
        (
            "#030FHeh, the situation is MOST clear.\x02\x03",

            "By the way, just what is this thing\x01",
            "the ambassador was talking about?\x02\x03",

            "He was acting like he wanted to show\x01",
            "us something...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E23")


    ChrTalk(    #83
        0xD,
        "Yes, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xD,
        (
            "There was a card that appeared to be\x01",
            "a declaration of criminal intent left at\x01",
            "the scene.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x101,
        "#1004FA card?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xD,
        "Yes, something like that. Allow me...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x05'Lovely princess and your escorts,\x01",
            "The bell of judgment draws near...\x01",
            "The iron horse's medal is in my hand.'\x02\x03",

            "'Should you desire to reclaim it,\x01",
            "strike through mine riddles.'\x02\x03",

            "'Your first key is the following spell--\x01",
            "RICUL, back the in flower.'\x02\x03",

            "'The end of everything is the beginning.\x01",
            "Heed this well.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_238F")

    ChrTalk(    #88
        0x101,
        (
            "#1007FReally, he puts a lot of work into these.\x02\x03",

            "The guy's so persistent, I can't even\x01",
            "work up the energy to complain.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2192")

    ChrTalk(    #89
        0x108,
        (
            "#070FHaha, that's a sort of enlightenment.\x02\x03",

            "Anyway, we should re-check the\x01",
            "important parts of the card.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238C")

    label("loc_2192")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_221B")

    ChrTalk(    #90
        0x106,
        (
            "#552FYep. Not even worth gettin' worked\x01",
            "up about.\x02\x03",

            "#053FAnyway, we should go over the\x01",
            "important parts of the card.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238C")

    label("loc_221B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22BF")

    ChrTalk(    #91
        0x103,
        (
            "#025F*sigh* That man brings me to\x01",
            "new frontiers of resignation.\x02\x03",

            "#020FAnyway, we should have another look\x01",
            "at the important parts of the card.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238C")

    label("loc_22BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_238C")

    ChrTalk(    #92
        0x104,
        (
            "#030FTo persistently pursue and\x01",
            "eventually outlast your foe...\x02\x03",

            "Heh, truly the ultimate mindset of seduction.\x02\x03",

            "Well, putting that aside, let us have another\x01",
            "look at his curious riddles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238C")

    Jump("loc_262F")

    label("loc_238F")


    ChrTalk(    #93
        0x101,
        (
            "#1019FUgggggh...\x02\x03",

            "Well, no matter how you look at it\x01",
            "it's definitely one of his.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2425")

    ChrTalk(    #94
        0x105,
        "#043F*sigh* It does indeed seem to be his...\x02",
    )

    CloseMessageWindow()

    label("loc_2425")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2471")

    ChrTalk(    #95
        0x104,
        (
            "#035FHeh, a challenge from my rival...\x01",
            "Let us accept it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2471")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F7")

    ChrTalk(    #96
        0x108,
        (
            "#073FThe Phantom Thief... Enforcer of Ouroboros.\x02\x03",

            "#072FI'd heard of him, but he's quite\x01",
            "the twisted man, it seems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253D")

    ChrTalk(    #97
        0x106,
        "#050FWell, let's take a look at the damn thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_262F")

    label("loc_253D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_258C")

    ChrTalk(    #98
        0x103,
        (
            "#022FWell, let us see what can be gleaned\x01",
            "from the card.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_262F")

    label("loc_258C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D5")

    ChrTalk(    #99
        0x107,
        "#560FA-Anyway, let's, um, look at the clues again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_262F")

    label("loc_25D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_262F")

    ChrTalk(    #100
        0x104,
        (
            "#030FMmm... Let us see if we can discern\x01",
            "the import clues on the card.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262F")

    OP_51(0x1E, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2674():
        OP_69(0x1E, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2674)
    OP_8C(0x101, 270, 400)

    def lambda_2689():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2689)
    Sleep(100)

    def lambda_269C():
        TurnDirection(0xF7, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_269C)
    Sleep(150)
    TurnDirection(0xF9, 0x101, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C3")
    TurnDirection(0x4, 0x101, 400)

    label("loc_26C3")

    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #101
        0x101,
        (
            "#1002FOkay. Well, the main point seems to\x01",
            "be this 'RICUL' word.\x02\x03",

            "I think we'll have to start by looking\x01",
            "for what that means.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E7")

    ChrTalk(    #102
        0x106,
        (
            "#050FIn which case, the bits that come\x01",
            "after that will be important.\x02\x03",

            "Most likely those parts will\x01",
            "be the hint to that word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BD")

    label("loc_27E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_288E")

    ChrTalk(    #103
        0x103,
        (
            "#022FIn which case, the bits that come after\x01",
            "that will be just as important.\x02\x03",

            "Most likely those parts will be the\x01",
            "hints to decrypting that word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BD")

    label("loc_288E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2922")

    ChrTalk(    #104
        0x108,
        (
            "#070FIn which case, the bits that come\x01",
            "after that will be important.\x02\x03",

            "Most likely those parts will\x01",
            "be the clues to that word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BD")

    label("loc_2922")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29BD")

    ChrTalk(    #105
        0x104,
        (
            "#030FIn which case, the bits that come\x01",
            "after that will be important.\x02\x03",

            "Most likely those parts will be\x01",
            "the hint to uncovering that word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A2A")

    ChrTalk(    #106
        0x105,
        (
            "#042F...'The end of everything is the beginning,' yes.\x02\x03",

            "It certainly would seem to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2A2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA6")

    ChrTalk(    #107
        0x107,
        (
            "#062FThe part with... 'The end of everything\x01",
            "is the beginning,' right?\x02\x03",

            "Yup, that sounds about right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B15")

    ChrTalk(    #108
        0x104,
        (
            "#030F...'The end of everything is the beginning,' hmm?\x02\x03",

            "It certainly does sound like it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2B15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B7C")

    ChrTalk(    #109
        0x103,
        (
            "#027F...'The end of everything is the beginning.'\x02\x03",

            "It certainly does sound like it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7C")


    ChrTalk(    #110
        0x101,
        (
            "#1002FShould be enough to start with.\x02\x03",

            "First, let's check out the town\x01",
            "using that as a hint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "Do you think you'll be able to investigate\x01",
            "the matter?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C20():
        OP_6D(-125210, 0, 179480, 1000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2C20)

    def lambda_2C38():
        OP_8C(0xF8, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2C38)
    Sleep(100)

    def lambda_2C4B():
        OP_8C(0xF7, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2C4B)
    Sleep(150)
    OP_8C(0x101, 90, 400)

    def lambda_2C65():
        OP_8C(0xF9, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2C65)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C80")
    OP_8C(0x4, 90, 400)

    label("loc_2C80")

    WaitChrThread(0xB, 0x1)

    ChrTalk(    #112
        0x101,
        (
            "#1006FYeah, we should be.\x02\x03",

            "Well, then, if we find anything out,\x01",
            "we'll let you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xD,
        "Yes, we expect good results from you all.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #114
        0xA,
        (
            "#1100F#4PThe investigation shall be underway, then?\x02\x03",

            "We're counting on you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #115
        0x101,
        "#1006FYeah, leave it to us.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x78, 0x4, 0x4)
    OP_28(0x78, 0x4, 0x8)
    OP_28(0x78, 0x1, 0x1)
    OP_28(0x78, 0x1, 0x2)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrPos(0x0, -125660, 0, 179040, 90)
    SetChrPos(0x1, -125660, 0, 179040, 90)
    SetChrPos(0x2, -125660, 0, 179040, 90)
    SetChrPos(0x3, -125660, 0, 179040, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E10")
    SetChrPos(0x4, -125660, 0, 179040, 90)

    label("loc_2E10")

    OP_69(0x0, 0x0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_30(0x0)
    OP_8C(0x101, 90, 0)
    OP_8C(0xF7, 90, 0)
    OP_8C(0xF8, 90, 0)
    OP_8C(0xF9, 90, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E74")
    OP_8C(0xFA, 90, 0)

    label("loc_2E74")

    OP_4A(0x0, 255)
    OP_4A(0x1, 255)
    OP_4A(0x2, 255)
    OP_4A(0x3, 255)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E94")
    OP_4A(0x4, 255)

    label("loc_2E94")

    SetChrPos(0xB, -127460, 0, 181340, 180)
    SetChrPos(0xD, -123490, 0, 178400, 45)
    SetChrPos(0xA, -122680, 0, 179240, 270)
    OP_4B(0xA, 255)
    OP_4B(0xD, 255)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    FadeToBright(1500, 0)
    EventEnd(0x0)
    Return()

    # Function_3_F6B end

    def Function_4_2EE5(): pass

    label("Function_4_2EE5")

    OP_8E(0x101, 0xFFFE0E1C, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0x101, 0xFFFE18C6, 0x0, 0x2BA48, 0x7D0, 0x0)
    OP_8C(0x101, 90, 400)
    Return()

    # Function_4_2EE5 end

    def Function_5_2F15(): pass

    label("Function_5_2F15")

    Sleep(400)
    OP_8E(0xF7, 0xFFFE0E1C, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0xF7, 0xFFFE140C, 0x0, 0x2BDB8, 0x7D0, 0x0)
    OP_8C(0xF7, 90, 400)
    Return()

    # Function_5_2F15 end

    def Function_6_2F4A(): pass

    label("Function_6_2F4A")

    Sleep(800)
    OP_8E(0xF8, 0xFFFE0E1C, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0xF8, 0xFFFE166E, 0x0, 0x2B6BA, 0x7D0, 0x0)
    OP_8C(0xF8, 90, 400)
    Return()

    # Function_6_2F4A end

    def Function_7_2F7F(): pass

    label("Function_7_2F7F")

    Sleep(1200)
    OP_8E(0xF9, 0xFFFE0AF2, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0xF9, 0xFFFE0E1C, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0xF9, 0xFFFE11A0, 0x0, 0x2BADE, 0x7D0, 0x0)
    OP_8C(0xF9, 90, 400)
    Return()

    # Function_7_2F7F end

    def Function_8_2FC8(): pass

    label("Function_8_2FC8")

    Sleep(1600)
    OP_8E(0x4, 0xFFFE0AF2, 0x0, 0x2BEDA, 0x7D0, 0x0)
    OP_8E(0x4, 0xFFFE0E30, 0x0, 0x2B82C, 0x7D0, 0x0)
    OP_8C(0x4, 90, 400)
    Return()

    # Function_8_2FC8 end

    def Function_9_2FFD(): pass

    label("Function_9_2FFD")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xB, 0xFFFE0AE8, 0x0, 0x2BDFE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_72(0x2, 0x800)
    OP_70(0x2, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x2)
    OP_71(0x2, 0x800)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xB, 0xFFFE0AE8, 0x0, 0x2BDFE, 0x7D0, 0x0)
    OP_8E(0xB, 0xFFFE0A5D, 0x0, 0x2C268, 0x7D0, 0x0)
    OP_8C(0xB, 90, 400)
    Return()

    # Function_9_2FFD end

    def Function_10_3074(): pass

    label("Function_10_3074")

    EventBegin(0x0)
    SetChrPos(0x101, -124730, 0, 178760, 90)
    SetChrPos(0xF7, -125890, 0, 178760, 90)
    SetChrPos(0xF8, -125330, 0, 177850, 90)
    SetChrPos(0xF9, -126540, 0, 178170, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30D7")
    SetChrPos(0x4, -127440, 0, 178220, 90)

    label("loc_30D7")

    SetChrPos(0xA, -123450, 0, 178760, 270)
    SetChrPos(0xD, -122420, 0, 179380, 270)
    SetChrPos(0xC, -128419, 0, 180840, 90)
    OP_6D(-125530, 0, 179560, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xA, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_0D()

    ChrTalk(    #116
        0xA,
        (
            "#1101F#4PI-Is it true?!\x02\x03",

            "You really found my medal?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1006F#6PYep, we got it.\x02\x03",

            "Well, here. Showing you is probably the\x01",
            "best way. Let me return it to you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #118
        "Estelle handed over the #2C#16Imedal#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #119
        0xA,
        (
            "#1101F#4POohhh! It truly is my...!\x02\x03",

            "Y-You found it... You really found it!\x02\x03",

            "#1102F*sniffle*\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32DA")
    OP_62(0xF6, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3318")

    label("loc_32DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3301")
    OP_62(0xF6, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3318")

    label("loc_3301")

    OP_62(0xF6, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_3318")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3344")
    OP_62(0xF7, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3382")

    label("loc_3344")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_336B")
    OP_62(0xF7, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3382")

    label("loc_336B")

    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_3382")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A9")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_33E7")

    label("loc_33A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33D0")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_33E7")

    label("loc_33D0")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_33E7")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3413")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3451")

    label("loc_3413")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343A")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3451")

    label("loc_343A")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_3451")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_349A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3483")
    OP_62(0x4, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_349A")

    label("loc_3483")

    OP_62(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_349A")

    Sleep(1000)

    ChrTalk(    #120
        0x101,
        (
            "#1016F#6PI-I hate to interrupt the moment, but...\x02\x03",

            "Is this something-or-other medal\x01",
            "what you were looking for, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0xA,
        (
            "#1101F#4P*gasp*\x02\x03",

            "It's not a 'something-or-other medal'!\x01",
            "It's the Grand Cordon of the Order of\x01",
            "the Winged Stallion!\x02\x03",

            "This is no ordinary medal! It is an\x01",
            "exceptionally high honor that all\x01",
            "long to receive and few ever obtain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1019F#6P#1SWho the heck can remember something\x01",
            "that long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        "#1100F#4PDid you say something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1016F#6PN-No, nothing.\x02\x03",

            "Anyway, it's the right medal, er,\x01",
            "cordon thingy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        (
            "#1100F#4PYes, most definitely.\x02\x03",

            "#1102FThis avoids the worst possible scenario.\x02\x03",

            "Now, if the criminal responsible could just\x01",
            "be punished, things will be settled.\x02\x03",

            "#1100FDo you have an idea who the criminal might be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1015F#6PWe've totally got an idea, but...\x02\x03",

            "#1007FUnfortunately, where they went is\x01",
            "another matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        "#1101F#4PWhat? Is there no way you can capture them?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3908")

    ChrTalk(    #128
        0x106,
        (
            "#050F#6PNot immediately, no.\x02\x03",

            "The one we've got our eyes on as the\x01",
            "culprit is quite the well-known thief.\x02\x03",

            "Have you heard the name 'Phantom Thief B' before?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3A")

    label("loc_3908")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39C7")

    ChrTalk(    #129
        0x103,
        (
            "#026F#6PIt's impossible for now.\x02\x03",

            "I heard that the person that we think\x01",
            "is the culprit is a well known thief.\x02\x03",

            "#027FDoes the name 'Phantom Thief B' ring\x01",
            "a bell for you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3A")

    label("loc_39C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A84")

    ChrTalk(    #130
        0x108,
        (
            "#074F#6PIt's not possible at the moment, I'm afraid.\x02\x03",

            "Our person of interest is reported\x01",
            "to be a well known thief.\x02\x03",

            "#072FDoes 'Phantom Thief B' sound familiar to you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3A")

    label("loc_3A84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B3A")

    ChrTalk(    #131
        0x104,
        (
            "#030F#6PThat, unfortunately, is an impossibility\x01",
            "right now.\x02\x03",

            "Our suspect is an internationally known thief.\x02\x03",

            "Have you ever heard of the name...\x01",
            "'Phantom Thief B'?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3A")

    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #132
        0xA,
        (
            "#1101F#4PPhantom Thief B?!\x02\x03",

            "He's been appearing in Liberl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#1011F#6PAh, so you do know him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "#1100F#4PH-Hmm, yes...\x02\x03",

            "He reigned havoc in the Imperial\x01",
            "capital for some time.\x02\x03",

            "#1102FHe was a man who could not be captured\x01",
            "even by the Imperial Army...\x02\x03",

            "It seems I should be glad that my\x01",
            "medal returned at all this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1003F#6PYeah, seems that way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xA,
        (
            "#1102F#4P...\x02\x03",

            "#1100F...Barkley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xD,
        "Sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xA,
        "#1100F#4PDo you have the item prepared?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xD,
        "Yes, here.\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0xB)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xA, 90, 400)

    ChrTalk(    #140
        0xA,
        "#1100F#3PHm...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_A2(0x16)
    OP_43(0xD, 0x1, 0x1, 0xB)
    Sleep(400)

    def lambda_3D73():
        OP_8C(0xA, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D73)
    WaitChrThread(0xD, 0x1)

    ChrTalk(    #141
        0xA,
        (
            "#1100F#4PWhile I feel some regret that things\x01",
            "did not proceed to capturing him...\x02\x03",

            "Against the infamous Phantom Thief B you\x01",
            "can hardly be blamed.\x02\x03",

            "You recovered my medal in good order\x01",
            "and maintained the dignity of the Empire.\x02\x03",

            "#1102FIn acknowledgment of your great services\x01",
            "to the Empire, I, the Erebonian Imperial\x01",
            "Ambassador--\x02\x03",

            "--grant you this Eisenritter's Medal.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #142
        (
            "\x07\x00Estelle was granted the #316i.\x01",
            "She did her best to keep a straight face.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x13C, 1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_22(0xBF, 0x0, 0x64)

    ChrTalk(    #143
        0xD,
        "Ladies and gentlemen, congratulations!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xC,
        "Congratulations!!\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_63(0xC)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402B")
    OP_62(0xF7, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_4069")

    label("loc_402B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4052")
    OP_62(0xF7, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_4069")

    label("loc_4052")

    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_4069")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4090")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_40CE")

    label("loc_4090")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B7")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_40CE")

    label("loc_40B7")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_40CE")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40FA")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_4138")

    label("loc_40FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4121")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_4138")

    label("loc_4121")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_4138")

    Sleep(1000)

    ChrTalk(    #145
        0x101,
        "#1015F#6PU-Umm...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4191")

    ChrTalk(    #146
        0x105,
        "#045FI certainly wasn't expecting this...\x02",
    )

    CloseMessageWindow()

    label("loc_4191")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41C9")

    ChrTalk(    #147
        0x107,
        "#562FThis is kind of embarrassing...\x02",
    )

    CloseMessageWindow()

    label("loc_41C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41EC")

    ChrTalk(    #148
        0x106,
        "#552FOh, boy...\x02",
    )

    CloseMessageWindow()

    label("loc_41EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4267")

    ChrTalk(    #149
        0x103,
        (
            "#025FTalk about making a big fuss of things...\x01",
            "I suppose this is also part of their\x01",
            "national character.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4267")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42A7")

    ChrTalk(    #150
        0x108,
        "#071FHaha, this is Imperial-style, it seems.\x02",
    )

    CloseMessageWindow()

    label("loc_42A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42E9")

    ChrTalk(    #151
        0x104,
        "#031FIt's not so bad, once you get used to it.\x02",
    )

    CloseMessageWindow()

    label("loc_42E9")


    ChrTalk(    #152
        0xA,
        (
            "#1102F#4PI understand your speechlessness at being\x01",
            "awarded such an honor. It must be very hard\x01",
            "for you to contain yourself.\x02\x03",

            "Ah, sweet youth... I was the same when\x01",
            "I received my first medal.\x02\x03",

            "#1100FHowever, do not feel unworthy. No, your\x01",
            "efforts are more than deserving of this.\x02\x03",

            "#1100FI expect great deeds in the future as is\x01",
            "befitting of one to receive this medal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1016F#6PYeah... Thanks.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #154
        "Quest #2C[Imperial Request] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2)
    OP_28(0x78, 0x1, 0x100)
    OP_28(0x78, 0x4, 0x10)
    OP_4B(0xA, 255)
    OP_4B(0xD, 255)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_10_3074 end

    def Function_11_44F3(): pass

    label("Function_11_44F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4520")
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFE212C, 0x0, 0x2BA20, 0x3E8, 0x0)
    OP_8C(0xFE, 270, 400)
    Jump("loc_4542")

    label("loc_4520")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFE21CC, 0x0, 0x2BCB4, 0x3E8, 0x0)
    OP_8C(0xFE, 270, 400)

    label("loc_4542")

    Return()

    # Function_11_44F3 end

    def Function_12_4543(): pass

    label("Function_12_4543")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4550")
    Return()

    label("loc_4550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4562")
    Return()

    label("loc_4562")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_459D")
    Call(1, 13)
    Jump("loc_4674")

    label("loc_459D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_45AC")
    Call(1, 13)
    Jump("loc_4674")

    label("loc_45AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_461E")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #155
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_4674")

    label("loc_461E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #156
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_4674")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_12_4543 end

    def Function_13_467B(): pass

    label("Function_13_467B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_46FC")

    ChrTalk(    #157
        0x8,
        (
            "Unfortunately, I don't recognize the person\x01",
            "in the photograph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        "I'm terribly sorry I can't be of any help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47F7")

    label("loc_46FC")


    ChrTalk(    #159
        0x8,
        (
            "You're looking for the person in\x01",
            "this photograph?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        "What to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        (
            "It would be different if it was the face of\x01",
            "a customer, but going off a likeness from\x01",
            "ten years ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "My apologies, but I don't think\x01",
            "I can be of any help to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_47F7")

    TalkEnd(0x8)
    Return()

    # Function_13_467B end

    SaveToFile()

Try(main)
