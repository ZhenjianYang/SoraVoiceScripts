from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3100   ._SN',
            'ED6_DT21/T3100_1 ._SN',
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
        "Function_1_9AC",          # 01, 1
        "Function_2_1222",         # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D")

    ChrTalk(    #0
        0x101,
        (
            "#1004FAh!\x02\x03",

            "Holy crap!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_111")

    ChrTalk(    #1
        0x106,
        "#052FFind somethin'?\x02",
    )

    CloseMessageWindow()
    Jump("loc_133")

    label("loc_111")


    ChrTalk(    #2
        0x103,
        "#023FDid you find something?\x02",
    )

    CloseMessageWindow()

    label("loc_133")


    ChrTalk(    #3
        0x101,
        "#1002FYeah... You could say that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36D")

    label("loc_15D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C5")

    ChrTalk(    #4
        0x106,
        (
            "#052FHm?\x02\x03",

            "Ah-ha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1002FDid you find something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x106,
        "#050FYeah, check this out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36D")

    label("loc_1C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_239")

    ChrTalk(    #7
        0x103,
        (
            "#023FOh!\x02\x03",

            "Could this be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1002FDid you find something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        "#027FEstelle, look at this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36D")

    label("loc_239")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")

    ChrTalk(    #10
        0x105,
        (
            "#044FAh...!\x02\x03",

            "Estelle, look at this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1002FDid you find something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_36D")

    label("loc_294")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")

    ChrTalk(    #12
        0x104,
        "#033FOh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1002FOlivier, did you find something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x104,
        "#035FLook at this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36D")

    label("loc_2F8")


    ChrTalk(    #15
        0x107,
        (
            "#064FHuh?\x02\x03",

            "Oh, there it is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1002FDid you find something?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #17
        0x107,
        (
            "#062FY-Yeah.\x02\x03",

            "Look at this, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D")

    OP_59()
    Fade(1000)
    EventBegin(0x0)
    OP_6D(35000, 500, 87940, 0)
    OP_67(0, 8109, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(143000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 36310, 0, 87490, 280)
    SetChrPos(0xF7, 35950, 0, 86340, 310)
    SetChrPos(0xF8, 37540, 0, 85600, 329)
    SetChrPos(0xF9, 37230, 0, 84600, 328)
    OP_0D()
    Sleep(400)
    OP_8E(0x101, 0x88C2, 0x1F4, 0x157B6, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")

    ChrTalk(    #18
        0x101,
        (
            "#1002F#6PThere's no doubt about it.\x02\x03",

            "That's his card.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5")

    label("loc_45A")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #19
        0x101,
        (
            "#1002F#6PNo doubt about it.\x02\x03",

            "This card has GOT to be his.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4E2")

    ChrTalk(    #20
        0x106,
        "#050FSo what's written on it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_505")

    label("loc_4E2")


    ChrTalk(    #21
        0x103,
        "#022FSo what's written on it?\x02",
    )

    CloseMessageWindow()

    label("loc_505")


    ChrTalk(    #22
        0x101,
        "#1002F#6POne second...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)
    Fade(1000)
    OP_6D(36720, 0, 87530, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(309000, 0)
    OP_6E(262, 0)
    OP_71(0x16, 0x4)
    SetChrPos(0x101, 35000, 500, 87760, 270)
    SetChrPos(0xF8, 37880, 0, 87320, 270)
    SetChrPos(0xF7, 37790, 0, 86040, 315)
    SetChrPos(0xF9, 39170, 0, 86460, 270)
    OP_0D()
    Sleep(400)
    OP_8C(0x101, 90, 400)
    OP_8F(0x101, 0x8DFE, 0x0, 0x1548C, 0x7D0, 0x0)
    Fade(1000)
    SetChrChipByIndex(0x101, 11)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05'Beauteous princess and her companions.\x01",
            "That which you seek is yet far off.'\x02\x03",

            "'Your second key is in the central factory.\x01",
            "Search within the [Wisest One].'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #24
        0x101,
        "#1002F#6PAaaaand that's it for our next hint.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_742")

    ChrTalk(    #25
        0x106,
        (
            "#051F#1PNext stop's the central factory,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77C")

    label("loc_742")


    ChrTalk(    #26
        0x103,
        (
            "#020F#1PI see. Our next stop is the\x01",
            "central factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C")


    ChrTalk(    #27
        0x101,
        (
            "#1002F#6PYeah, we know the place, but...\x02\x03",

            "Who do you think this 'Wisest One' is?\x02\x03",

            "#1007FIt's not Professor Russell, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_85D")

    ChrTalk(    #28
        0x106,
        (
            "#050F#1PWell, whoever it is, we know where\x01",
            "we'll find it.\x02\x03",

            "Let's go check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D7")

    label("loc_85D")


    ChrTalk(    #29
        0x103,
        (
            "#020F#1PMmmm, whoever it is, we know where\x01",
            "our next clue can be found, at least.\x02\x03",

            "Let's go and see what we can find.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FD")

    ChrTalk(    #30
        0x104,
        "#031FLet's be off.\x02",
    )

    CloseMessageWindow()

    label("loc_8FD")


    ChrTalk(    #31
        0x101,
        "#1006F#6PYeah, let's go.\x02",
    )

    CloseMessageWindow()
    OP_64(0x3, 0x1)

    def lambda_925():
        OP_8E(0x0, 0x9902, 0x0, 0x151BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_925)

    def lambda_940():
        OP_8E(0x1, 0x9902, 0x0, 0x151BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_940)

    def lambda_95B():
        OP_8E(0x2, 0x9902, 0x0, 0x151BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_95B)

    def lambda_976():
        OP_8E(0x3, 0x9902, 0x0, 0x151BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_976)
    OP_69(0xF9, 0x3E8)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    OP_6A(0xFF)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_9AC(): pass

    label("Function_1_9AC")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 58240, 0, 48320, 270)
    SetChrPos(0xF7, 59110, 0, 47500, 270)
    SetChrPos(0xF8, 59440, 0, 48970, 270)
    SetChrPos(0xF9, 60100, 0, 48320, 270)
    OP_6D(56710, 0, 46620, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #32
        0x101,
        (
            "#1011F#5PHere are three chimneys at different\x01",
            "heights.\x02\x03",

            "#1015FHey, don't you think this could be the\x01",
            "'Three Hatted Brothers'?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ABE():
        OP_6D(52980, 0, 43380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ABE)
    OP_67(0, 10800, -10000, 2000)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B64")

    ChrTalk(    #33
        0x107,
        (
            "#060F#2PEach of the chimneys is a little different\x01",
            "in height.\x02\x03",

            "#061FHeehee. They're like real siblings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC")

    label("loc_B64")


    ChrTalk(    #34
        0x105,
        (
            "#040F#2PAll three are at different heights.\x02\x03",

            "I see.. Perhaps this is what was\x01",
            "meant by 'brothers.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C62")

    ChrTalk(    #35
        0x106,
        (
            "#050F#1PSeems like it's the only building with\x01",
            "three chimneys at different heights.\x02\x03",

            "I'd say it's possible. Why don't we\x01",
            "check it out?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEE")

    label("loc_C62")


    ChrTalk(    #36
        0x103,
        (
            "#020F#1PThis seems to be the only building with\x01",
            "three chimneys at different heights.\x02\x03",

            "I'd say it's possible. Why don't we\x01",
            "have a look?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEE")

    OP_59()

    def lambda_CF5():
        OP_6D(56710, 0, 46620, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CF5)

    def lambda_D0D():
        OP_8E(0x101, 0xDE30, 0x0, 0xBCC0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0D)
    OP_6D(59550, 0, 47740, 2000)
    WaitChrThread(0x101, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #37
        "\x07\x05There was a card stuck to the chimney pipe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #38
        0x101,
        "#1018F#5PAll right, found it!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_DB1():
        OP_6D(59080, 0, 48310, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DB1)

    def lambda_DC9():
        OP_67(0, 7560, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_DC9)

    def lambda_DE1():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_DE1)
    OP_8C(0x101, 90, 400)
    OP_8E(0x101, 0xE380, 0x0, 0xBCC0, 0x7D0, 0x0)

    def lambda_E0C():
        TurnDirection(0xF7, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_E0C)

    def lambda_E1A():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_E1A)

    def lambda_E28():
        TurnDirection(0xF9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_E28)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x13, 0x2)
    WaitChrThread(0x13, 0x3)
    Fade(1000)
    SetChrChipByIndex(0x101, 11)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x07\x05'The door has already been opened. Let the\x01",
            "souls of heroes descend into the quiet earth.'\x02\x03",

            "'Raise your voice high and chant to the\x01",
            "goddess: C-26D-E!'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #40
        0x101,
        (
            "#1007F#4PPhew! I think this next step is the last.\x01",
            "(Please let it be the last one...)\x02\x03",

            "#1015FStill, 'chant to the Goddess' in\x01",
            "'the quiet earth,' of all things...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AC")

    ChrTalk(    #41
        0x104,
        (
            "#032FThe 'quiet earth' is probably exactly\x01",
            "what it sounds like: somewhere\x01",
            "underground.\x02\x03",

            "The problem is 'goddess' and the\x01",
            "incomprehensible part after that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1150")

    label("loc_10AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(    #42
        0x105,
        (
            "#042FThe 'quiet earth' probably refers to\x01",
            "somewhere underground, but...\x02\x03",

            "I don't know what to make of 'goddess'\x01",
            "and the strange part after that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1150")


    ChrTalk(    #43
        0x101,
        (
            "#1006F#4PWell, for now, let's go 'underground.'\x02\x03",

            "There's only one place I think of\x01",
            "when you say 'underground' in Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_11FB")

    ChrTalk(    #44
        0x106,
        "#051F#3PYeah, let's get goin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_121F")

    label("loc_11FB")


    ChrTalk(    #45
        0x103,
        "#020F#3PYeah, let's get going.\x02",
    )

    CloseMessageWindow()

    label("loc_121F")

    EventEnd(0x0)
    Return()

    # Function_1_9AC end

    def Function_2_1222(): pass

    label("Function_2_1222")

    EventBegin(0x0)
    SetChrPos(0xF, 28770, 0, 61520, 71)
    SetChrPos(0x101, 27390, 0, 60100, 71)
    SetChrPos(0xF7, 26830, 0, 61050, 61)
    SetChrPos(0xF8, 27120, 0, 59000, 71)
    SetChrPos(0xF9, 26310, 0, 59830, 71)
    ClearChrFlags(0xF, 0x80)
    OP_4A(0x9, 255)
    SetChrFlags(0x10, 0x8)
    OP_72(0x1, 0x4)
    OP_71(0x15, 0x4)
    OP_64(0x2, 0x1)
    OP_6D(29300, 10850, 62850, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(330000, 0)
    OP_6E(262, 0)

    def lambda_12D8():
        OP_6D(29300, 1900, 63800, 6000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_12D8)

    def lambda_12F0():
        OP_67(0, 5320, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_12F0)

    def lambda_1308():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1308)

    def lambda_1318():
        OP_6C(296000, 6000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_1318)
    OP_0D()
    Sleep(2000)
    WaitChrThread(0x13, 0x3)
    Sleep(2000)

    def lambda_1338():
        OP_6D(26280, 0, 60230, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1338)

    def lambda_1350():
        OP_6C(283000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_1350)

    def lambda_1360():
        OP_8C(0xF7, 61, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1360)
    OP_8C(0xF, 250, 400)
    WaitChrThread(0x13, 0x3)

    ChrTalk(    #46
        0xF,
        (
            "#791FYou did well to reclaim it.\x02\x03",

            "I had every confidence in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1006FGlad we were able to live up\x01",
            "to your expectations.\x02\x03",

            "#1007FBut, man, this time we really got\x01",
            "jerked around by Phantom Thief B.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_14CA")

    ChrTalk(    #48
        0x106,
        (
            "#053F#6PYeah, feels like once again we got\x01",
            "a good picture of how strong he is.\x02\x03",

            "#050FMaybe that was his goal all along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1555")

    label("loc_14CA")


    ChrTalk(    #49
        0x103,
        (
            "#026F#6PYes, it feels like once again we got a\x01",
            "good picture of just how strong he is.\x02\x03",

            "#022FPerhaps that was his intention all along.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1555")

    OP_8C(0x101, 307, 400)

    ChrTalk(    #50
        0x101,
        (
            "#1002FHe's trying to intimidate us by showing\x01",
            "off his power, in other words?\x02\x03",

            "#1015FDunno if he thought it through that far,\x01",
            "but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xF,
        (
            "#792FOne way or the other, it's obvious he's\x01",
            "no ordinary foe.\x02\x03",

            "#790FBe sure to tread with caution.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168F")

    ChrTalk(    #52
        0x104,
        "#030F#3PWise words from a wise woman.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16B6")

    label("loc_168F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B6")

    ChrTalk(    #53
        0x107,
        "#062F#3PYes, ma'am!\x02",
    )

    CloseMessageWindow()

    label("loc_16B6")

    OP_8C(0x101, 71, 400)
    Sleep(400)

    ChrTalk(    #54
        0x101,
        "#1002FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "#791FThis task is officially complete.\x02\x03",

            "With that, I'd like for you to return\x01",
            "to your main mission.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_175D")

    ChrTalk(    #56
        0x106,
        "#050F#6PGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1776")

    label("loc_175D")


    ChrTalk(    #57
        0x103,
        "#020F#6PUnderstood.\x02",
    )

    CloseMessageWindow()

    label("loc_1776")


    ChrTalk(    #58
        0xF,
        "#790FIf you'll excuse me.\x02",
    )

    CloseMessageWindow()

    def lambda_179B():

        label("loc_179B")

        TurnDirection(0x0, 0xF, 0)
        OP_48()
        Jump("loc_179B")

    QueueWorkItem2(0x0, 1, lambda_179B)

    def lambda_17AC():

        label("loc_17AC")

        TurnDirection(0x1, 0xF, 0)
        OP_48()
        Jump("loc_17AC")

    QueueWorkItem2(0x1, 1, lambda_17AC)

    def lambda_17BD():

        label("loc_17BD")

        TurnDirection(0x2, 0xF, 0)
        OP_48()
        Jump("loc_17BD")

    QueueWorkItem2(0x2, 1, lambda_17BD)

    def lambda_17CE():

        label("loc_17CE")

        TurnDirection(0x3, 0xF, 0)
        OP_48()
        Jump("loc_17CE")

    QueueWorkItem2(0x3, 1, lambda_17CE)
    OP_8E(0xF, 0x6932, 0x0, 0xF726, 0x7D0, 0x0)
    OP_8C(0xF, 0, 400)
    OP_70(0xC, 0x1D)
    OP_73(0xC)
    OP_8E(0xF, 0x6932, 0x0, 0xFD3E, 0x7D0, 0x0)
    OP_72(0xC, 0x800)
    OP_6F(0xC, 29)
    OP_70(0xC, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xC)
    OP_71(0xC, 0x800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #59
        "Quest #2C[The Stolen Sign] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xF, 0x80)
    OP_4B(0x9, 255)
    SetChrPos(0x10, 13900, 0, 58910, 227)
    ClearChrFlags(0x10, 0x8)
    EventEnd(0x0)
    Return()

    # Function_2_1222 end

    SaveToFile()

Try(main)
