from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2120_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        "Function_1_AF",           # 01, 1
        "Function_2_1818",         # 02, 2
        "Function_3_181D",         # 03, 3
        "Function_4_3ABC",         # 04, 4
        "Function_5_3AC1",         # 05, 5
        "Function_6_4B32",         # 06, 6
        "Function_7_4BCE",         # 07, 7
        "Function_8_5D49",         # 08, 8
        "Function_9_60C3",         # 09, 9
        "Function_10_66BC",        # 0A, 10
        "Function_11_67D1",        # 0B, 11
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Call(1, 1)
    Return()

    # Function_0_AA end

    def Function_1_AF(): pass

    label("Function_1_AF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_104")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E5")
    OP_A9(0x77)
    Jump("loc_E7")

    label("loc_E5")

    OP_A9(0x64)

    label("loc_E7")

    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101")
    TalkEnd(0x9)
    Return()

    label("loc_101")

    Jump("loc_EAB")

    label("loc_104")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAB")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -29500, 0, 2800, 0)
    SetChrPos(0x102, -30300, 0, 2600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B")
    SetChrPos(0xF9, -29900, 0, 1600, 0)
    SetChrPos(0xF8, -30800, 0, 1400, 0)
    Jump("loc_18D")

    label("loc_16B")

    SetChrPos(0xF8, -29900, 0, 1600, 0)
    SetChrPos(0xF9, -30800, 0, 1400, 0)

    label("loc_18D")

    OP_8C(0x9, 180, 0)
    OP_6D(-30100, 0, 3960, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0x9,
        "Sorry, but the factory's closed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "Not much we can do without a single\x01",
            "orbal device working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "They're not broken, either... *sigh*\x01",
            "I wonder what's going on.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F4")

    ChrTalk(    #3
        0x101,
        (
            "#1018F#6POh, right, of course.\x01",
            "Don't worry, though!\x02\x03",

            "I THINK we have a little something to\x01",
            "help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        "Oh, what's that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_88A")

    label("loc_2F4")


    ChrTalk(    #5
        0x101,
        (
            "#1026F#6POhhh, right.\x02\x03",

            "#1015FWell, that's kind of a problem,\x01",
            "isn't it?\x02\x03",

            "If we can't manufacture quartz or\x01",
            "upgrade our slots, we're kinda\x01",
            "in trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E1")

    ChrTalk(    #6
        0x103,
        (
            "#025F#6PYes, at this rate we're just\x01",
            "wasting our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D1")

    label("loc_3E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_430")

    ChrTalk(    #7
        0x108,
        (
            "#072F#6PAt this rate, we're just\x01",
            "wasting our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D1")

    label("loc_430")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D1")

    ChrTalk(    #8
        0x106,
        (
            "#552F#6PKeep in mind we ARE kind of lucky to\x01",
            "even have arts right now.\x02\x03",

            "Does feel like a waste to just be sittin'\x01",
            "on all this sepith, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_547")

    ChrTalk(    #9
        0x107,
        (
            "#064F#6PAh, but, Estelle...\x02\x03",

            "If it's just for a little while,\x01",
            "we might be able to do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B2")

    label("loc_547")


    ChrTalk(    #10
        0x102,
        (
            "#1043F#6PThat's true, but...\x02\x03",

            "#1040FHowever, we may be able to do\x01",
            "something for a short time, anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B2")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62F")

    def lambda_5E2():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5E2)
    Sleep(120)

    def lambda_5F5():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5F5)

    def lambda_603():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_603)
    Sleep(120)

    def lambda_616():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_616)

    def lambda_624():
        TurnDirection(0x9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_624)
    Jump("loc_636")

    label("loc_62F")

    TurnDirection(0x101, 0x102, 400)

    label("loc_636")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #11
        0x101,
        "#1004F#4PHuh...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A0")

    ChrTalk(    #12
        0x106,
        "#052F#6PCan you get the factory working?\x02",
    )

    CloseMessageWindow()
    Jump("loc_71B")

    label("loc_6A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DF")

    ChrTalk(    #13
        0x103,
        "#023F#6PCan you get the factory working?\x02",
    )

    CloseMessageWindow()
    Jump("loc_71B")

    label("loc_6DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71B")

    ChrTalk(    #14
        0x108,
        "#073F#6PCan you get the factory working?\x02",
    )

    CloseMessageWindow()

    label("loc_71B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_767")

    ChrTalk(    #15
        0x107,
        (
            "#060F#6PY-Yeah, probably.\x02\x03",

            "If we use the generator...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9")

    label("loc_767")


    ChrTalk(    #16
        0x102,
        (
            "#1040F#6PYes, most likely...\x02\x03",

            "If we use the generator, we can briefly\x01",
            "restore the equipment here, I suspect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D9")


    ChrTalk(    #17
        0x101,
        "#1018F#4PAh, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        "Whoa, whoa, you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        "The heck are you talking about?\x02",
    )

    CloseMessageWindow()

    def lambda_83A():
        TurnDirection(0x0, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_83A)
    Sleep(120)

    def lambda_84D():
        TurnDirection(0x1, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_84D)

    def lambda_85B():
        TurnDirection(0x2, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_85B)
    Sleep(120)

    def lambda_86E():
        TurnDirection(0x3, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_86E)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_88A")


    ChrTalk(    #20
        0x102,
        "#1040F#6PLet me explain.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Joshua explained that by using the Zero Field Generator the\x01",
            "factory's functionality could be temporarily restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #22
        0x9,
        "Huh, that's incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "The machines are right there,\x01",
            "so wanna give it a try?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1006F#6PYeah, if you don't mind.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F8")

    ChrTalk(    #25
        0x107,
        "#560F#6POkay! Just a sec...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A48")

    label("loc_9F8")


    ChrTalk(    #26
        0x102,
        (
            "#1040F#6PWell, then, if you'll let me borrow the\x01",
            "equipment for a moment...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A48")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_8C(0x9, 315, 0)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "\x07\x05On activation, the Zero Field Generator restored power\x01",
            "to the factory's tools.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #28
        0x9,
        (
            "Ohh, things are looking up.\x01",
            "The orbal energy's returned to the machinery.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BA2")
    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #29
        0x9,
        (
            "I'm sure it's just a temporary patch, so if you\x01",
            "wanna tune your equipment, now's your chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D30")

    label("loc_BA2")


    ChrTalk(    #30
        0x101,
        "#1000F#6PAwesome. It worked.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C32")

    ChrTalk(    #31
        0x107,
        (
            "#063F#6PYeah, but it'll only last for a little bit.\x02\x03",

            "#561FIt'll go back to normal soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C97")

    label("loc_C32")


    ChrTalk(    #32
        0x102,
        (
            "#1040F#6PYeah, it went well...\x02\x03",

            "But it's not really fixed, so after\x01",
            "some time it'll stop again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C97")

    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #33
        0x9,
        (
            "I see... So it is ultimately just a temporary\x01",
            "patch, in other words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "Well, one way or another, if you\x01",
            "wanna tune your, gear do it now.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    label("loc_D30")

    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x77)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #35
        0x9,
        "Still, that's one incredible device.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        "If you don't mind, could you leave one here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1015F#6PI wish we could, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#1040F#6PI'm sorry.\x01",
            "They're needed for an important mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "*sigh* I guess that was too much to hope for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        "Well, bring that when you come by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "If you do, you'll be able to use\x01",
            "the factory like normal.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20E3)
    EventEnd(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_F79")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_F17")

    ChrTalk(    #42
        0x9,
        (
            "Seems like bracers are good\x01",
            "at photography too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "Some kinda special training?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F76")

    label("loc_F17")


    ChrTalk(    #44
        0x9,
        "Gonna go take pictures somewhere?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "Seems like photography is all the\x01",
            "rage these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F76")

    Jump("loc_1814")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_10C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1066")

    ChrTalk(    #46
        0x9,
        "The orbments in town still aren't working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "As long as the big bridge is frozen,\x01",
            "that's gonna remain true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "Still, to wipe out all orbal energy-using\x01",
            "devices...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        "Really, what's going on in Liberl...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_10C0")

    label("loc_1066")


    ChrTalk(    #50
        0x9,
        "The orbments in town still aren't working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        "Really, what's going on in Liberl...\x02",
    )

    CloseMessageWindow()

    label("loc_10C0")

    Jump("loc_1814")

    label("loc_10C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1196")

    ChrTalk(    #52
        0x9,
        (
            "If I had that that equipment, I could\x01",
            "reopen my business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "Well, whatever.\x01",
            "No point asking for the impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "Guess I'll just have to wait until\x01",
            "this thing blows over, whatever it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1814")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_138F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12A2")

    ChrTalk(    #55
        0x9,
        (
            "Norman's not wrong when he says that\x01",
            "the future is in the tourism industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "But, Ruan is also a strategic hub connected\x01",
            "directly to the capital by water. We can't let\x01",
            "our harbor facilities fall into disuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "Mmmm, who should I vote for?\x02",
    )

    CloseMessageWindow()
    Jump("loc_138C")

    label("loc_12A2")

    OP_A2(0x1)

    ChrTalk(    #58
        0x9,
        (
            "Norman's not wrong when he says that\x01",
            "the future is in the tourism industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "But, Ruan is also a strategic hub connected\x01",
            "directly to the capital by water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "I feel like it's important to maintain our\x01",
            "harbor facilities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138C")

    Jump("loc_1814")

    label("loc_138F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_152B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_143D")

    ChrTalk(    #61
        0x9,
        (
            "With all that scandal business involving Mayor\x01",
            "Dalmore, the city's image has gotten worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "On top of that, we almost had a riot?\x01",
            "Aidios, spare us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1528")

    label("loc_143D")

    OP_A2(0x1)

    ChrTalk(    #63
        0x9,
        (
            "Really, it's a serious problem having\x01",
            "a riot almost happen like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "The city's image has already taken hit\x01",
            "from the Dalmore scandal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "If anything else happens on top of that,\x01",
            "we're gonna get a real nasty reputation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1528")

    Jump("loc_1814")

    label("loc_152B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_156A")

    ChrTalk(    #66
        0x9,
        (
            "Hey, how's it going?\x01",
            "You seem kinda in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1814")

    label("loc_156A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1634")

    ChrTalk(    #67
        0x9,
        (
            "Lately I've been asked to develop some\x01",
            "photo-quartz by some touring visitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "With orbal cameras becoming more common, the\x01",
            "number of people taking photos has gone way up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B8")

    label("loc_1634")

    OP_A2(0x1)

    ChrTalk(    #69
        0x9,
        (
            "Actually, I haven't decided which\x01",
            "candidate to vote for yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "I do a lot of business with both\x01",
            "tourists and the harbor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B8")

    Jump("loc_1814")

    label("loc_16BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_177F")

    ChrTalk(    #71
        0x9,
        (
            "The Epstein Foundation is really pushing\x01",
            "the new model orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "Even independently owned and operated factories\x01",
            "like mine are participating in their outreach\x01",
            "programs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1814")

    label("loc_177F")

    OP_A2(0x1)

    ChrTalk(    #73
        0x9,
        "Hey, so how do those new orbments feel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "You should focus on upgrading your slots\x01",
            "to get a handle on their functionality levels\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1814")

    TalkEnd(0x9)
    Return()

    # Function_1_AF end

    def Function_2_1818(): pass

    label("Function_2_1818")

    Call(1, 3)
    Return()

    # Function_2_1818 end

    def Function_3_181D(): pass

    label("Function_3_181D")

    TalkBegin(0xA)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184E")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1843")
    OP_A9(0x76)
    Jump("loc_1845")

    label("loc_1843")

    OP_A9(0x65)

    label("loc_1845")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_184E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185F")
    TalkEnd(0xA)
    Return()

    label("loc_185F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_32E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x408, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xCB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A5A")

    ChrTalk(    #75
        0xA,
        "Oh, my, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "I heard you guys solved the\x01",
            "case at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1006FYeah, somehow.\x02\x03",

            "We couldn't have done it without Carna\x01",
            "and the rest helping us out, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #78
        0xA,
        (
            "Heehee! I'm glad to hear my collection\x01",
            "helped out a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1011FYour collection...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#1040FThat's right, the gun Carna was using...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #81
        0xA,
        (
            "Yes, handling gunpowder firearms\x01",
            "is quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "Though, with Carna's skills, I figured\x01",
            "she wouldn't have any problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x20B3)
    OP_A2(0x2040)
    Jump("loc_32E3")

    label("loc_1A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x408, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D79")

    ChrTalk(    #83
        0xA,
        "Oh, my, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "I heard you guys solved the\x01",
            "case at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1006FYeah, somehow.\x02\x03",

            "We couldn't have done it without Carna\x01",
            "and the rest helping us out, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #86
        0xA,
        (
            "Heehee! I'm glad to hear my collection\x01",
            "helped out a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1011FYour collection...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        "#1040FThat's right, the gun Carna was using...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #89
        0xA,
        (
            "Yes, handling gunpowder firearms\x01",
            "is quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "Though, with Carna's skills, I figured\x01",
            "she wouldn't have any problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "But, what surprised me most was the\x01",
            "girl who was shooting alongside her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1000FAh, you mean Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        "Yes, darling little Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "But, it seems she's not with\x01",
            "you right now, is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#1044FIs there something you'd like\x01",
            "to talk to her about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        "Oh, just a little thing.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x20B3)
    Jump("loc_1F24")

    label("loc_1D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E07")

    ChrTalk(    #97
        0xA,
        "My little sister Nikita attends the royal academy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        (
            "Allow me to offer my deepest thanks\x01",
            "for safely resolving things there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F24")

    label("loc_1E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED5")

    ChrTalk(    #99
        0xA,
        (
            "Apparently you safely resolved\x01",
            "things at the royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        "My little sister Nikita attends school there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "Allow me to offer my deepest thanks\x01",
            "for safely resolving things there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1F24")

    label("loc_1ED5")


    ChrTalk(    #102
        0xA,
        (
            "Thank you for resolving things. I'm grateful\x01",
            "from the depths of my heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F24")

    Jump("loc_31DB")

    label("loc_1F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227C")

    ChrTalk(    #103
        0xA,
        "Oh, my, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "I heard you guys solved the\x01",
            "case at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1006FYeah, somehow.\x02\x03",

            "We couldn't have done it without Carna\x01",
            "and the rest helping us out, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #106
        0xA,
        (
            "Heehee! I'm glad to hear my collection\x01",
            "helped out a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1011FYour collection...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        "#1040FThat's right, the gun Carna was using...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #109
        0xA,
        (
            "Yes, handling gunpowder firearms\x01",
            "is quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "Though, with Carna's skills, I figured\x01",
            "she wouldn't have any problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "But, what surprised me most was the\x01",
            "girl who was shooting alongside her.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x107, 400)

    ChrTalk(    #112
        0xA,
        "Is that... Are you Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x107,
        "#064FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1015FYeah, that's right, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        "#1044FWhat do you need with Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        (
            "Well, actually I have a bit of business with her.\x01",
            "How to put this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        (
            "If you don't mind, could I have\x01",
            "a little bit of your time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238F")

    label("loc_227C")


    ChrTalk(    #118
        0xA,
        "Oh, my, bracers.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x107, 400)

    ChrTalk(    #119
        0xA,
        "Is that... Are you Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x107,
        "#064FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#1040FOh, right...\x02\x03",

            "You said you had something to say to Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xA,
        "Yes, well, how to put this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        (
            "Anyway, if you don't mind, could I have\x01",
            "a little bit of your time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238F")

    FadeToDark(1500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    Sleep(500)
    OP_8C(0xA, 180, 0)
    OP_6D(1130, 400, 3310, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 2050, 0, 1930, 0)
    SetChrPos(0x102, 620, 0, 1630, 0)
    SetChrPos(0xF8, 1220, 0, 2670, 0)
    SetChrPos(0xF9, 1320, 0, 710, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2458")
    SetChrPos(0xF9, 1220, 0, 2670, 0)
    SetChrPos(0xF8, 1320, 0, 710, 0)

    label("loc_2458")

    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #124
        0x107,
        (
            "#560FUm, um...\x01",
            "What did you want to talk about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        "Yes, about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xA,
        (
            "First, would you mind showing\x01",
            "me your gunpowder cannon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x107,
        "#064FO-Okay...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #128
        "\x07\x05Tita took out her favored gatling cannon.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xA)
    Sleep(500)

    ChrTalk(    #129
        0xA,
        "...I thought so, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        "Ahh! I knew it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x107,
        "#064FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xA,
        "Tita, do you know what model this is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        (
            "#560FAh, yes, it's what's called the CZ Series.\x02\x03",

            "It's one of the first models in that line.\x01",
            "Grandpa said it's really rare. There's\x01",
            "only a few in the world or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "Yes, that's right.\x01",
            "Do you know anything else about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x107,
        (
            "#561FUm, um... I don't know that much\x01",
            "about weapons myself, but...\x02\x03",

            "#060FApparently there was a problem with the\x01",
            "initial model's basic structure, so it wasn't\x01",
            "able to live up to design specifications.\x02\x03",

            "As a result, while the firepower was upgradable,\x01",
            "the attack range wasn't adjustable.\x02\x03",

            "The next generation models were improved\x01",
            "though, apparently.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287F")

    ChrTalk(    #136
        0x101,
        "#1016F(I-I'd say she knows plenty...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x106,
        "#551F(Yeah, seriously.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_28C8")

    label("loc_287F")


    ChrTalk(    #138
        0x101,
        "#1016F(I-I'd say she knows plenty...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x102,
        "#1054F(Haha, well said.)\x02",
    )

    CloseMessageWindow()

    label("loc_28C8")


    ChrTalk(    #140
        0xA,
        (
            "I see. Well, if you know that much,\x01",
            "then this is simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xA,
        "So, Tita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xA,
        (
            "Have you heard about the F Parts\x01",
            "produced by the Reinford Company?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x107,
        (
            "#560FYeah! They're the 'Final' parts to compliment\x01",
            "the CZ Series' weak points, right?\x02\x03",

            "But I heard they only work with relatively\x01",
            "new models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xA,
        (
            "Actually, there are F Parts for that\x01",
            "initial model.\x02\x01",

            "Would you believe that if I said it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #145
        0x107,
        "#064FWh... Is that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xA,
        "Yes, it is indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xA,
        (
            "There's little demand for them so there's\x01",
            "not many around, but they certainly exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        "Now, here's the real point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x107,
        "#062FWh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xA,
        (
            "As it happens, by total coincidence a set\x01",
            "of those parts is in this very store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x107,
        "#560FR-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xA,
        "Really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xA,
        "I'd like you to have these F Parts.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #154
        0x107,
        "#064FB-But that's... Are you sure?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        "Of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        (
            "I owe you all for saving my little sister\x01",
            "at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "Besides, it'd be a real waste to\x01",
            "just let them rust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x107,
        (
            "#561FB-But it doesn't feel right just\x01",
            "taking something for free...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DA1")
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #159
        0x106,
        (
            "#053FWell, hey.\x02\x03",

            "#051FWhy don't you just accept them?\x02\x03",

            "If it still bothers you, you can\x01",
            "pay her back some other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x107,
        "#064FAgate...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E8B")

    label("loc_2DA1")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #161
        0x101,
        (
            "#1011FHey, Tita.\x02\x03",

            "The shop owner is saying she wants you to\x01",
            "have them, so why don't you just accept them?\x02\x03",

            "If it still bothers you, you can find\x01",
            "some other way to pay her back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x107,
        "#064FEstelle...\x02",
    )

    CloseMessageWindow()

    label("loc_2E8B")

    OP_62(0x107, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #163
        0x107,
        (
            "#563F...\x02\x03",

            "#067FUmm... Are you sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        "Of course! That's why I mentioned it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        "Do you know how to install the parts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x107,
        (
            "#061FYeah, probably.\x02\x03",

            "#560FUm, if you don't mind, could\x01",
            "I borrow some space?\x02\x03",

            "I'll put them on right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        "That's perfectly fine.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xB7, 0x0, 0x64)
    Sleep(2500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #168
        "#5CTita learned a new S-Craft, #2CCannon Impulse F#5C.\x02",
    )

    CloseMessageWindow()
    OP_22(0x21E, 0x0, 0x64)
    SetMessageWindowPos(-1, 38, -1, -1)

    AnonymousTalk(    #169
        (
            "\x07\x05Would you like to register Cannon\x01",
            "Impulse F as her S-Break?\x18\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3070")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_311B")

    Menu(
        1,
        -1,
        250,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30AB"),
        (SWITCH_DEFAULT, "loc_30E5"),
    )


    label("loc_30AB")

    OP_35(0x6, 0x107)
    OP_BB(0x6, 0x6, 0x107)
    OP_C0(0x18, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3118")

    label("loc_30E5")

    OP_35(0x6, 0x107)
    OP_C0(0x18, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3118")

    label("loc_3118")

    Jump("loc_3070")

    label("loc_311B")

    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #170
        0xA,
        "Well done! Perfectly upgraded.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        "This should make it QUITE a bit different now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x107,
        (
            "#560FYes, I'll be sure to try it right away.\x02\x03",

            "#061FThank you so very much!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2040)
    EventEnd(0x0)

    label("loc_31DB")

    Jump("loc_32E3")

    label("loc_31DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3294")

    ChrTalk(    #173
        0xA,
        (
            "Not at all. Thank YOU for safely managing\x01",
            "things at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xA,
        "My little sister Nikita attends school there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        "I'm thankful from the depths of my heart.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_32E3")

    label("loc_3294")


    ChrTalk(    #176
        0xA,
        (
            "Thank you for resolving things. I'm grateful\x01",
            "from the depths of my heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E3")

    Jump("loc_3AB8")

    label("loc_32E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_34A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F3")

    ChrTalk(    #177
        0xA,
        (
            "None of the weapons using\x01",
            "orbal energy are working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "Of course, normal weapons still work, so as long\x01",
            "as you're martially trained, there shouldn't be\x01",
            "a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        (
            "It seems when you come down\x01",
            "to it, your basics really are what's tested.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_349D")

    label("loc_33F3")


    ChrTalk(    #180
        0xA,
        (
            "None of the weapons using\x01",
            "orbal energy are working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "Of course, normal weapons still work, so as long\x01",
            "as you're martially trained, there shouldn't be\x01",
            "a problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_349D")

    Jump("loc_3AB8")

    label("loc_34A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_35ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_353C")

    ChrTalk(    #182
        0xA,
        (
            "I'm going to go vote, but I'm not terribly\x01",
            "interested in the election to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xA,
        "Well, I figure I'll vote based on character.\x02",
    )

    CloseMessageWindow()
    Jump("loc_35EA")

    label("loc_353C")

    OP_A2(0x0)

    ChrTalk(    #184
        0xA,
        (
            "Technically, I'm going to go vote, but\x01",
            "frankly I don't really care much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xA,
        (
            "I know the people whose jobs will be affected\x01",
            "are taking things very seriously, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EA")

    Jump("loc_3AB8")

    label("loc_35ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_36AD")

    ChrTalk(    #186
        0xA,
        (
            "Ruan's a city of sailors, so there are a lot of\x01",
            "people with, ah, strong personalities here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xA,
        (
            "Without that much backbone, you can hardly\x01",
            "endure a long ocean trip, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB8")

    label("loc_36AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_3722")

    ChrTalk(    #188
        0xA,
        (
            "A customer just ran out of here like\x01",
            "a War Bat out of Gehenna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        "I wonder if something happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AB8")

    label("loc_3722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_37B0")

    ChrTalk(    #190
        0xA,
        (
            "Bracer work involves running all over.\x01",
            "Must be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xA,
        (
            "I hope you can at least relax a bit\x01",
            "while you're in Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3A")

    label("loc_37B0")

    OP_A2(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3905")

    ChrTalk(    #192
        0xA,
        "Welcome, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xA,
        (
            "Your work involves running all over.\x01",
            "Must be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        (
            "After all, if you don't have any time to\x01",
            "relax, it's hard to meet people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xA,
        (
            "I've even heard men are leaving\x01",
            "starting a family till QUITE late...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(    #196
        0x101,
        "#1028FHuuuuuuh, I see.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #197
        0x106,
        (
            "#552F...\x02\x03",

            "Hey, why are you looking at me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3A")

    label("loc_3905")


    ChrTalk(    #198
        0xA,
        "Welcome, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xA,
        (
            "Your work involves running all over.\x01",
            "Must be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        (
            "After all, if you don't have any time to\x01",
            "relax, it's hard to meet people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        (
            "It seems there are a lot of women whose\x01",
            "chances have just flown right by them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x103,
        "#023F(...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        "Oh, come, now! It was just a little joke.\x02",
    )

    CloseMessageWindow()

    label("loc_3A3A")

    Jump("loc_3AB8")

    label("loc_3A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3AB8")

    ChrTalk(    #204
        0xA,
        "Oh, welcome. Two bracers together, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xA,
        (
            "Carna's not here right now,\x01",
            "so I hope you guys will do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB8")

    TalkEnd(0xA)
    Return()

    # Function_3_181D end

    def Function_4_3ABC(): pass

    label("Function_4_3ABC")

    Call(1, 5)
    Return()

    # Function_4_3ABC end

    def Function_5_3AC1(): pass

    label("Function_5_3AC1")

    TalkBegin(0xB)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF2")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE7")
    OP_A9(0x6D)
    Jump("loc_3AE9")

    label("loc_3AE7")

    OP_A9(0x66)

    label("loc_3AE9")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_3AF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B03")
    TalkEnd(0xB)
    Return()

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3D09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C50")

    ChrTalk(    #206
        0xB,
        (
            "We've got some lamp oil and foodstuffs\x01",
            "in stock, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xB,
        (
            "Obviously if this keeps goin' on,\x01",
            "then we'll run out real fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xB,
        (
            "We're continuing to sell these new model\x01",
            "glasses from the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xB,
        (
            "They're quite the convenient tool in places\x01",
            "where the lights are out, so you should buy\x01",
            "several.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3D06")

    label("loc_3C50")


    ChrTalk(    #210
        0xB,
        (
            "We're continuing to sell these new model\x01",
            "glasses from the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xB,
        (
            "They're quite the convenient tool in places\x01",
            "where the lights are out, so you should buy\x01",
            "several.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D06")

    Jump("loc_4B2E")

    label("loc_3D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3F7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EA6")

    ChrTalk(    #212
        0xB,
        "Hmm, with orbments stopped it's quite terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xB,
        (
            "Even I've never seen a phenomenon\x01",
            "like this before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xB,
        (
            "Putting that aside, speaking of\x01",
            "things I've never seen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xB,
        (
            "We're continuing to sell these new model\x01",
            "glasses from the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xB,
        (
            "They're quite the convenient tool in places\x01",
            "where the lights are out, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xB,
        "If you don't have any, you should buy several.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3F77")

    label("loc_3EA6")


    ChrTalk(    #218
        0xB,
        (
            "We're selling new model glasses provided\x01",
            "by the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xB,
        (
            "They're quite the convenient tool in places\x01",
            "where the lights are out, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xB,
        "If you don't have any, you should buy several.\x02",
    )

    CloseMessageWindow()

    label("loc_3F77")

    Jump("loc_4B2E")

    label("loc_3F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_412D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4035")

    ChrTalk(    #221
        0xB,
        (
            "It's true that the city can't survive\x01",
            "on just the income from the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xB,
        (
            "I understand putting the emphasis on tourism,\x01",
            "but at the same time it's terribly sad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_412A")

    label("loc_4035")

    OP_A2(0x4)

    ChrTalk(    #223
        0xB,
        (
            "As a former sailor I'd like to somehow\x01",
            "maintain the harbor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xB,
        (
            "It's true that the city can't survive\x01",
            "on just the income from the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xB,
        (
            "I understand putting the emphasis on tourism,\x01",
            "but at the same time it's terribly sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_412A")

    Jump("loc_4B2E")

    label("loc_412D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_442D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4172")

    ChrTalk(    #226
        0xB,
        (
            "Oh, want to hear more of my\x01",
            "adventure stories?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442A")

    label("loc_4172")

    OP_A2(0x4)

    ChrTalk(    #227
        0xB,
        (
            "It seems there was a bit of a fuss,\x01",
            "but, hmph, that was nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xB,
        (
            "The 'elections' I took part in when I was\x01",
            "younger were far more extreme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xB,
        (
            "Those elections were far simpler, see.\x01",
            "Everyone fought, and the guy standing\x01",
            "at the end was the representative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xB,
        (
            "Of course, I got involved. But, well, how did it\x01",
            "turn out? I am, after all, Captain O'Neil, and I\x01",
            "learned my lessons in the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xB,
        "When I realized it, I was the only one standing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xB,
        (
            "They were just about to drag me off in a\x01",
            "palanquin as their new chieftain, but I\x01",
            "barely managed to escape to my ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xB,
        (
            "I'm sure if I'd gone on to become their chieftain,\x01",
            "that would've been quite the life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xB,
        "Wahaha!\x02",
    )

    CloseMessageWindow()

    label("loc_442A")

    Jump("loc_4B2E")

    label("loc_442D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_44B9")

    ChrTalk(    #235
        0xB,
        (
            "Hmm, seems like there's a\x01",
            "fuss over at the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xB,
        (
            "Guess those young punks are off making\x01",
            "noise like idiots again, hmm?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2E")

    label("loc_44B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_482F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_45C2")

    ChrTalk(    #237
        0xB,
        (
            "Speaking of countries without elections,\x01",
            "the Erebonian Empire comes to mind,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xB,
        (
            "You could say Liberl is a very clever kingdom,\x01",
            "what with dividing up its roles between the royal\x01",
            "family and a locally-elected government and all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_482C")

    label("loc_45C2")

    OP_A2(0x4)

    ChrTalk(    #239
        0xB,
        (
            "The best representative of countries without\x01",
            "elections would probably be the Erebonian\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xB,
        (
            "There are elections in border regions without\x01",
            "a lord, but the pillar of the Empire is a\x01",
            "strict social status society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xB,
        (
            "However, when that kind of system works,\x01",
            "it really works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xB,
        (
            "If there are many competent people of high\x01",
            "status, such a system can actually work very\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xB,
        (
            "Of course, when it's the other way around,\x01",
            "well, that's painful to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xB,
        (
            "Well, thinking of that, Liberl, where we use both\x01",
            "a royal system and an electoral system, could be\x01",
            "said to have set up a very wise social system.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_482C")

    Jump("loc_4B2E")

    label("loc_482F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_4B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_48EA")

    ChrTalk(    #245
        0xB,
        (
            "The way elections are done is different\x01",
            "based on each country's values.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xB,
        (
            "Apparently there are also countries that,\x01",
            "conversely, pick terrible people to kick out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2E")

    label("loc_48EA")

    OP_A2(0x4)

    ChrTalk(    #247
        0xB,
        (
            "The city's worked up over the election,\x01",
            "but even the word 'election' calls up a\x01",
            "lot of different images.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xB,
        (
            "For example, Liberl's mayoral election system\x01",
            "is based heavily off of the Republic's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xB,
        (
            "The people of that country come from all over,\x01",
            "so they needed a fair and equal way to decide\x01",
            "things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xB,
        (
            "Incidentally, in the world there are countries\x01",
            "that, unlike us, decide on who they don't\x01",
            "like instead!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xB,
        (
            "Apparently, there the unpopular person with\x01",
            "the most votes is kicked off of the council.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xB,
        (
            "That might be a reasonable system\x01",
            "in its own way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xB,
        "Wahaha!\x02",
    )

    CloseMessageWindow()

    label("loc_4B2E")

    TalkEnd(0xB)
    Return()

    # Function_5_3AC1 end

    def Function_6_4B32(): pass

    label("Function_6_4B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4B43")
    OP_2A(0xB9, 0xBA, 0xFFFF)
    Jump("loc_4BCA")

    label("loc_4B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4B60")
    OP_2A(0x65, 0x66, 0xA1, 0xA3, 0x67, 0x68, 0xA2, 0xA4, 0xFFFF)
    Jump("loc_4BCA")

    label("loc_4B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_4B7B")
    OP_2A(0x65, 0x66, 0xA1, 0xA3, 0x67, 0xA2, 0xA4, 0xFFFF)
    Jump("loc_4BCA")

    label("loc_4B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_4B90")
    OP_2A(0x65, 0x66, 0xA1, 0xA3, 0xFFFF)
    Jump("loc_4BCA")

    label("loc_4B90")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #254
        "\x07\x05No jobs are available.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4BCA")

    TalkEnd(0xFF)
    Return()

    # Function_6_4B32 end

    def Function_7_4BCE(): pass

    label("Function_7_4BCE")

    EventBegin(0x0)
    OP_6D(-32970, 0, 5800, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x9, -33640, 0, 6750, 0)
    SetChrPos(0x15, -29550, 0, 3100, 0)
    SetChrPos(0x101, -30640, 0, 3100, 0)
    SetChrPos(0xF7, -29970, 0, 1750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4C74")
    SetChrPos(0x127, -31340, 0, 1210, 0)

    label("loc_4C74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4C92")
    SetChrPos(0x104, -31640, 0, 2480, 0)

    label("loc_4C92")

    OP_4A(0x9, 255)

    def lambda_4C9C():

        label("loc_4C9C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4C9C")

    QueueWorkItem2(0x0, 1, lambda_4C9C)

    def lambda_4CAD():

        label("loc_4CAD")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4CAD")

    QueueWorkItem2(0x1, 1, lambda_4CAD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4CE7")

    def lambda_4CCB():

        label("loc_4CCB")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4CCB")

    QueueWorkItem2(0x2, 1, lambda_4CCB)

    def lambda_4CDC():

        label("loc_4CDC")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4CDC")

    QueueWorkItem2(0x3, 1, lambda_4CDC)

    label("loc_4CE7")


    def lambda_4CED():

        label("loc_4CED")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4CED")

    QueueWorkItem2(0x15, 1, lambda_4CED)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_4D0D():
        OP_6D(-29850, 0, 3090, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4D0D)
    OP_8E(0x9, 0xFFFF8882, 0x0, 0x17A2, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF8AD0, 0x0, 0x132E, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    Sleep(400)
    WaitChrThread(0x0, 0x2)
    OP_44(0x15, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D79")
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    label("loc_4D79")


    ChrTalk(    #255
        0x9,
        "Phew! All done here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x15,
        "...Yeah, thanks.\x02",
    )

    CloseMessageWindow()

    def lambda_4DAF():

        label("loc_4DAF")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_4DAF")

    QueueWorkItem2(0x0, 1, lambda_4DAF)

    def lambda_4DC0():

        label("loc_4DC0")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_4DC0")

    QueueWorkItem2(0x1, 1, lambda_4DC0)

    def lambda_4DD1():

        label("loc_4DD1")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_4DD1")

    QueueWorkItem2(0x2, 1, lambda_4DD1)

    def lambda_4DE2():

        label("loc_4DE2")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_4DE2")

    QueueWorkItem2(0x3, 1, lambda_4DE2)

    ChrTalk(    #257
        0x15,
        "Now, then, how'd the photo turn out...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x15)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_5296")

    ChrTalk(    #258
        0x15,
        "#4P...Huh, well this is a shock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x15,
        (
            "#4PIt's good enough to look like it came from\x01",
            "a pro... Actually, it's better than most\x01",
            "professional work. Wow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        "#1004FI-Is it that well done?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x15,
        "#4PHere, take a look.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0x0, 0x0, 0x258, 0x12C, 0x14, 0x5A, 0x280, 0x12C, 0x0, 0x0, 0x258, 0x12C, 0xFFFFFF, 0x0, "C_VIS198._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #262
        "#1011FWhoa, that is really nice.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Santos")

    AnonymousTalk(    #263
        (
            "Yeah, you really matched the focus on\x01",
            "panorama mode, which is really difficult...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Santos")

    AnonymousTalk(    #264
        (
            "Maaan, the way it captures the light\x01",
            "is just perfect.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Santos")

    AnonymousTalk(    #265
        (
            "You can tell just by looking at this\x01",
            "that this 'device' has a long history.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Santos")

    AnonymousTalk(    #266
        (
            "Of course, a photo this good is plenty\x01",
            "for research purposes, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Santos")

    AnonymousTalk(    #267
        (
            "It almost feels like a waste\x01",
            "to use it for that.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #268
        (
            "#1004FO-Oh, really...?\x02\x03",

            "#1016FPretty complex, huh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Dorothy")

    AnonymousTalk(    #269
        "#151FHeehee! It's incredible.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    FadeToBright(300, 0)
    OP_0D()
    OP_C6(0x0, 0x6, 0, 0, 0)
    Sleep(1500)
    OP_C7(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_524E")

    ChrTalk(    #270
        0x106,
        "#051FWell, then, our job's done.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5283")

    label("loc_524E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5283")

    ChrTalk(    #271
        0x103,
        "#020FWell, then, this completes the job.\x02",
    )

    CloseMessageWindow()

    label("loc_5283")

    OP_2B(0x66, 0x2)
    OP_2C(0x66, 0x3E8)
    OP_28(0x66, 0x1, 0x10)
    Jump("loc_5782")

    label("loc_5296")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5302")

    ChrTalk(    #272
        0x15,
        "#4P...Hmm, it's okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x15,
        "#4PIt can be used as material, more or less.\x02",
    )

    CloseMessageWindow()
    OP_28(0x66, 0x1, 0x80)
    Jump("loc_53BB")

    label("loc_5302")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5352")

    ChrTalk(    #274
        0x15,
        "#4P... Yeah, well done. No problems at all.\x02",
    )

    CloseMessageWindow()
    OP_2B(0x66, 0x1)
    OP_2C(0x66, 0x3E8)
    OP_28(0x66, 0x1, 0x20)
    Jump("loc_53BB")

    label("loc_5352")


    ChrTalk(    #275
        0x15,
        "#4P...Hmm, it's okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x15,
        (
            "#4PThis one's plenty good enough to use as\x01",
            "research material.\x02",
        )
    )

    CloseMessageWindow()
    OP_2C(0x66, 0x1F4)
    OP_28(0x66, 0x1, 0x40)

    label("loc_53BB")


    ChrTalk(    #277
        0x15,
        "#4PWould you like to take a look?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        "#1018FYeah, absolutely. ♪\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    FadeToDark(300, 0, 100)
    Call(1, 8)
    OP_C5(0x1, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x0, 0x0, 0x190, 0x12C, 0xFFFFFF, 0x0, "C_VIS199._CH")
    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #279
        (
            "#1001FAhhh, thank Aidios.\x02\x03",

            "It's a lot nicer than I thought it would be.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5511")
    SetMessageWindowPos(250, 50, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #280
        "#031FThe focus is clean. Most impressive.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5511")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5554")
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Dorothy")

    AnonymousTalk(    #281
        "#150FYeah, yeah, well shot! ♪\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5554")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_569B")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Santos")

    AnonymousTalk(    #282
        "The angle's a pity, though...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Santos")

    AnonymousTalk(    #283
        (
            "This is a research material photo, so if possible,\x01",
            "I would have preferred a shot from straight on.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #284
        (
            "#1008FAw, of course...\x02\x03",

            "I-I got kind of worked up and excited,\x01",
            "and tried to take it at a different angle.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_56D4")

    label("loc_569B")

    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Santos")

    AnonymousTalk(    #285
        "Yes, this is enough to satisfy me.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_56D4")

    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    FadeToBright(300, 0)
    OP_0D()
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    Sleep(1500)
    OP_C7(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5754")

    ChrTalk(    #286
        0x106,
        "#050FThat finishes the job, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5782")

    label("loc_5754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5782")

    ChrTalk(    #287
        0x103,
        "#020FThat finishes the job, then.\x02",
    )

    CloseMessageWindow()

    label("loc_5782")

    TurnDirection(0x15, 0xF7, 400)

    ChrTalk(    #288
        0x15,
        "#4PRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x15,
        "#4PThank you all so much for all you've done!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x15,
        (
            "#4PClimbing all the way up that tower must\x01",
            "have been exhausting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1015FWell, it was kind of rough, but...\x02\x03",

            "#1006FIt's all part of the job.\x01",
            "Don't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x15,
        (
            "#4PAhaha, thanks. Hearing you say\x01",
            "that makes me feel better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x15,
        "#4POh, right. Here. It's not much, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x15,
        "#4PPlease, take this.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #295
        "\x07\x00Received #341i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x155, 1)
    Sleep(500)

    ChrTalk(    #296
        0x15,
        (
            "#4PIt's a piece of equipment I picked up with\x01",
            "research funds for this expedition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x15,
        (
            "#4PI'm sure it'll be useful if you have to venture\x01",
            "into dangerous places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x101,
        (
            "#1001FAhaha, thanks. ♪\x02\x03",

            "Since you're offering, we'll accept.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5A62")

    ChrTalk(    #299
        0x106,
        "#051FThanks. 'Preciate it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A98")

    label("loc_5A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5A98")

    ChrTalk(    #300
        0x103,
        "#020FThank you. I'm sure it'll be useful.\x02",
    )

    CloseMessageWindow()

    label("loc_5A98")


    ChrTalk(    #301
        0x15,
        "#4PNo, no. It's not all that much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x15,
        "#4PAnyway, if you'll pardon me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x15,
        "#4PThanks again for your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        (
            "#1000FGood luck with your investigation!\x02\x03",

            "I'm kinda curious too, honestly.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #305
        0x15,
        (
            "#4PAhaha... It's going to be quite\x01",
            "the piece of homework, certainly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x15,
        (
            "#4PWell, I will do my best to live\x01",
            "up to your expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x15,
        "#4P...Well, see you guys later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        "#1006FYeah, later!\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8C(0x15, 180, 400)

    def lambda_5C51():
        OP_91(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_5C51)
    OP_8E(0x15, 0xFFFF8C92, 0x0, 0xFFFFFC18, 0x7D0, 0x1)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_5C8B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5C8B)
    OP_8E(0x15, 0xFFFF8C92, 0xFFFFFDFA, 0xFFFFF574, 0x7D0, 0x0)
    WaitChrThread(0x15, 0x2)
    SetChrFlags(0x15, 0x80)
    Sleep(1500)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #309
        "Quest #CR#[Sapphirl Tower Photo] #CW#completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x66, 0x1, 0x100)
    OP_28(0x66, 0x4, 0x10)
    OP_A2(0x5)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_7_4BCE end

    def Function_8_5D49(): pass

    label("Function_8_5D49")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D84")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x78, 0x0, 0x208, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5D84")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC0")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x64, 0x0, 0x1F4, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5DC0")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DFB")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x8C, 0x0, 0x21C, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5DFB")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E37")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x50, 0x0, 0x1E0, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5E37")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E72")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xA0, 0x0, 0x230, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5E72")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EAE")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x3C, 0x0, 0x1CC, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5EAE")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EE9")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xB4, 0x0, 0x244, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5EE9")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F25")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x14, 0x0, 0x1A4, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5F25")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F60")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xDC, 0x0, 0x26C, 0x12C, 0xFFFFFF, 0x0, "C_VIS195._CH")
    Jump("loc_60C2")

    label("loc_5F60")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F9C")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x3C, 0x0, 0x1CC, 0x12C, 0xFFFFFF, 0x0, "C_VIS196._CH")
    Jump("loc_60C2")

    label("loc_5F9C")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FD8")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x78, 0x0, 0x208, 0x12C, 0xFFFFFF, 0x0, "C_VIS196._CH")
    Jump("loc_60C2")

    label("loc_5FD8")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6014")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xDC, 0x0, 0x26C, 0x12C, 0xFFFFFF, 0x0, "C_VIS196._CH")
    Jump("loc_60C2")

    label("loc_6014")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_604F")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0xB4, 0x0, 0x244, 0x12C, 0xFFFFFF, 0x0, "C_VIS197._CH")
    Jump("loc_60C2")

    label("loc_604F")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_608A")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x3C, 0x0, 0x1CC, 0x12C, 0xFFFFFF, 0x0, "C_VIS197._CH")
    Jump("loc_60C2")

    label("loc_608A")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60C2")
    OP_C5(0x0, 0x0, 0x0, 0x190, 0x12C, 0x78, 0x5A, 0x280, 0x12C, 0x14, 0x0, 0x1A4, 0x12C, 0xFFFFFF, 0x0, "C_VIS197._CH")

    label("loc_60C2")

    Return()

    # Function_8_5D49 end

    def Function_9_60C3(): pass

    label("Function_9_60C3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60E4")
    OP_3F(0x151, 1)
    Jump("loc_66BB")

    label("loc_60E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66BB")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #310
        "\x07\x05Choose member to remove Zero Field Generator from.\x02",
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6161")
    Call(1, 10)
    Jump("loc_6165")

    label("loc_6161")

    Call(1, 11)

    label("loc_6165")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_618C")
    Call(1, 10)
    Jump("loc_6190")

    label("loc_618C")

    Call(1, 11)

    label("loc_6190")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61B7")
    Call(1, 10)
    Jump("loc_61BB")

    label("loc_61B7")

    Call(1, 11)

    label("loc_61BB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61E2")
    Call(1, 10)
    Jump("loc_61E6")

    label("loc_61E2")

    Call(1, 11)

    label("loc_61E6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_622D"),
        (1, "loc_6273"),
        (2, "loc_62B9"),
        (3, "loc_62FF"),
        (SWITCH_DEFAULT, "loc_6345"),
    )


    label("loc_622D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6250")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6270")

    label("loc_6250")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6270")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6270")

    Jump("loc_6345")

    label("loc_6273")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6296")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_62B6")

    label("loc_6296")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62B6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_62B6")

    Jump("loc_6345")

    label("loc_62B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62DC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_62FC")

    label("loc_62DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62FC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_62FC")

    Jump("loc_6345")

    label("loc_62FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6322")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6342")

    label("loc_6322")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6342")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6342")

    Jump("loc_6345")

    label("loc_6345")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_638C")

    AnonymousTalk(    #311
        "\x07\x05They are not equipped with a Zero Field Generator.\x02",
    )

    Jump("loc_66AC")

    label("loc_638C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63E1")

    AnonymousTalk(    #312
        (
            "\x07\x05Estelle removed her Zero Field Generator. \x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_66AC")

    label("loc_63E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6434")

    AnonymousTalk(    #313
        (
            "\x07\x05Joshua removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_66AC")

    label("loc_6434")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_648B")

    AnonymousTalk(    #314
        (
            "\x07\x05Scherazard removed her Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_66AC")

    label("loc_648B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64DF")

    AnonymousTalk(    #315
        (
            "\x07\x05Olivier removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_66AC")

    label("loc_64DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6530")

    AnonymousTalk(    #316
        (
            "\x07\x05Kloe removed her Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_66AC")

    label("loc_6530")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6582")

    AnonymousTalk(    #317
        (
            "\x07\x05Agate removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_66AC")

    label("loc_6582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_660D")

    AnonymousTalk(    #318
        (
            "\x07\x05Tita removed her Zero Field Generator. Arts/crafts/normal\x01",
            "attacks now unavailable. S-Craft [Cannon Impulse] available.\x02",
        )
    )

    Jump("loc_66AC")

    label("loc_660D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_665D")

    AnonymousTalk(    #319
        (
            "\x07\x05Zin removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_66AC")

    label("loc_665D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66AC")

    AnonymousTalk(    #320
        (
            "\x07\x05Kevin removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )


    label("loc_66AC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_60E4")

    label("loc_66BB")

    Return()

    # Function_9_60C3 end

    def Function_10_66BC(): pass

    label("Function_10_66BC")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_66E9"),
        (1, "loc_6704"),
        (2, "loc_671E"),
        (3, "loc_673C"),
        (4, "loc_6757"),
        (5, "loc_676F"),
        (6, "loc_6788"),
        (7, "loc_67A0"),
        (8, "loc_67B7"),
        (SWITCH_DEFAULT, "loc_67D0"),
    )


    label("loc_66E9")

    OP_CC(0x1, 0x0, "[Estelle - Equipped]")
    Jump("loc_67D0")

    label("loc_6704")

    OP_CC(0x1, 0x0, "[Joshua - Equipped]")
    Jump("loc_67D0")

    label("loc_671E")

    OP_CC(0x1, 0x0, "[Scherazard - Equipped]")
    Jump("loc_67D0")

    label("loc_673C")

    OP_CC(0x1, 0x0, "[Olivier - Equipped]")
    Jump("loc_67D0")

    label("loc_6757")

    OP_CC(0x1, 0x0, "[Kloe - Equipped]")
    Jump("loc_67D0")

    label("loc_676F")

    OP_CC(0x1, 0x0, "[Agate - Equipped]")
    Jump("loc_67D0")

    label("loc_6788")

    OP_CC(0x1, 0x0, "[Tita - Equipped]")
    Jump("loc_67D0")

    label("loc_67A0")

    OP_CC(0x1, 0x0, "[Zin - Equipped]")
    Jump("loc_67D0")

    label("loc_67B7")

    OP_CC(0x1, 0x0, "[Kevin - Equipped]")
    Jump("loc_67D0")

    label("loc_67D0")

    Return()

    # Function_10_66BC end

    def Function_11_67D1(): pass

    label("Function_11_67D1")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_67FE"),
        (1, "loc_681D"),
        (2, "loc_683B"),
        (3, "loc_685D"),
        (4, "loc_687C"),
        (5, "loc_6898"),
        (6, "loc_68B5"),
        (7, "loc_68D1"),
        (8, "loc_68EC"),
        (SWITCH_DEFAULT, "loc_6909"),
    )


    label("loc_67FE")

    OP_CC(0x1, 0x0, "[Estelle - Not Equipped]")
    Jump("loc_6909")

    label("loc_681D")

    OP_CC(0x1, 0x0, "[Joshua - Not Equipped]")
    Jump("loc_6909")

    label("loc_683B")

    OP_CC(0x1, 0x0, "[Scherazard - Not Equipped]")
    Jump("loc_6909")

    label("loc_685D")

    OP_CC(0x1, 0x0, "[Olivier - Not Equipped]")
    Jump("loc_6909")

    label("loc_687C")

    OP_CC(0x1, 0x0, "[Kloe - Not Equipped]")
    Jump("loc_6909")

    label("loc_6898")

    OP_CC(0x1, 0x0, "[Agate - Not Equipped]")
    Jump("loc_6909")

    label("loc_68B5")

    OP_CC(0x1, 0x0, "[Tita - Not Equipped]")
    Jump("loc_6909")

    label("loc_68D1")

    OP_CC(0x1, 0x0, "[Zin - Not Equipped]")
    Jump("loc_6909")

    label("loc_68EC")

    OP_CC(0x1, 0x0, "[Kevin - Not Equipped]")
    Jump("loc_6909")

    label("loc_6909")

    Return()

    # Function_11_67D1 end

    SaveToFile()

Try(main)
