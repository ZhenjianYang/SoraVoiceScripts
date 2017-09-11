from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3119_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3119.x',
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_256")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #0
        0x102,
        (
            "#010FHmmm...\x01",
            "No reaction from Antoine yet.\x02\x03",

            "At this rate, we'll just have\x01",
            "to keep searching the factory.\x02\x03",

            "There may be some kind of clue\x01",
            "here, like Dr. Miriam said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#003FUgh... Not like we have much\x01",
            "choice in the matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A")

    label("loc_1BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_1D9")

    label("loc_1D2")

    TurnDirection(0x102, 0x0, 400)

    label("loc_1D9")


    ChrTalk(    #2
        0x102,
        (
            "#010FHmmm...\x01",
            "No reaction from Antoine yet.\x02\x03",

            "Let's go check out Chief Murdock's\x01",
            "office, on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A")

    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Return()

    label("loc_256")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_2D7")
    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        (
            "Uh, can I help you folks\x01",
            "with something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I trust I'm no longer under\x01",
            "suspicion...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_2D7")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(400, 0, 9640, 0)
    SetChrPos(0x101, 450, 0, 9220, 358)
    SetChrPos(0x102, 1650, 0, 9460, 322)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_330")
    SetChrPos(0x107, 1160, 0, 8750, 357)

    label("loc_330")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34F")
    SetChrPos(0x106, -720, 0, 8630, 37)

    label("loc_34F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E")
    SetChrPos(0x13C, -590, 0, 9610, 42)

    label("loc_36E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_388")

    def lambda_380():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_380)

    label("loc_388")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A2")

    def lambda_39A():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_39A)

    label("loc_3A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BC")

    def lambda_3B4():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3B4)

    label("loc_3BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D6")

    def lambda_3CE():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3CE)

    label("loc_3D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F0")

    def lambda_3E8():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_3E8)

    label("loc_3F0")

    TurnDirection(0x8, 0x101, 0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #5
        0xFE,
        "Hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Did you find what you were\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#000FOh...uh, yeah, we did.\x02\x03",

            "We're just looking for something\x01",
            "different now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #8
        0xFE,
        "Different...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#010FYes. Some cigarettes were taken\x01",
            "from the clinic.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #10
        0xFE,
        "Heh. Someone actually did that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I imagine you're being kept\x01",
            "pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010FHave you been in the clinic\x01",
            "at any time today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "No, I haven't.\x01",
            "I've been here all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "You're welcome to search\x01",
            "the room, if you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#505FHmmm... Well, he doesn't SEEM\x01",
            "suspicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#017FYeah...\x01",
            "I think he's a dead end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Well? Am I still under suspicion?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#010FSorry to have taken up\x01",
            "your time.\x02\x03",

            "We'd appreciate your future\x01",
            "cooperation with our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Sure, no problem.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_4B(0xFE, 255)
    OP_28(0x2C, 0x1, 0x20)
    Jump("loc_10F3")

    label("loc_6F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_9DB")
    EventBegin(0x0)
    OP_4A(0xFE, 255)
    Fade(1000)
    OP_6D(400, 0, 9640, 0)
    SetChrPos(0x101, 450, 0, 9220, 358)
    SetChrPos(0x102, 1650, 0, 9460, 322)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75E")
    SetChrPos(0x107, 1160, 0, 8750, 357)

    label("loc_75E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77D")
    SetChrPos(0x106, -720, 0, 8630, 37)

    label("loc_77D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79C")
    SetChrPos(0x13C, -590, 0, 9610, 42)

    label("loc_79C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B6")

    def lambda_7AE():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7AE)

    label("loc_7B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D0")

    def lambda_7C8():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7C8)

    label("loc_7D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EA")

    def lambda_7E2():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7E2)

    label("loc_7EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_804")

    def lambda_7FC():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7FC)

    label("loc_804")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81E")

    def lambda_816():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_816)

    label("loc_81E")

    TurnDirection(0x8, 0x101, 400)
    OP_0D()

    ChrTalk(    #20
        0xFE,
        (
            "Uh, can I help you folks\x01",
            "with something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I trust I'm no longer under\x01",
            "suspicion...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#000FJust a moment...\x01",
            "We're almost done.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B7():
        TurnDirection(0x102, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B7)

    def lambda_8C5():
        TurnDirection(0x107, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8C5)
    TurnDirection(0x101, 0x13C, 400)

    ChrTalk(    #23
        0x13C,
        "...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x13C, 0x101, 400)

    ChrTalk(    #24
        0x13C,
        "...Nyao?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x107,
        "#063FNo reaction...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #26
        0x102,
        (
            "#010FSorry to have disturbed you.\x02\x03",

            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_965():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_965)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #27
        0x101,
        "#000FSeeya later!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #28
        0xFE,
        "Wh-What was THAT about...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_4B(0xFE, 255)
    OP_28(0x2C, 0x1, 0x40)
    Jump("loc_ECB")

    label("loc_9DB")

    EventBegin(0x0)
    OP_4A(0xFE, 255)
    Fade(1000)
    OP_6D(400, 0, 9640, 0)
    SetChrPos(0x101, 450, 0, 9220, 358)
    SetChrPos(0x102, 1650, 0, 9460, 322)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A38")
    SetChrPos(0x107, 1160, 0, 8750, 357)

    label("loc_A38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A57")
    SetChrPos(0x106, -720, 0, 8630, 37)

    label("loc_A57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A76")
    SetChrPos(0x13C, -590, 0, 9610, 42)

    label("loc_A76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A90")

    def lambda_A88():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A88)

    label("loc_A90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAA")

    def lambda_AA2():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AA2)

    label("loc_AAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC4")

    def lambda_ABC():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_ABC)

    label("loc_AC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADE")

    def lambda_AD6():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AD6)

    label("loc_ADE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF8")

    def lambda_AF0():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_AF0)

    label("loc_AF8")

    TurnDirection(0x8, 0x101, 400)
    OP_0D()

    ChrTalk(    #29
        0xFE,
        "Hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Did you find what you were\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#000FOh...uh, yeah, we did.\x02\x03",

            "We're just looking for something\x01",
            "different now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #32
        0xFE,
        "Different...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#010FYes. Some cigarettes were taken\x01",
            "from the clinic.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #34
        0xFE,
        "Heh. Someone actually did that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I imagine you're being kept\x01",
            "pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#010FHave you been in the clinic\x01",
            "at any time today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "No, I haven't.\x01",
            "I've been here all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "You're welcome to search\x01",
            "the room, if you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#505FHmmm... Well, he doesn't SEEM\x01",
            "suspicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#017FYeah...\x01",
            "I think he's a dead end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Well? Am I still under suspicion?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#004FOh, right. What do you\x01",
            "think, Antoine?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D99():
        TurnDirection(0x102, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D99)

    def lambda_DA7():
        TurnDirection(0x107, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_DA7)
    TurnDirection(0x101, 0x13C, 400)

    ChrTalk(    #43
        0x13C,
        "...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x13C, 0x101, 400)

    ChrTalk(    #44
        0x13C,
        "...Nyao?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x107,
        "#063FNo reaction...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#000FSo much for that, then.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #47
        0x102,
        (
            "#010FSorry to have taken up your time.\x02\x03",

            "We'd appreciate your future\x01",
            "cooperation with our investigation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E8E():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_E8E)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #48
        0xFE,
        "Sure, no problem.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_4B(0xFE, 255)
    OP_28(0x2C, 0x1, 0x20)
    OP_28(0x2C, 0x1, 0x40)

    label("loc_ECB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_10F3")

    def lambda_EDC():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EDC)
    TurnDirection(0x101, 0x102, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_FE4")

    ChrTalk(    #49
        0x101,
        (
            "#505FHmmm...\x01",
            "No response on either one.\x02\x03",

            "I guess that means that we should\x01",
            "go back to where he did react, and\x01",
            "check it over more thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        (
            "#010FSo back to the chief's office\x01",
            "on the second floor, then?\x02\x03",

            "No point in waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10ED")

    label("loc_FE4")


    ChrTalk(    #51
        0x101,
        (
            "#505FHmmm...\x01",
            "No response on either one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#013FWhich means no leads.\x02\x03",

            "#010FAt this rate, we'll just have\x01",
            "to keep searching the factory.\x02\x03",

            "There may be some kind of clue\x01",
            "here, like Dr. Miriam said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#003FUgh... Not like we have much\x01",
            "choice in the matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10ED")

    OP_28(0x2C, 0x1, 0x80)

    label("loc_10F3")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
