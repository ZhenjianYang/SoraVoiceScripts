from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1410   ._SN',
        MapName             = 'Bose',
        Location            = 'C1410.x',
        MapIndex            = 62,
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
        'Whemler',                              # 9
        'Agate',                                # 10
        'Target Camera',                        # 11
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
        'ED6_DT07/CH01680 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
    )

    DeclNpc(
        X                   = 3200,
        Z                   = 0,
        Y                   = 33900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_14F",          # 01, 1
        "Function_2_150",          # 02, 2
        "Function_3_166",          # 03, 3
        "Function_4_E75",          # 04, 4
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126")

    label("loc_126")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_14E")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_14E")

    Return()

    # Function_0_11A end

    def Function_1_14F(): pass

    label("Function_1_14F")

    Return()

    # Function_1_14F end

    def Function_2_150(): pass

    label("Function_2_150")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_165")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_150")

    label("loc_165")

    Return()

    # Function_2_150 end

    def Function_3_166(): pass

    label("Function_3_166")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(3000, 1500, 39360, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 2800, 0, 38100, 270)
    SetChrPos(0x10, 3140, 0, 36980, 270)
    SetChrPos(0x112, 540, 0, 37040, 90)
    SetChrPos(0x111, 440, 0, 37840, 90)
    SetChrPos(0x113, 340, 0, 38640, 90)

    def lambda_219():
        OP_6D(3000, 0, 39360, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_219)

    def lambda_231():
        OP_67(0, 4800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_231)
    FadeToBright(2000, 0)
    WaitChrThread(0x12, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x111,
        (
            "#1749F#6PWhen I found out we were gonna be doing our\x01",
            "final exam outside Ruan, I was so excited...\x01",
            "Didn't think it was gonna be a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x113,
        (
            "#1765F#6PSame here. Who'd have figured we'd end up\x01",
            "dragged out to a cabin in the middle of this\x01",
            "misty-ass swamphole?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x112,
        (
            "#1755F#6PHave any of us even been outside of Ruan\x01",
            "before?\x02\x03",

            "#1754FWhy'd our first taste of fresh air have to be\x01",
            "somewhere so WEIRD?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x111,
        (
            "#1744F#6PIt's not like we're here on vacation.\x02\x03",

            "#1740FWe're here as part of our training! Can't expect\x01",
            "to get taken to a theme park or somethin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x112,
        "#1751F#6PI guess. Wow, that's so grown up of you!\x02",
    )

    CloseMessageWindow()

    def lambda_4C3():
        OP_6D(3500, 0, 39360, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_4C3)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    WaitChrThread(0x12, 0x0)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #5
        0x11,
        (
            "#051F#11PHeh. Glad one of you's got his head screwed on.\x02\x03",

            "#053FI thought I was gonna have to give you guys\x01",
            "a lecture on why you're here, but maybe I can\x01",
            "spare myself the boring crap after all.\x02\x03",

            "#050FAnyway, that's enough shootin' the shit here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x111,
        "#1742F#6PS-Sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x113,
        "#1763F#6PBah. Always gotta talk down to us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#053F#11PAs you know, this final exam is what determines\x01",
            "whether you pass your training or not.\x02\x03",

            "It all hinges on this. Pass, and you're all junior\x01",
            "bracers from here on. Fail, and you ain't.\x02\x03",

            "#051FEither way, let me say this.\x02\x03",

            "I'm impressed you've made it this far without\x01",
            "dropping out. I wasn't sure you had it in you,\x01",
            "but you sure as hell proved me wrong.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x111,
        "#1743F#6PD-Did he just praise us...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x112,
        "#1753F#6PWh-What's gotten into him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x113,
        "#1764F#6PI think I'm gonna be sick.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x11,
        (
            "#555F#11PWhat kinda heartless monster do you guys\x01",
            "think I am?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x113,
        (
            "#1761FJust hurry up and spill the details.\x02\x03",

            "I'm gettin' sick of standing around\x01",
            "here. I wanna get started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#051F#11PThat shows balls. Good.\x02\x03",

            "#053FAll right. Let's get down to it, then.\x02\x03",

            "#050FYour task's simple enough. You're gonna make your\x01",
            "way through a cave full of monsters. Get to the end,\x01",
            "and you pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x111,
        "#1743F#6PA-A cave?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x112,
        (
            "#1753F#6PI thought our exam was gonna be in this valley...\x01",
            "We gotta go somewhere else now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#051F#11PQuit whinin'. It's not far from here.\x02\x03",

            "#053FIt'll be harder than it sounds, but if you get to\x01",
            "the end in one piece, you get your badges.\x02\x03",

            "I'm not giving you a strict time limit, but the\x01",
            "longer you take, the longer you keep me waitin',\x01",
            "so don't push your luck.\x02\x03",

            "#050FThat's it. Any questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x111,
        (
            "#1744F#6PSounds easy.\x02\x03",

            "#1741FAll we have to do is go for a walk\x01",
            "while beating up some monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x112,
        "#1756F#6PThis exam was made for us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x113,
        "#1761F#6PThis should be kinda fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        "#551F#11P...That's a no to the questions, I guess.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)
    Sleep(300)

    ChrTalk(    #22
        0x11,
        (
            "#051F#5PWell, Whemler?\x02\x03",

            "I'll be countin' on you to back 'em up for me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)
    Sleep(300)

    ChrTalk(    #23
        0x10,
        "#12PWell, if you insist...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#12PYou're sure they're up for this, though?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#053F#5PIt'll be fine. Trust me.\x02\x03",

            "#051FOkay. Let's get our butts over to that cave.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DC4():
        OP_8E(0xFE, 0x8C, 0x0, 0x8C78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DC4)
    Sleep(300)

    def lambda_DE4():

        label("loc_DE4")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_DE4")

    QueueWorkItem2(0x111, 2, lambda_DE4)

    def lambda_DF5():

        label("loc_DF5")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_DF5")

    QueueWorkItem2(0x112, 2, lambda_DF5)

    def lambda_E06():

        label("loc_E06")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_E06")

    QueueWorkItem2(0x113, 2, lambda_E06)

    def lambda_E17():
        OP_8F(0xFE, 0x0, 0x0, 0x9092, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_E17)
    Sleep(600)
    FadeToDark(2000, 0, -1)
    OP_43(0x10, 0x3, 0x0, 0x4)
    WaitChrThread(0x11, 0x1)

    def lambda_E4D():
        OP_8E(0xFE, 0xFFFFEAE8, 0x0, 0x8C78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E4D)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_166 end

    def Function_4_E75(): pass

    label("Function_4_E75")


    def lambda_E7B():
        OP_8E(0xFE, 0x53C, 0x0, 0x9074, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E7B)
    WaitChrThread(0x10, 0x1)

    def lambda_E9B():
        OP_8E(0xFE, 0x8C, 0x0, 0x8C78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E9B)
    WaitChrThread(0x10, 0x1)

    def lambda_EBB():
        OP_8E(0xFE, 0xFFFFEAE8, 0x0, 0x8C78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_EBB)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_4_E75 end

    SaveToFile()

Try(main)
